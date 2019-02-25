# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:43:48 2019

@author: tomhu
"""
import numpy as np
import math as m
#from ForceSolver import Vy, Vz, Tx
def RibShearHinge(Ry,Rz,C,h):
    Ry = float(Ry)
    Rz=float(Rz)
    rib1=np.matrix([[-h,h/2,h/2,],
                [0,-(C-h/2),(C-h/2)],
                [m.pi*h**2/4,h/2*(C-h/2),h/2*(C-h/2)]])
    res = np.matrix([[Ry],
                 [Rz],
                 [-Ry*(C-h/2)]])
    B = rib1.I * res
    shear1 = (-B[0]*h-2*(m.pi*h**2/4/2)*-B[0]*h/2/(C-h/2)) / h
    shear2 = (shear1*h+Ry)/h
    return shear1, shear2

def RibShearActuator(Ry,Rz,C,h):
    Ry = float(Ry)
    Rz=float(Rz)
    rib1=np.matrix([[-h/2,-h/2,h],
                [(C-h/2),-(C-h/2),0],
                [0,0,2*h*(C-h/2)]])
    res = np.matrix([[Ry],
                 [Rz],
                 [Ry*(C)-Rz*h/2]])
    B= rib1.I * res
    shear1 = (-B[0]*h-2*(m.pi*h**2/4/2)*-B[0]*h/2/(C-h/2)) / h
    shear2 = (shear1*h+Ry)/h
    return shear1,shear2


C=1.611*10**3
h=0.161*10**3
theta = m.radians(25.)
P  = -20600.0 
A=np.matrix([[ 6.56326488e+04],
 [-2.99280085e+04],
 [ 0.00000000e+00],
 [-9.32054504e+04],
 [ 2.73538743e+04],
 [ 3.23659761e+04],
 [-1.56076390e+03],
 [ 5.03843396e+04],
 [-4.55168632e+03],
 [ 1.70401690e+03],
 [ 6.39377657e+02],
 [-7.99398950e+01]])
n=1000
#xpos = [int(78/1000*n),int(233/1000*n),int(309/1000*n),int(385/1000*n),int(927/1000*n)]
ribflow=[]
#hinge 1
Ry=A[0]
Rz=A[1]
Rib = RibShearHinge(Ry, Rz, C, h)
ribflow.append(Rib)
#at F
Rz = A[7] * m.cos(theta)
Ry = A[7] * m.sin(theta)
Rib = RibShearActuator(Ry,Rz,C,h)
ribflow.append(Rib)

#hinge 2
Ry=A[3]
Rz=A[4]
Rib = RibShearHinge(Ry, Rz, C, h)
ribflow.append(Rib)


#at P 
Rz = P * m.cos(theta)
Ry = P * m.sin(theta)
Rib = RibShearActuator(Ry,Rz,C,h)
ribflow.append(Rib)
#hinge 3
Ry=A[5]
Rz=A[6]
Rib = RibShearHinge(Ry, Rz, C, h)
ribflow.append(Rib)

print(ribflow)
