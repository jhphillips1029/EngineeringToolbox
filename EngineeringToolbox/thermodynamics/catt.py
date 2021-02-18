import pandas as pd
import json
import numpy as np
import os

def getState(temp=None,press=None,fluid="water",state="SLSV",tables="Wiley",preferTemp=False,debug=False,generic=False,Sat=-1.0e-5,qual=1.0):
    # Evaluate input for errors
    if temp == None and press == None:
        raise ValueError("Either temperature (temp) or pressure (press) must be defined.")
    if state not in ["SLSV","SHV","CL"]:
        raise ValueError("State '"+state+"' not recognized.")
    if state != "SLSV" and (temp == None or press == None):
        raise ValueError("Both temperature (temp) and pressure (press) must be defined for given state.")
    
    # Parse input
    if temp != None and press == None:
        preferTemp = True
    if state == "SLSV":
        state = "sat_liq"
        
        pressORtemp = "press"
        if preferTemp:
            pressORtemp = "temp"
            
        state += "_"+pressORtemp
        
    if temp != None:
        temp = float(temp)
    if press != None:
        press = float(press)
        
    
    prefix = os.path.abspath(__file__).replace("catt.py","")+"data_tables/"

    # Get corresponding data table(s)
    data_filename = "_".join([fluid,state,tables,"metric"])
    data = None
    if "sat_liq" in state:
        data = pd.read_csv(prefix+data_filename+".csv")
    else:
        with open(prefix+data_filename+".json") as f:
            data = json.load(f)
            
    # Construct return
    rtn = pd.DataFrame()
            
    # Get pressure entry for SHV and CL
    if state in ["CL","SHV"]:
        if str(float(press)) not in data.keys():
            return "You're gonna wanna interpolate!"
        else:
            data = data[str(float(press))]
            
        for key in data.keys():
            for i in range(len(data[key])):
                if data[key][i] == "Sat.":
                    data[key][i] == -1.0e-5
                    continue
                data[key][i] = float(data[key][i])
        
        d2 = {'press':press}
        d2.update(data)
        data = d2
        data = pd.DataFrame(data=data)
        
    if debug:
        print(data)
    
    # Get specific state
    characteristic = press
    charKey = 'press'
    if state in ['CL','SHV'] or preferTemp:
        characteristic = temp
        charKey = 'temp'
        
    if debug:
        print('')
        print(characteristic,charKey)
        print('')
        print(data[charKey])
        for d in data[charKey]:
            print(type(d))
        
    chars = list(data[charKey])
    if 'Sat.' in chars:
        chars[chars.index('Sat.')] = Sat
    chars = np.array(chars)
    upper = chars[chars  > characteristic].min()
    lower = chars[chars <= characteristic].max()
    if lower == -1.0e-5:
        raise ValueError('Must provide saturation value.')
    if lower == characteristic:
        rtn = data[data[charKey]==characteristic]
    else:
        upper_index = list(chars).index(upper)
        lower_index = list(chars).index(lower)
        state = {}
        for key in data.keys():
            state[key] = (data[key][upper_index]-data[key][lower_index])/(upper-lower) * (temp-lower) + data[key][lower_index]
        rtn = pd.DataFrame(data=state,index=[0])
        
    if state not in ['CL','SHV'] and not generic:
        keys = ['temp','press','v','u','h','s']
        dat = [rtn['temp'],rtn['press']]
        v = rtn['v_f']*1.0e-3 + qual*(rtn['v_g']-rtn['v_f']*1.0e-3)
        u = rtn['u_f'] + qual*(rtn['u_g']-rtn['u_f'])
        h = rtn['h_f'] + qual*(rtn['h_g']-rtn['h_f'])
        s = rtn['s_f'] + qual*(rtn['s_g']-rtn['s_f'])
        dat += [v,u,h,s]
        state = {key:datum for key,datum in zip(keys,dat)}
        rtn = pd.DataFrame(data=state)
        
    return rtn
