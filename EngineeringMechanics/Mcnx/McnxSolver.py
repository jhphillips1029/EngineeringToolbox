import math
import matplotlib.pyplot as plt
import numpy as np

def plotMohrsCircle(filename,sigmaXX,sigmaYY,tauXy,center,radius,sigmaP1,sigmaP2,thetaP1,phi=None,alpha=None,sigma1=None,sigma2=None,tau1=None,thetaCutPlane=None,show=[0],units='MPa'):
    fig,axes = plt.subplots(nrows=1,ncols=len(show))
    if len(show)==1:
        axes = [axes]
    for i in range(len(axes)):
        axes[i].set_aspect('equal')
    
    axesIndex = 0
    
    if 0 in show:
        circ = plt.Circle((center,0),radius,edgecolor='#0000FF',facecolor='#FFFFFF')
        axes[axesIndex].add_artist(circ)
        axes[axesIndex].set_xlim(center-(radius+0.5*radius),center+(radius+0.75*radius))
        axes[axesIndex].set_ylim(-(radius+0.3*radius),(radius+0.3*radius))
        axes[axesIndex].plot([center],[0],'ko',[sigmaXX],[tauXY],'ro',[sigmaYY],[-tauXY],'ro',[sigmaXX,sigmaYY],[tauXY,-tauXY],'k--')
        axes[axesIndex].plot([sigmaP1],[0],'bo',[sigmaP2],[0],'bo')
        axes[axesIndex].plot([center-(radius+0.5*radius),center+(radius+0.75*radius)],[0,0],'k')
        axes[axesIndex].text(sigmaXX + 0.1*radius,tauXY,"({},{})".format(sigmaXX,tauXY),fontsize=12)
        axes[axesIndex].text(sigmaYY + 0.1*radius, -tauXY-0.25*radius, "({},{})".format(sigmaYY,-tauXY),fontsize=12)
        axes[axesIndex].text(center+0.25*radius,0.1*radius,"{}°".format(round(thetaP1*180/math.pi,3)),fontsize=12)
        axes[axesIndex].text(center+0.1*radius,-0.25*radius, "{}".format(round(center,3)),fontsize=12)
        axes[axesIndex].text(sigmaP1+0.1*radius,-0.25*radius,"s_P1",fontsize=12)
        axes[axesIndex].text(sigmaP2+0.1*radius,-0.25*radius,"s_P2",fontsize=12)
        
        axesIndex+=1
    
    if 1 in show:
        corners = [[2,4,4,2],
                   [2,2,4,4]]
        lines = [[1.5,3,3,4.5,0,3,3,6,0,3,3,6],
                 [3,1.5,4.5,3,3,0,6,3,3,0,6,3]]
        ends = [[0,3,3,6,0.25,3.25,3.25,5.75,0.25,2.75,2.75,5.75],
                [3,0,6,3,3.25,0.25,5.75,3.25,2.75,0.25,5.75,2.75]]
        R = [[math.cos(thetaP1),-math.sin(thetaP1)],
             [math.sin(thetaP1),math.cos(thetaP1)]]
        corners = [list(line) for line in np.matmul(np.array(R),np.array(corners))]
        lines = [list(line) for line in np.matmul(np.array(R),np.array(lines))]
        ends = [list(line) for line in np.matmul(np.array(R),np.array(ends))]
        corners[0].append(corners[0][0])
        corners[1].append(corners[1][0])
        axes[axesIndex].plot(corners[0],corners[1])
        for i in range(len(lines[0])):
            axes[axesIndex].plot([lines[0][i],ends[0][i]],[lines[1][i],ends[1][i]],'k')
        axes[axesIndex].plot([corners[0][1],corners[0][1]],[min(lines[1]+ends[1])-0.5,max(lines[1]+ends[1])+0.5],'k--')
        axes[axesIndex].text(ends[0][2]+0.1,ends[1][2]+0.1,"{} {}".format(round(sigmaP1,3),units),fontsize=12)
        axes[axesIndex].text(ends[0][3]+0.1,ends[1][3]+0.1,"{} {}".format(round(sigmaP2,3),units),fontsize=12)
        axes[axesIndex].set_xlim(min(lines[0]+ends[0])-0.5,max(lines[0]+ends[0])+2.25)
        axes[axesIndex].set_ylim(min(lines[1]+ends[1])-0.5,max(lines[1]+ends[1])+0.5)
        
        axesIndex+=1
    
    if 2 in show:
        corners = [[2,4,4,2],
                   [2,2,4,4]]
        lines = [[1.5,3.0,3.0,4.5,   0.00,3.00,3.00,6.00,   0.00,3.00,3.00,6.00,   1.75,2.00,4.25,2.00,   1.75,2.00,4.00,4.25,   4.25,1.75],
                 [3.0,1.5,4.5,3.0,   3.00,0.00,6.00,3.00,   3.00,0.00,6.00,3.00,   2.00,1.75,2.00,4.25,   4.00,4.25,1.75,2.00,   1.75,4.25]]
        ends =  [[0.0,3.0,3.0,6.0,   0.25,3.25,3.25,5.75,   0.25,2.75,2.75,5.75,   1.75,4.00,4.25,4.00,   1.50,2.25,3.75,4.50,   4.25,1.75],
                 [3.0,0.0,6.0,3.0,   3.25,0.25,5.75,3.25,   2.75,0.25,5.75,2.75,   4.00,1.75,4.00,4.25,   3.75,4.50,1.50,2.25,   1.75,4.25]]
        R = [[math.cos(phi),-math.sin(phi)],
             [math.sin(phi),math.cos(phi)]]
        corners = [list(line) for line in np.matmul(np.array(R),np.array(corners))]
        lines = [list(line) for line in np.matmul(np.array(R),np.array(lines))]
        ends = [list(line) for line in np.matmul(np.array(R),np.array(ends))]
        corners[0].append(corners[0][0])
        corners[1].append(corners[1][0])
        axes[axesIndex].plot(corners[0],corners[1])
        for i in range(len(lines[0])):
            axes[axesIndex].plot([lines[0][i],ends[0][i]],[lines[1][i],ends[1][i]],'k')
        axes[axesIndex].plot([corners[0][1],corners[0][1]],[min(lines[1]+ends[1])-0.5,max(lines[1]+ends[1])+0.5],'k--')
        axes[axesIndex].text(ends[0][2]+0.1,ends[1][2]+0.1,"{} {}".format(round(center,3),units),fontsize=12)
        axes[axesIndex].text(ends[0][3]+0.1,ends[1][3]+0.1,"{} {}".format(round(center,3),units),fontsize=12)
        axes[axesIndex].text(ends[0][-1]-2.5,lines[1][-1]-0.1,"{} {}".format(round(radius,3),units),fontsize=12)
        axes[axesIndex].text(ends[0][-2]+0.1,lines[1][-2]-0.1,"{} {}".format(round(radius,3),units),fontsize=12)
        axes[axesIndex].set_xlim(min(lines[0]+ends[0])-1.5,max(lines[0]+ends[0])+2.25)
        axes[axesIndex].set_ylim(min(lines[1]+ends[1])-0.5,max(lines[1]+ends[1])+0.5)
        
        axesIndex+=1
    
    if 3 in show:
        corners = [[2,4,4,2],
                   [2,2,4,4]]
        lines = [[1.5,3.0,3.0,4.5,   0.00,3.00,3.00,6.00,   0.00,3.00,3.00,6.00,   1.75,2.00,4.25,2.00,   1.75,2.00,4.00,4.25,   4.25,1.75],
                 [3.0,1.5,4.5,3.0,   3.00,0.00,6.00,3.00,   3.00,0.00,6.00,3.00,   2.00,1.75,2.00,4.25,   4.00,4.25,1.75,2.00,   1.75,4.25]]
        ends =  [[0.0,3.0,3.0,6.0,   0.25,3.25,3.25,5.75,   0.25,2.75,2.75,5.75,   1.75,4.00,4.25,4.00,   1.50,2.25,3.75,4.50,   4.25,1.75],
                 [3.0,0.0,6.0,3.0,   3.25,0.25,5.75,3.25,   2.75,0.25,5.75,2.75,   4.00,1.75,4.00,4.25,   3.75,4.50,1.50,2.25,   1.75,4.25]]
        R = [[math.cos(alpha),-math.sin(alpha)],
             [math.sin(alpha),math.cos(alpha)]]
        corners = [list(line) for line in np.matmul(np.array(R),np.array(corners))]
        lines = [list(line) for line in np.matmul(np.array(R),np.array(lines))]
        ends = [list(line) for line in np.matmul(np.array(R),np.array(ends))]
        corners[0].append(corners[0][0])
        corners[1].append(corners[1][0])
        axes[axesIndex].plot(corners[0],corners[1])
        for i in range(len(lines[0])):
            axes[axesIndex].plot([lines[0][i],ends[0][i]],[lines[1][i],ends[1][i]],'k')
        axes[axesIndex].plot([corners[0][1],corners[0][1]],[min(lines[1]+ends[1])-0.5,max(lines[1]+ends[1])+0.5],'k--')
        axes[axesIndex].text(ends[0][2]+0.1,ends[1][2]+0.1,"{} {}".format(round(sigma1,3),units),fontsize=12)
        axes[axesIndex].text(ends[0][3]+0.1,ends[1][3]+0.1,"{} {}".format(round(sigma2,3),units),fontsize=12)
        axes[axesIndex].text(ends[0][-2]+0.1,lines[1][-2]-0.1,"{} {}".format(round(tau1,3),units),fontsize=12)
        axes[axesIndex].set_xlim(min(lines[0]+ends[0])-1.5,max(lines[0]+ends[0])+2.25)
        axes[axesIndex].set_ylim(min(lines[1]+ends[1])-0.5,max(lines[1]+ends[1])+0.5)
    
    fig.set_figheight(4)
    fig.set_figwidth(4*len(axes))
    fig.tight_layout()
    
    fig.savefig(filename+'.png')

