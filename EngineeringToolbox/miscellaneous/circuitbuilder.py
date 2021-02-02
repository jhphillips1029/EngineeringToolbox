class Comp:
    def __init__(self,start,end=None,compType=None,labels=None,arrowType=None,node=None):
        if compType == None and node == None:
            raise TypeError("must provide component or node.")
        self.compType = compType
        self.start = start
        self.end = end
        self.labels = labels
        self.arrowType = arrowType
        self.node = node
    
    def wire(start,end,arrowType):
        return Comp(start,end=end,compType="short",arrowType=arrowType)
    
    def res(start,end,labels,arrowType):
        return Comp(start,end=end,compType="R",labels=labels,arrowType=arrowType)
    
    def Isrc(start,end,labels,arrowType):
        return Comp(start,end=end,compType="I",labels=labels,arrowType=arrowType)
    
    def Vsrc(start,end,labels,arrowType):
        return Comp(start,end=end,compType="V",labels=labels,arrowType=arrowType)
    
    def gnd(start):
        return Comp(start,end=(start[0],start[1]-0.5),node="node[ground]{}")
    
    O=(0,0)
        
def texCircuit(components):
    circuit = []
    for comp in components:
        compStr = "\\draw "+str(comp.start)+" "
        if comp.compType != None:
            compStr += "to["+comp.compType
            if comp.labels != None:
                compStr += ", "+comp.labels
            if comp.arrowType != None:
                compStr += ", "+comp.arrowType
            compStr += "]"
            if comp.end != None:
                compStr += " "+str(comp.end)
        if comp.node != None:
            if comp.end != None:
                compStr += " -- "+str(comp.end)
            compStr += " "+comp.node
        compStr += ";"
        circuit.append(compStr)
    return circuit

def Thevenin_Norton(V_OC,I_SC,R_t):
    import math
    R_label = ""
    V_label = ""
    I_label = ""
    if isinstance(V_OC,complex):
        V_label = "{} \\angle {}^o".format(round((V_OC.imag**2 + V_OC.real**2)**0.5,3),round(math.atan2(V_OC.imag,V_OC.real),3))
    else:
        V_label = str(round(V_OC,3))
    if isinstance(I_SC,complex):
        I_label = "{} \\angle {}^o".format(round((I_SC.imag**2 + I_SC.real**2)**0.5,3),round(math.atan2(I_SC.imag,I_SC.real),3))
    else:
        V_label = str(round(I_SC,3))
    if isinstance(R_t,complex):
        R_label = str(R_t)
    else:
        R_label = str(round(R_t,3))
    
    R_t1 = Comp.res((0,3),(3,3),"R=$R_t \\text{$=$} "+R_label+" \\Omega$","-o")
    R_t2 = Comp.res((15,3),(15,0),"R=$R_t \\text{$=$} "+R_label+" \\Omega$",None)
    
    V_s1 = Comp.Vsrc((0,3),(0,0),"V=$V_{OC} \\text{$=$} "+V_label+" V$",None)
    
    I_s2 = Comp.Isrc((12,0),(12,3),"I=$I_{SC} \\text{$=$} "+I_label+" A$",None)
    
    w1 = Comp.wire((0,0),(3,0),"-o")
    w2 = Comp.wire((15,3),(18,3),"-o")
    w3 = Comp.wire((15,0),(18,0),"-o")
    w4 = Comp.wire((12,0),(15,0),None)
    w5 = Comp.wire((12,3),(15,3),None)
    
    comps = [R_t1,R_t2,V_s1,I_s2,w1,w2,w3,w4,w5]
    return texCircuit(comps)
