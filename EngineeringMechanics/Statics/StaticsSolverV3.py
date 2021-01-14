'''
Copyright 2020 Joshua Phillips
StaticsSolver is meant only as an additional aid for completing statics homework
so that the user can check their work. There are likely still bugs in the code.
I am not responsible for incorrect answers. If you solve the problem using only
variables, you should be able to see if the answer provided by the program is
reasonable or not.
'''

import numpy as np
import math
from sympy import symbols, Poly, integrate
import matplotlib.pyplot as plt
import numpy as np

#print('Copyright 2020 Joshua Phillips\n')
#print('StaticsSolver is meant only as an additional aid for completing statics homework')
#print('so that the user can check their work. There are likely still bugs in the code.')
#print('I am not responsible for incorrect answers. If you solve the problem using only')
#print('variables, you should be able to see if the answer provided by the program is')
#print('reasonable or not.')

class Vector:
    from math import sin,cos
    def __init__(self, vecType, a1, a2, a3, pointOfAction, tol=1e-12):
        if vecType == "Cartesian" or vecType == "c":
            self.x = a1
            self.y = a2
            self.z = a3
        elif vecType == "Magnitude" or vecType == "m":
            self.x = a1 * math.sin(a3) * math.cos(a2)
            self.y = a1 * math.sin(a3) * math.sin(a2)
            self.z = a1 * math.cos(a3)
        if type(self.x) == type(0.0) and abs(self.x) < tol:
            self.x = 0
        if type(self.y) == type(0.0) and abs(self.y) < tol:
            self.y = 0
        if type(self.z) == type(0.0) and abs(self.z) < tol:
            self.z = 0
        self.x_0 = pointOfAction[0]
        self.y_0 = pointOfAction[1]
        self.z_0 = pointOfAction[2]
    
    def disp(self):
        print("<"+str(self.x)+","+str(self.y)+","+str(self.z)+"> @ ("+str(self.x_0)+","+str(self.y_0)+","+str(self.z_0)+")")
        
    def add(f1,f2):
        return Vector('c',f1.x+f2.x,f1.y+f2.y,f1.z+f2.z,(None,None,None))
    
    def mag(self):
        return (self.x**2 + self.y**2 + self.z**2)**(1/2)
    
    def dot(f1, f2):
        return f1.x*f2.x + f1.y*f2.y + f1.z*f2.z
    
    def cross(f1, f2):
        return Vector('c',(f1.y*f2.z-f1.z*f2.y),(f1.z*f2.x-f1.x*f2.z),(f1.x*f2.y-f1.y*f2.x),(None,None,None))
    
    def unit(self):
        m = Vector.mag(self)
        return Vector('c',self.x/m,self.y/m,self.z/m,(self.x_0,self.y_0,self.z_0))
    
    def scalarMult(v, s):
        return Vector('c',v.x*s,v.y*s,v.z*s,(v.x_0,v.y_0,v.z_0))    
    def addOrigin(self,point):
        self.x_0 = point[0]
        self.y_0 = point[1]
        self.z_0 = point[2]
        
    def addComps(self,tag,c1,c2,c3):
        if tag == 'Cartesian' or tag == 'c' :
            self.x = c1
            self.y = c2
            self.z = c3
        elif tag == "Magnitude" or tag == "m":
            self.x = a1 * math.sin(a3) * math.cos(a2)
            self.y = a1 * math.sin(a3) * math.sin(a2)
            self.z = a1 * math.cos(a3)
            
    def getPointOfAction(self):
        return (self.x_0,self.y_0,self.z_0)
    
    def getEndpoint(self):
        return (self.x_0+self.x,self.y_0+self.y,self.z_0+self.z)
    
    def getComps(self):
        return (self.x,self.y,self.z)
    
zeroVec = Vector('c',0,0,0,(0,0,0))