def generateMohrsCircle(sigmaXX,sigmaYY,tauXY,filename,thetaCutPlane=None,show=[0]):
    # Arguments: sigmaXX - the normal stress acting on the right face
    #            sigmaYY - the normal stress acting on the top face
    #            tau XY  - the shear stress acting on the unit
    #            filename - name to save file as for HW formatting; do not include file extension; disregard
    #            thetaCutPlane - angle of the cut plane in degrees; OPTIONAL - default is no angle
    #            show - the figures to show; OPTIONAL - default is Mohr's Circle only
    
    # Calculate values necessary for constructing Mohr's Circle
    center = (sigmaXX+sigmaYY)/2
    radius = math.hypot(sigmaYY-center,tauXY)
    sigmaP1,sigmaP2 = center-radius,center+radius
    thetaP1 = 1/2*math.asin(tauXY/radius)
    thetaP2 = thetaP1+math.pi
    
    # Calculate angle necessary for maximum in-plane shear stress
    phi = math.pi/4 + thetaP1
    
    # Calculate values necessary for a cut plane if angle for said plane is provided
    alpha,sigma1,sigma2,tau1=None,None,None,None
    if thetaCutPlane != None:
        alpha = -(2*math.radians(thetaCutPlane)+2*thetaP1)
        sigma1 = center + radius*math.cos(alpha)
        sigma2 = center - radius*math.cos(alpha)
        tau1 = radius*math.sin(alpha)
    
    # A function designed to draw the figures. Workings are irrelevant to actual assignment
    plotMohrsCircle(filename,sigmaYY,sigmaXX,tauXY,center,radius,sigmaP1,sigmaP2,thetaP1,phi,alpha,sigma1,sigma2,tau1,thetaCutPlane,show)
    
    # Constructing an object to return. You can ignore this as well
    keys = ['center','radius','sigmaP1','sigmaP2','thetaP1','phi']
    values = [center,radius,sigmaP1,sigmaP2,math.degrees(thetaP1),math.degrees(phi)]
    if thetaCutPlane != None:
        keys = keys + ['alpha','sigma1','sigma2','tau1']
        values = values + [math.degrees(alpha),sigma1,sigma2,tau1]
    meDict = dict(zip(keys,values))
    
    return meDict
