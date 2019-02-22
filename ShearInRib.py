# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:43:48 2019

@author: tomhu
"""
import numpy as np
#from ForceSolver import Vy, Vz, Tx
def RibShear(Vy,Vz,T,C,h):
    rib1=np.matrix([[-h/2,-h/2,h],
                [(C-h/2),-(C-h/2),0],
                [0,0,2*h*(C-h/2)]])
    res = np.matrix([[Vy],
                 [Vz],
                 [Vy*(C-h/2)+T]])
    B = rib1.I * res
    #print(A)
    Px1=(2*h/2/2*(C-h/2)*B[0])/h
    Px3=(2*h/2/2*(C-h/2)*B[1])/h
    
    Py1 = Px1 * h/2/(C-h/2)
    Py3 = Px3 * h/2/(C-h/2)
    
    q = (B[0]*h/2+B[1]*h/2-Py1-Py3)/h
    print(q)
    return q



C=1.611*10**3
h=0.161*10**3
Vy = np.ones((1000,1))
Vz = np.ones((1000,1))
Tx = np.ones((1000,1))
n=1000
xpos = [int(78/1000*n),int(233/1000*n),int(309/1000*n),int(385/1000*n),int(927/1000*n)]
ribflow=[]
for i in xpos:
    Rib=RibShear(Vy[i],Vz[i],Tx[i],C,h)
    ribflow.append(Rib)
