# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:59:58 2019

@author: tomhu
"""

import numpy as np
#from Input import *
import math as m
import matplotlib.pyplot as plt

Ca = 0.505                 #m chord length
l = 1.611                 #m span
x1 = 0.125            #m x-location hinge 1
x2 = 0.498                #m x-location hinge 2
x3 = 1.494                #m x-location hinge 3 
xa = 0.245                 #m distance between actuator 1 & 2
h  = 0.161               #m aileron height
d1 = 0.00389          #m vertical displacement hinge 1
d3 = 0.01245         #m vertical displacement hinge 3
theta=m.radians(30.0)       #deg max upward deflection
P  = 49200.0               #N load actuator 2
q  = 3860.0                #N/m aerodynamic load 
E  = 73.1*10**9             #Pa E-modulus
 

zsc = -0.0229
ysc = 0.0
G = 28. * ( 10. ** 9. )
J = 7.268*10**-6 


def force_solver(parameters, n = 1000, Ca = Ca, l = l, x1 = x1, x2 = x2, x3 = x3, xa = xa, h = h, d1 = d1, d3 = d3, theta = theta, P = P, q = q, E = E, zsc = zsc,ysc = ysc, G = G, J = J ):
    n = parameters['n']
    Izz = parameters['Izz']
    Iyy = parameters['Iyy']

    M = np.matrix([[0,0,1,0,0,0,0,0,0,0,0,0],               #Fx
              [1,0,0,1,0,1,0,m.sin(theta),0,0,0,0],     #Fy
              [0,1,0,0,1,0,1,m.cos(theta),0,0,0,0],     #Fz
              [d1*m.sin(theta),d1*m.cos(theta),0,0,0,d3*m.sin(theta),\
               d3*m.cos(theta),(m.cos(theta)*h/2-m.sin(theta)*h/2),0,0,0,0],#Mx
              [0,(x2-x1),0,0,0,0,-(x3-x2),xa/2*m.cos(theta),0,0,0,0],       #My
              [-(x2-x1),0,0,0,0,(x3-x2),0,-xa/2*m.sin(theta),0,0,0,0],    #Mz
              [0,0,0,0,0,0,0,0,x1,1,0,0],                           #y at 1
              [1/6*(x2-x1)**3,0,0,0,0,0,0,m.sin(theta)*1/6*(xa/2)**3,x2,1,0,0],              #y at 2
              [1/6*(x3-x1)**3,0,0,1/6*(x3-x2)**3,0,0,0,m.sin(theta)*1/6*(x3-(x2-xa/2))**3,x3,1,0,0], #y at 3
              [0,0,0,0,0,0,0,0,0,0,x1,1],                           #z at 1
              [0,1/6*(x2-x1)**3,0,0,0,0,0,m.cos(theta)*1/6*(xa/2)**3,0,0,x2,1],  #z at 2
              [0,1/6*(x3-x1)**3,0,0,1/6*(x3-x2)**3,0,0,m.cos(theta)*1/6*(x3-(x2-xa/2))**3,0,0,x3,1]])#z at 3
    
    R = np.matrix([[0],                                     #Fx
              [P*m.sin(theta)+q*l*m.cos(theta)],        #Fy
              [P*m.cos(theta)-q*l*m.sin(theta)],        #Fz
              [P*m.cos(theta)*h/2-P*m.sin(theta)*h/2+q*l*m.cos(theta)*(0.25*Ca-h/2)], #Mx
              [-P*xa/2*m.cos(theta)+q*l*(l/2-x2)*m.sin(theta)],     #My
              [P*xa/2*m.sin(theta)+q*l*m.cos(theta)*(l/2-x2)],   #Mz
              [d1*m.cos(theta)*E*Izz +q*m.cos(theta)*x1**4/24], #y at 1
              [q*m.cos(theta)*x2**4/24],                             #y at 2
              [d3*m.cos(theta)*E*Izz+q*m.cos(theta)*x3**4/24+P*m.sin(theta)/6*(x3-(x2+xa/2))**3],        #y at 3
              [-d1*m.sin(theta)*E*Iyy-q*m.sin(theta)*x1**4/24],                    #z at 1
              [-q*m.sin(theta)*x2**4/24],                                  #z at 2
              [+P*m.cos(theta)/6*(x3-(x2+xa/2))**3-d3*m.sin(theta)*E*Iyy-q*m.sin(theta)*x3**4/24]])#z at 3
    
    A = M.I * R
    Vz = np.zeros((n,1))
    Vy = np.zeros((n,1))
    My = np.zeros((n,1))
    Mz = np.zeros((n,1))
    Tx = np.ones((n,1))
    twist = np.zeros((n,1))
    xlist =[]
    
    Aprime =   A
    
    Vz = np.zeros((n,1))
    Vy = np.zeros((n,1))
    My = np.zeros((n,1))
    Mz = np.zeros((n,1))
    Tx = np.zeros((n,1))
    twist = np.zeros((n,1))
    xlist =[]
    for i in range(len(Vz)):
        x = l * i / len(Vz)
    
        Vy[i] = Aprime[0]*np.heaviside(x-x1,0) \
        + Aprime[7]*m.sin(theta)*np.heaviside(x-x2+xa/2,0) \
        +Aprime[3]*np.heaviside(x-x2,0) \
        - P*m.sin(theta)*np.heaviside(x-x2-xa/2,0) \
        + Aprime[5]*np.heaviside(x-x3,0)\
        - q * x * m.cos(theta)
    
    
        Vz[i] = Aprime[1]*np.heaviside(x-x1,0) \
        + Aprime[7]*m.cos(theta)*np.heaviside(x-x2+xa/2,0) \
        +Aprime[4]*np.heaviside(x-x2,0) \
        - P*m.cos(theta)*np.heaviside(x-x2-xa/2,0) \
        + Aprime[6]*np.heaviside(x-x3,0)\
        + q * x * m.sin(theta)
    
    
        Tx[i] = -q*x*m.cos(theta)*(zsc+0.25*Ca-h/2)\
        +(Aprime[7]*m.cos(theta)*h/2-Aprime[7]*m.sin(theta)*(h/2-zsc))*np.heaviside(x-x2+xa/2,0)\
        -(P*m.cos(theta)*h/2-P*m.sin(theta)*(h/2-zsc))*np.heaviside(x-x2-xa/2,0)\
        +((d1*m.cos(theta))*Aprime[1]+(d1*m.sin(theta)+zsc)*Aprime[0])*np.heaviside(x-x1,0)\
        +(Aprime[3]*zsc)*np.heaviside(x-x2,0)\
        +((d3*m.cos(theta))*Aprime[6]+(d3*m.sin(theta)+zsc)*Aprime[5])*np.heaviside(x-x3,0)\
        
        if i >=1:
            twist[i] = twist[i-1] - Tx[i-1]/G/J * l * 1 / len(Vz)
#            
        My[i] = My[i-1]  + Vz[i-1] * l * 1 / len(Vz)
        Mz[i] = Mz[i-1]  + Vy[i-1] * l * 1 / len(Vz)
        xlist.append(x)
    f= twist[int(len(My)*0.375/l)]
    twist = twist - f
    
    parameters['Equations?'] = M
    parameters['Reaction_forces?'] = R
    parameters['Shear_z'] =Vz
    parameters['Shear_y'] =Vy
    parameters['Moment_y'] =My
    parameters['Moment_z'] =Mz
    parameters['Torque'] =Tx
    parameters['twist'] =twist
    parameters['spanwise_locations'] =xlist
    parameters['zsc'] = zsc
    parameters['P'] = P
    parameters['n'] = n
    parameters['A'] = A
    
