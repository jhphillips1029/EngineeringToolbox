import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import math
import warnings
warnings.filterwarnings(action='once')

data = None;
matData = None;

def initData(csvName):
    data = pd.read_csv(csvName)
    matData = pd.DataFrame(columns=['Name','Diameter','Length','Reduced Diamter','Area','Reduced Area','UTS','Elastic Modulus','Total Fail Strain','Plastic Strain Fail','Elastic Strain Fail','Offset Yield'])

def addMaterial(matInfo):
    if len(matInfo) < len(matData.columns):
        print("Not enough entries in matInfo")
        return
    matData.loc[len(matData)] = matInfo

def area(diameter):
    return math.pi * (diameter/2)**2

def findUTS(key):
    return max(data[key])

def getYoungsModulus(stress,strain,plot=False):
    # finds the Young's Modulus by finding the largest linear slope between 1/10 the number of data points
    # returns the Young's Modulus in the same units as the input stress
    dummyData = pd.DataFrame(data={'x':strain,'y':stress})
    dummyData.dropna(inplace=True)
    x=np.array(dummyData['x'][:int(len(dummyData['x'])/2)])
    y=np.array(dummyData['y'][:int(len(dummyData['x'])/2)])

    numPts = len(x)
    minFitLength = 8

    chi = 0
    chi_min = 10000

    i_best=0
    j_best=0
    m_best=0

    for i in range(numPts - minFitLength):
        for j in range(i+minFitLength, numPts):
            coefs = np.polyfit(x[i:j],y[i:j],1)
            y_lin = x * coefs[0] + coefs[1]
            chi=0
            for k in range(i,j):
                chi += (y_lin[k] - y[k])**2
            if chi < chi_min and coefs[0] > m_best:
                i_best = i
                j_best = j
                chi_min = chi
                m_best = coefs[0]

    coefs = np.polyfit(x[i_best:j_best],y[i_best:j_best],1)
    y_lin = x[i_best:j_best] * coefs[0] + coefs[1]

    if(plot):
        plt.plot(x,y,'ro')
        plt.plot(x[i_best:j_best],y_lin,'b-')
        print("Young's Modulus (MPa): " + str(m_best))
    return m_best

def findElasticModulus(stressKey,strainKey):
    strain = data[strainKey]
    stress = data[stressKey]
    return getYoungsModulus(stress,strain)

def getFailure(stress):
    # finds the point of failure by looking for largest jump between two stresses
    # returns index of point of failure
    # stress = np.array(stress)[int(len(stress)/2):]
    maxJump=0;
    indexVal=0;
    for i in range(2,len(stress)):
        if( abs(stress[i] - stress[i-2]) > maxJump and stress[i] - stress[i-2] < 0 ):
            maxJump = abs(stress[i] - stress[i-2])
            indexVal = i
            
    return indexVal-2

def findFailure(stressKey,strainKey):
    stress = data[stressKey]
    return data[strainKey][getFailure(stress)]

def findPlasticElasticFailureStrain(stressKey,strainKey,elasticModulus,totFailStrain):
    failIndex = findFailure(data[stressKey])
    failStress = data[stressKey][failIndex]
    return [failStress/elasticModulus,totFailStrain-failStress/elasticModulus]

def getYieldStress(strain, stress, offset, E):
    x = strain
    y = stress
    x_n = x[x>0]
    x_n = x_n[y>0]
    y_n = y[x>0]
    y_n = y_n[y>0]
    dummyData = pd.DataFrame(data={'x':x_n,'y':y_n})
    dummyData.dropna(inplace=True)
    x=np.array(dummyData['x'][:int(len(dummyData['x'])/2)])
    y=np.array(dummyData['y'][:int(len(dummyData['x'])/2)])

    f=lambda x : E*(x-offset)
    
    u=np.linspace(0,0.2,100)
    v=f(u)
    
    minDiff = 1000
    index = -1
    for i in range(len(y)):
        for j in range(len(v)):
            if y[i]-v[j] < minDiff:
                minDiff = y[i]-v[j]
                index = j
                
    print(v[j])
    return v[j]

def findYieldStress(stressKey,strainKey,elasticModulus,offset=.002):
    stress = data[stressKey]
    strain = data[strainKey]
    return getYieldStress(strain,stress,offset,elasticModulus)

def writeOut(fName):
    f = open(fName,'w')
    for i in range(matData.shape[0]):
        f.write(matData['Type'][i]+'\n')
        f.write(str(matData['Diameter (mm)'][i])+'\n')
        f.write(str(matData['Length (m)'][i])+'\n')
        f.write(str(matData["Young's Modulus (MPa)"][i])+'\n')
    f.close()

def plotData(stressKeys,strainKeys,names,totalFailureStrain,fName=None):
    for i,xKey,yKey in enumerate(zip(strainKeys,stressKeys)):
        x = data[xKey]
        y = data[yKey]
        index = 0
        for j in range(len(x)):
            if x[j] == totalFailureStrain:
                index = j
        xy = [[a,b] for k, (a,b) in enumerate(zip(x,y)) if a>0 and b>0 and k<index]
        plt.plot(xy[:,0],xy[:,1],label=names[i])
    plt.xlabel('Strain')
    plt.ylabel('Stress')
    plt.title('Stress-Strain Curve')
    plt.legend(loc=(1.05,.65))
    if fName != None:
        plt.savefig(fName)
