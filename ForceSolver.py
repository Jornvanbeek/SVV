# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:59:58 2019

@author: tomhu
"""

import numpy as np
#from Input import *
import math as m

Ca = 0.505                  #m chord length
l = 1.611                 #m span
x1 = 0.125                 #m x-location hinge 1
x2 = 0.498                 #m x-location hinge 2
x3 = 1.494                  #m x-location hinge 3 
xa = 0.245                  #m distance between actuator 1 & 2
h  = 0.161               #m aileron height
d1 = 0.00389            #m vertical displacement hinge 1
d3 = 0.01245         #m vertical displacement hinge 3
theta=m.radians(30.0)       #deg max upward deflection
P  = -49200.0               #N load actuator 2
q  = -3860.0                #N/m aerodynamic load 
E  = 73.1*10**9             #Pa E-modulus
Izz = 1.0121766965*10**-5  #m^4 moment of inertia z
Iyy = 7.34770871618*10**-5    #m^4 moment of inertia y 
zsc = -0.121
ysc = 0.0
G = 28. * ( 10. ** 9. )
J = 7.046*10**-5  

M = np.matrix([[0,0,1,0,0,0,0,0,0,0,0,0],
              [1,0,0,1,0,1,0,0,0,0,0,0],
              [0,1,0,0,1,0,1,1,0,0,0,0],
              [x2-x1,0,0,0,0,-(x3-x2),0,0,0,0,0,0],
              [0,x2-x1,0,0,0,0,-(x3-x2),xa/2,0,0,0,0],
              [0,d1,0,0,0,0,d3,h/2*(m.cos(theta)-m.sin(theta)),0,0,0,0],
              [0,0,0,0,0,0,0,0,x1,1,0,0],
              [1/6*(x2-x1)**3,0,0,0,0,0,0,0,x2,1,0,0],
              [1/6*(x3-x1)**3,0,0,1/6*(x3-x2)**3,0,0,0,0,x3,1,0,0],
              [0,0,0,0,0,0,0,0,0,0,x1,1],
              [0,1/6*(x2-x1)**3,0,0,0,0,0,1/6*(xa/2)**3,0,0,x2,1],
              [0,1/6*(x3-x1)**3,0,0,1/6*(x3-x2)**3,0,0,1/6*(x3-(x2-xa/2))**3,0,0,x3,1]])

R = np.matrix([[0],
              [q*l],
              [P],
              [-q*l*(l/2-x2)],
              [-P*xa/2],
              [P*h/2*(m.cos(theta)-m.sin(theta))+q*l*(0.25*Ca)*m.cos(theta)],
              [d1*E*Izz+q*x1**4/24],
              [q*x2**4/24],
              [d3*E*Izz+q*x3**4/24],
              [0],
              [0],
              [0]])

A = inv(M) * R