class Load:
    X,Y,Z = 1,2,3
    
    def __init__(self,expr,start,end,axis2,axis1=1):
        self.expr = expr
        self.start = start
        self.end = end
        self.axis1 = axis1
        self.axis2 = axis2
    
    def getForce(self,start,end,num=1000):
        st = start[self.axis1-1]-self.start[self.axis1-1]
        sp = end[self.axis1-1]-self.start[self.axis1-1]
        if end[self.axis1-1] > self.end[self.axis1-1]:
            sp = self.end[self.axis1-1]-self.start[self.axis1-1]
        l = np.linspace(st,sp,num)
        w = [self.expr(l[i]) for i in range(num)]
        m = np.trapz(w,l)
        x_bar = 1/m * np.trapz([W*L for W,L in zip(w,l)],l)
        rtn = Vector('c',0,0,0,(0,0,0))
        comps = [0,0,0]
        print(comps)
        comps[self.axis2-1] = m
        print(comps)
        PoA = list(self.start)
        PoA[self.axis1-1] += x_bar
        rtn.addComps('c',*comps)
        rtn.addOrigin(tuple(PoA))
        return rtn

class Truss:
    def __init__(self,points):
        self.points = points
    
    def generateMembers(self,connections):
        # connections should be of form [(A,[B,C,D]),(B,[D,E]),...]
        ticker = 0
        self.members=[]
        self.numMembers = 0
        # construct
        self.memberForces = []
        ticker = 0
        for connSet in connections:
            p_1 = connSet[0]
            pList = connSet[1]
            for p_i in pList:
                self.numMembers += 1
                member = Vector('c',(p_i[0]-p_1[0]),(p_i[1]-p_1[1]),(p_i[2]-p_1[2]),(p_1[0],p_1[1],p_1[2]))
                self.members.append(member)
                label = 'v_'+str(ticker)
                mag = symbols(label)
                self.memberForces.append(Vector.scalarMult(member.unit(),mag))
                member = Vector('c',(p_1[0]-p_i[0]),(p_1[1]-p_i[1]),(p_1[2]-p_i[2]),(p_i[0],p_i[1],p_i[2]))
                self.members.append(member)
                label = 'v_'+str(ticker)
                mag = symbols(label)
                self.memberForces.append(Vector.scalarMult(member.unit(),mag))
                ticker += 1
    
    def showMembers(self):
        print('Number of members:',self.numMembers)
        for member in self.members:
            member.disp()
        print('\n\n')
        for member in self.memberForces:
            member.disp()
            
    def addSupports(self,supports):
        self.supports = supports
    
    def getForcesOnPoint(self,point):
        rtn = []
        for member in self.memberForces:
            if member.getPointOfAction() == point :
                rtn.append(member)
        for force in self.extForces:
            if force.getPointOfAction() == point :
                rtn.append(force)
        return rtn
    
    def addExtForces(self,extForces):
        self.extForces = extForces
        
    def getAdjacentJoints(self,point):
        rtn = []
        for member in self.members:
            if member.getPointOfAction() == point :
                rtn.append(member.getEndpoint())
        return rtn
    
    def solveByJoints(self,jointOrder,show=False):
        jointIndex = 0
        complete = False
        subsList = []
        while(not complete):
            currNode = jointOrder[jointIndex]
            forces = self.getForcesOnPoint(currNode)
            F_net = sumForces(forces)
            for pair in subsList:
                F_net.x = F_net.x.subs(pair[0],pair[1])
                F_net.y = F_net.y.subs(pair[0],pair[1])
                F_net.z = F_net.z.subs(pair[0],pair[1])
            free_vars = (F_net.x + F_net.y + F_net.z).free_symbols
            if show :
                print('\n\n\n')
                print(F_net.x)
                print(F_net.y)
                print(F_net.z)
                print(free_vars)
            if len(free_vars) == 3 :
                u = solve([F_net.x,F_net.y,F_net.z],list(free_vars))
            elif len(free_vars) == 2 :
                u = solve([F_net.x,F_net.y],list(free_vars))
            elif len(free_vars) == 1:
                u = solve([F_net.x],list(free_vars),solver='gaussElim')
            for var,val in zip(free_vars,u):
                subsList.append((var,val))
            complete = ( len(subsList) == self.numMembers )
            jointIndex += 1
        rtn = []
        for pair in subsList:
            rtn.append((pair[0],pair[1][0]))
        for mForce in self.memberForces:
            for pair in subsList:
                mForce.x = mForce.x.subs(pair[0],pair[1])
                mForce.y = mForce.x.subs(pair[0],pair[1])
                mForce.z = mForce.x.subs(pair[0],pair[1])
            mForce.x = mForce.x.subs(pair[0],pair[1])
            mForce.y = mForce.x.subs(pair[0],pair[1])
            mForce.z = mForce.x.subs(pair[0],pair[1])
        return rtn

