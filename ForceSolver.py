# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 15:59:58 2019

@author: tomhu
"""

import numpy as np
#from Input import *
import math as m
import matplotlib.pyplot as plt

Ca = 0.605                 #m chord length
l = 2.661                 #m span
x1 = 0.172                #m x-location hinge 1
x2 = 1.211                 #m x-location hinge 2
x3 = 2.591                 #m x-location hinge 3 
xa = 0.35                  #m distance between actuator 1 & 2
h  = 0.205               #m aileron height
d1 = 0.0454            #m vertical displacement hinge 1
d3 = 0.0724         #m vertical displacement hinge 3
theta=m.radians(28.0)       #deg max upward deflection
P  = -97400.0               #N load actuator 2
q  = -5540.0                #N/m aerodynamic load 
E  = 73.1*10**9             #Pa E-modulus
Izz = 1.0121766965*10**-5  #m^4 moment of inertia z
Iyy = 7.34770871618*10**-5    #m^4 moment of inertia y 
zsc = -0.121
ysc = 0.0
G = 28. * ( 10. ** 9. )
J = 7.046*10**-5  

n =1000 #number of elements

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
              [d1*E*Izz + q*x1**4/24],
              [q*x2**4/24],
              [d3*E*Izz+q*x3**4/24],
              [0],
              [0],
              [P/6*(x3-(x2+xa/2))**3]])

A = inv(M) * R
Vz = np.zeros((n,1))
Vy = np.zeros((n,1))
My = np.zeros((n,1))
Mz = np.zeros((n,1))
Tx = np.zeros((n,1))
twist = np.zeros((n,1))
xlist =[]
#conv  = np.matrix([[m.cos(theta),m.sin(theta),0,0,0,0,0,0,0,0,0,0],
#                    [-1*m.sin(theta),m.cos(theta),0,0,0,0,0,0,0,0,0,0],
#                    [0,0,1,0,0,0,0,0,0,0,0,0],
#                    [0,0,0,m.cos(theta),m.sin(theta),0,0,0,0,0,0,0],
#                    [0,0,0,-1*m.sin(theta),m.cos(theta),0,0,0,0,0,0,0],
#                    [0,0,0,0,0,m.cos(theta),m.sin(theta),0,0,0,0,0],
#                    [0,0,0,0,0,-1*m.sin(theta),m.cos(theta),0,0,0,0,0],
#                    [0,0,0,0,0,0,0,m.sin(theta),0,0,0,0],
#                    [0,0,0,0,0,0,0,m.cos(theta),0,0,0,0]])

#A[3] = -A[3]
#A[7] = -A[7]
#A[5] = -A[5]
#A[4] = -A[4]
Aprime =   A
csz= m.cos(theta)*zsc
csy= -m.sin(theta)*zsc 


for i in range(len(Vz)):
    x = l * i / len(Vz)
    if  0 < x  and x < x1 : 
        Vz[i] = 0
        Vy[i] = -q*x
        Tx[i] = -q*x*m.cos(theta)*(zsc+0.25*Ca-h/2)
        twist[i] = (m.cos(theta)*(zsc+0.25*Ca*h/2))/G/J
    elif x1 <= x and x < x2 -xa/2 :
        Vz[i] = Aprime[1]
        Vy[i] = Aprime[0] - q*x
        Tx[i] = -q*x*m.cos(theta)*(zsc+0.25*Ca-h/2)\
        +((zsc*m.sin(theta)+d1)*Aprime[1]+m.cos(theta)*zsc*Aprime[0]*zsc)
        twist[i] = (m.cos(theta)*(zsc+0.25*Ca*h/2)\
             +((m.sin(theta)*zsc+d1)*Aprime[1]\
               +m.cos(theta)*zsc**2*Aprime[0])*(x-x1))/G/J
        
    elif x >= x2 -xa/2 and x < x2 :
        Vz[i] = Aprime[1] + Aprime[7]
        Vy[i] = Aprime[0] -q*x
        Tx[i] = -q*x*m.cos(theta)*(zsc+0.25*Ca-h/2)\
        +((zsc*m.sin(theta)+d1)*Aprime[1]+m.cos(theta)*zsc*Aprime[0]*zsc)\
        +Aprime[7]*(h/2*(m.cos(theta)*m.sin(theta))+zsc*m.sin(theta))
        twist[i] = (m.cos(theta)*(zsc+0.25*Ca*h/2)\
             +((m.sin(theta)*zsc+d1)*Aprime[1]\
               +m.cos(theta)*zsc**2*Aprime[0])*(x-x1)\
               +Aprime[7]*(h/2*(m.cos(theta)*m.sin(theta))+zsc*m.sin(theta))*(x-(x2-xa/2)))/G/J
             
    elif x >= x2 and x < x2 + xa/2 :
        Vy[i] = Aprime[0] + Aprime[3]- q*x
        Vz[i] = Aprime[1] + Aprime[7] + Aprime[4] 
        Tx[i] = -q*x*m.cos(theta)*(zsc+0.25*Ca-h/2)\
        +((zsc*m.sin(theta)+d1)*Aprime[1]+m.cos(theta)*zsc*Aprime[0]*zsc)\
        +Aprime[7]*(h/2*(m.cos(theta)*m.sin(theta))+zsc*m.sin(theta))\
        +(m.sin(theta)*zsc*Aprime[4]+m.cos(theta)*Aprime[3]*zsc)
        twist[i] = (m.cos(theta)*(zsc+0.25*Ca*h/2)\
             +((m.sin(theta)*zsc+d1)*Aprime[1]\
               +m.cos(theta)*zsc**2*Aprime[0])*(x-x1)\
               +Aprime[7]*(h/2*(m.cos(theta)*m.sin(theta))+zsc*m.sin(theta))*(x-(x2-xa/2))\
               +(m.sin(theta)*zsc*Aprime[4]+m.cos(theta)*Aprime[3]*zsc)*(x-x2))/G/J
    elif x >= x2 + xa/2 and x < x3 :
        Vz[i] = Aprime[1] + Aprime[7] + Aprime[4] - P
        Vy[i] = Aprime[0] + Aprime[3]  - q*x
        Tx[i] = -q*x*m.cos(theta)*(zsc+0.25*Ca-h/2)\
        +((zsc*m.sin(theta)+d1)*Aprime[1]+m.cos(theta)*zsc*Aprime[0]*zsc)\
        +Aprime[7]*(h/2*(m.cos(theta)*m.sin(theta))+zsc*m.sin(theta))\
        +(m.sin(theta)*zsc*Aprime[4]+m.cos(theta)*Aprime[3]*zsc)\
        -P*(h/2*(m.cos(theta)-m.sin(theta))+m.sin(theta)*zsc)
        twist[i] = (m.cos(theta)*(zsc+0.25*Ca*h/2)\
             +((m.sin(theta)*zsc+d1)*Aprime[1]\
               +m.cos(theta)*zsc**2*Aprime[0])*(x-x1)\
               +Aprime[7]*(h/2*(m.cos(theta)*m.sin(theta))+zsc*m.sin(theta))*(x-(x2-xa/2))\
               +(m.sin(theta)*zsc*Aprime[4]+m.cos(theta)*Aprime[3]*zsc)*(x-x2)\
               -P*(h/2*(m.cos(theta)-m.sin(theta))+m.sin(theta)*zsc)*(x-x2-xa/2))/G/J
    elif x >= x3 and x < l:
        Vz[i] = Aprime[1] + Aprime[7] + Aprime[4] - P + Aprime[6]
        Vy[i] = Aprime[0] + Aprime[3] + Aprime[5] - q*x
        Tx[i] = -q*x*m.cos(theta)*(zsc+0.25*Ca-h/2)\
        +((zsc*m.sin(theta)+d1)*Aprime[1]+m.cos(theta)*zsc*Aprime[0]*zsc)\
        +Aprime[7]*(h/2*(m.cos(theta)*m.sin(theta))+zsc*m.sin(theta))\
        +(m.sin(theta)*zsc*Aprime[4]+m.cos(theta)*Aprime[3]*zsc)\
        -P*(h/2*(m.cos(theta)-m.sin(theta))+m.sin(theta)*zsc)\
        +((zsc*m.sin(theta)+d3)*Aprime[6]+m.cos(theta)*zsc*Aprime[5]*zsc)
        twist[i] = (m.cos(theta)*(zsc+0.25*Ca*h/2)\
             +((m.sin(theta)*zsc+d1)*Aprime[1]\
               +m.cos(theta)*zsc**2*Aprime[0])*(x-x1)\
               +Aprime[7]*(h/2*(m.cos(theta)*m.sin(theta))+zsc*m.sin(theta))*(x-(x2-xa/2))\
               +(m.sin(theta)*zsc*Aprime[4]+m.cos(theta)*Aprime[3]*zsc)*(x-x2)\
               -P*(h/2*(m.cos(theta)-m.sin(theta))+m.sin(theta)*zsc)*(x-x2-xa/2)\
               +((zsc*m.sin(theta)+d3)*Aprime[6]+m.cos(theta)*zsc*Aprime[5]*zsc)*(x-x3))/G/J
        
    
    
    Vy[i] = Vy[i]*m.cos(theta) + Vz[i]*m.sin(theta)
    Vz[i] = Vz[i]*m.cos(theta) - Vy[i] *m.sin(theta)  
    My[i] = My[i-1]  - Vz[i-1] * l * 1 / len(Vz)
    Mz[i] = Mz[i-1]  - Vy[i-1] * l * 1 / len(Vz)
    xlist.append(x) 

#plt.figure(1)
#plt.plot(xlist, Vz)
#plt.xlabel("x")
#plt.ylabel("Vz'")
#plt.grid()
#plt.show()
#plt.figure(2)
#plt.plot(xlist, Vy)
#plt.xlabel("x")
#plt.ylabel("Vy'")
#plt.grid()
#plt.show()
#plt.figure(3)
#plt.plot(xlist, My)
#plt.xlabel("x")
#plt.ylabel("My'")
#plt.grid()
#plt.show()
#plt.figure(4)
#plt.plot(xlist, Mz)
#plt.xlabel("x")
#plt.ylabel("Mz'")
#plt.grid()
#plt.show()
plt.figure(5)
plt.plot(xlist, Tx* -1)
plt.xlabel("x")
plt.ylabel("Tx")
plt.grid()
plt.show()
plt.figure(6)
plt.plot(xlist, twist)
plt.xlabel("x")
plt.ylabel("Theta")
plt.grid()
plt.show()

