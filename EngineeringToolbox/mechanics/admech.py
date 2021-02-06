import numpy as np

def tensorToVector(tensor):
    vec = [tensor[i][i] for i in range(3)]
    vec += [tensor[2][1]]
    vec += [tensor[0][2]]
    vec += [tensor[0][1]]
    vec = np.array(vec).reshape(len(vec),1)
    
    return vec

def vectorToTensor(vec):
    tens = [[vec[0][0],vec[5][0],vec[4][0]],
            [vec[5][0],vec[1][0],vec[3][0]],
            [vec[4][0],vec[3][0],vec[2][0]]]
    
    return tens

def getC(E,nu):
    # eps = C sig
    C = [[1,-nu,-nu,0,0,0],
         [-nu,1,-nu,0,0,0],
         [-nu,-nu,1,0,0,0],
         [0,0,0,1+nu,0,0],
         [0,0,0,0,1+nu,0],
         [0,0,0,0,0,1+nu]]
    C = [[1/E*v for v in L] for L in C]
    
    return C

def getS(E,nu):
    # sig = S eps
    S = [[1-nu,nu,nu,0,0,0],
         [nu,1-nu,nu,0,0,0],
         [nu,nu,1-nu,0,0,0],
         [0,0,0,1-2*nu,0,0],
         [0,0,0,0,1-2*nu,0],
         [0,0,0,0,0,1-2*nu]]
    S = [[E/( (1+nu) * (1 - (2*nu)) ) * v for v in L] for L in S]
    
    return S