def sumForces(forces):
    F_net = zeroVec
    for force in forces:
        F_net = Vector.add(F_net,force)
    return F_net

def sumMoments(point, forces, moments):
    x,y,z = point[0],point[1],point[2]
    M_net = zeroVec
    for force in forces:
        r = Vector('c',force.x_0-x,force.y_0-y,force.z_0-z,(x,y,z))
        M = Vector.cross(r,force)
        M_net = Vector.add(M_net,M)
    for moment in moments:
        M_net = Vector.add(M_net,moment)
    M_net.x_0 = x
    M_net.y_0 = y
    M_net.z_0 = z
    return M_net

def solve(eqs, u, slns=None, subs=None, show=False, solver='default'):
    if len(eqs) != len(u) :
        raise TypeError("Number of equations and number of variables must be the same.")
    if slns!=None and len(eqs)!=len(slns) :
        raise TypeError("Number of equations and number of solutions must be the same")
    if slns == None :
        slns = np.zeros((len(u),1))
    A = np.zeros((len(u),len(u)))
    B = slns
    # A * u = B
    for eq_i in range(len(eqs)):
        expr = eqs[eq_i]
        if subs != None:
            for i in range(len(subs)):
                expr = expr.subs(subs[i][0],subs[i][1])
        for var_i in range(len(u)):
            coeffs = Poly(expr,u[var_i]).coeffs()
            
            if len(coeffs) == 1 :
                try:
                    A[eq_i,var_i] = coeffs[0]
                    if var_i==len(u)-1 :
                        B[eq_i]=0
                        break
                except:
                    A[eq_i,var_i] = 0
                    B[eq_i] = 0
            else:
                A[eq_i,var_i] = coeffs[0]
                try:
                    B[eq_i] = -coeffs[-1]
                    break;
                except:
                    expr = coeffs[-1]

    #'''
    if show :
        print('A\n',A)
        print('\nB\n',B,'\n')
    #'''
    
    if solver == 'default' :
        rtn = np.linalg.solve(A,B)
    elif solver == 'gaussElim' :
        rtn = gaussElim(A,B)
    
    if show :
        maxAstrlen = 0
        for L in A:
            for v in L:
                if len(str(v)) > maxAstrlen:
                    maxAstrlen = len(str(v))
        maxBstrlen = 0
        for L in B:
            for v in L:
                if len(str(v)) > maxBstrlen:
                    maxBstrlen = len(str(v))
        maxustrlen = 0
        for v in u:
            if len(str(v)) > maxustrlen:
                maxustrlen = len(str(v))

        for i,(La,Lb,U) in enumerate(zip(A,B,u)):
            linstr = "["
            for v in La:
                linstr += " "*(maxAstrlen-len(str(v)))
                linstr += str(v)
                linstr += "   "
            linstr = linstr[0:len(linstr)-3]
            linstr += "]"

            if i == int(len(A)/2):
                linstr += "  *  "
            else:
                linstr += "     "

            linstr += "["
            linstr += " "*(maxustrlen-len(str(U)))
            linstr += str(U)
            linstr += "]"

            if i == int(len(A)/2):
                linstr += "  =  "
            else:
                linstr += "     "

            linstr += "["
            linstr += " "*(maxBstrlen-len(str(Lb[0])))
            linstr += str(Lb[0])
            linstr += "]"

            print(linstr)
            
        print('\n')
        
        maxRstrlen = 0
        for L in rtn:
            for v in L:
                if len(str(v)) > maxRstrlen:
                    maxRstrlen = len(str(round(v,4)))

        for i,(U,r) in enumerate(zip(u,rtn)):
            linstr = "["
            linstr += " "*(maxustrlen-len(str(U)))
            linstr += str(U)
            linstr += "]"

            if i == int(len(A)/2):
                linstr += "  =  "
            else:
                linstr += "     "

            linstr += "["
            linstr += " "*(maxRstrlen-len(str(round(r[0],4))))
            linstr += str(round(r[0],4))
            linstr += "]"

            print(linstr)
    
    return rtn

