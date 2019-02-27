# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:43:48 2019

@author: tomhu
"""
import numpy as np
import math as m
import ForceSolver

def RibShearHinge(Ry,Rz):
    Ry = float(Ry)
    Rz=float(Rz)
    rib1=np.matrix([[-h,h/2,h/2,],
                [0,-(C-h/2),(C-h/2)],
                [m.pi*h**2/4,h/2*(C-h/2),h/2*(C-h/2)]])
    res = np.matrix([[Ry],
                 [Rz],
                 [-Ry*(C-h/2)]])
    B = rib1.I * res
    shear1 = -B[0] #(-B[0]*h-2*(m.pi*h**2/4/2)*-B[0]*h/2/(C-h/2)) / h
    shear2 = 0#(shear1*h+Ry)/h
    return shear1, shear2

def RibShearActuator(Ry,Rz):
    Ry = float(Ry)
    Rz=float(Rz)
    rib1=np.matrix([[-h/2,-h/2,h],
                [(C-h/2),-(C-h/2),0],
                [0,0,2*h*(C-h/2)]])
    res = np.matrix([[Ry],
                 [Rz],
                 [Ry*(C)-Rz*h/2]])
    B= rib1.I * res
    shear1 = -B[0] #(-B[0]*h-2*(m.pi*h**2/4/2)*-B[0]*h/2/(C-h/2)) / h
    shear2 = 0#(shear1*h+Ry)/h
    return shear1,shear2


def ribshear_init(parameters):
    global C
    global h
    C = parameters['c']
    h = parameters['h']
    #testparameters
    #theta = m.radians(25.)
    #P  = -20600.0 
    
#    #to be used parameters


    #xpos = [int(78/1000*n),int(233/1000*n),int(309/1000*n),int(385/1000*n),int(927/1000*n)]
    ribflow=[]
    #hinge 1
    Ry=A[0]
    Rz=A[1]
    Rib = RibShearHinge(Ry, Rz)
    ribflow.append(Rib)
    #at F
    Rz = A[7] * m.cos(theta)
    Ry = A[7] * m.sin(theta)
    Rib = RibShearActuator(Ry,Rz)
    ribflow.append(Rib)
    
    #hinge 2
    Ry=A[3]
    Rz=A[4]
    Rib = RibShearHinge(Ry, Rz)
    ribflow.append(Rib)
    
    
    #at P 
    Rz = P * m.cos(theta)
    Ry = P * m.sin(theta)
    Rib = RibShearActuator(Ry,Rz)
    ribflow.append(Rib)
    #hinge 3
    Ry=A[5]
    Rz=A[6]
    Rib = RibShearHinge(Ry, Rz)
    ribflow.append(Rib)
    parameters['ribflow'] = ribflow
    
#    print(ribflow)