def gaussElim(A,B):
    A = np.array(A)
    B = np.array(B)
    A = np.array([np.append(A[i,:],B[i,:]) for i in range(len(A))])
    
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i,i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k,i]) > maxEl:
                maxEl = abs(A[k,i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n+1):
            tmp = A[maxRow,k]
            A[maxRow,k] = A[i,k]
            A[i,k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -A[k,i]/A[i,i]
            for j in range(i, n+1):
                if i == j:
                    A[k,j] = 0
                else:
                    A[k,j] += c * A[i,j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i,n]/A[i,i]
        for k in range(i-1, -1, -1):
            A[k,n] -= A[k,i] * x[i]
            
    rtn = list(np.array([[x_val] for x_val in x]))
    return rtn

def deg2Rad(deg):
    return deg * math.pi/180

def shearMomentDiagram(loads,forces,moments,startPt,stopPt,axis=1,num=1000,sigFigs=3,saveAs=None):
    dl = (stopPt[axis-1]-startPt[axis-1])/num
    l = np.linspace(startPt[axis-1],stopPt[axis-1],num)
    w1 = [0]*num
    w2 = [0]*num
    
    for i in range(num):
        w1[i] = sum([w.expr(l[i]) for w in loads if w.axis2 == [1,2,3][axis-2] and w.start[w.axis1-1] <= dl*i and w.end[w.axis1-1] > dl*i])
        w2[i] = sum([w.expr(l[i]) for w in loads if w.axis2 == [1,2,3][axis-3] and w.start[w.axis1-1] <= dl*i and w.end[w.axis1-1] > dl*i])
    
    v1 = [np.trapz(w1[:i],l[:i]) for i in range(num)]
    v2 = [np.trapz(w2[:i],l[:i]) for i in range(num)]
    
    for i in range(num):
        v1[i] += sum([vec.getComps()[axis-2] for vec in forces if vec.getPointOfAction()[axis-1] <= dl*i])
        v2[i] += sum([vec.getComps()[axis-3] for vec in forces if vec.getPointOfAction()[axis-1] <= dl*i])
    
    M1 = [np.trapz(v1[:i],l[:i]) for i in range(num)]
    M2 = [np.trapz(v2[:i],l[:i]) for i in range(num)]
    
    for i in range(num):
        M1[i] -= sum([vec.getComps()[axis] for vec in moments if vec.getPointOfAction()[axis-1] <= dl*i])
        M2[i] -= sum([vec.getComps()[axis-2] for vec in moments if vec.getPointOfAction()[axis-1] <= dl*i])
        
    fig,axs = plt.subplots(2,2)
    
    dir1 = ['x','y','z'][axis-2]
    dir2 = ['x','y','z'][axis-3]
    
    axs[0][0].plot(l,v2,'r')
    axs[0][0].set_title("Shear in the "+dir2)
    axs[0][0].set_xlabel("Length")
    axs[0][0].set_ylabel("Force")

    axs[1][0].plot(l,M2,'b')
    axs[1][0].set_title("Moment in the "+dir2)
    axs[1][0].set_xlabel("Length")
    axs[1][0].set_ylabel("Moment")

    axs[0][1].plot(l,v1,'r')
    axs[0][1].set_title("Shear in the "+dir1)
    axs[0][1].set_xlabel("Length")
    axs[0][1].set_ylabel("Force")

    axs[1][1].plot(l,M1,'b')
    axs[1][1].set_title("Moment in the "+dir1)
    axs[1][1].set_xlabel("Length")
    axs[1][1].set_ylabel("Moment")

    fig.tight_layout()
    
    return (l,v2,M2,v1,M1)
