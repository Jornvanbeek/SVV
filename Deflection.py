# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:05:36 2019

@author: tomhu
"""
import math as m
import numpy as np
import matplotlib.pyplot as plt
import ForceSolver



x=np.linspace(0,l,n)

deltay = 1/E/Izz*(- m.cos(theta)*q*x**4/24+np.multiply(np.power(x-x1,3),np.heaviside(x-x1,0)*float(A[0])/6)\
         +np.multiply(np.power(x-x2,3),np.heaviside(x-x2,0)*float(A[3])/6)\
         +np.multiply(np.power(x-x2+xa/2,3),np.heaviside(x-x2+xa/2,0)*float(A[7])*m.sin(theta)/6)\
         +np.multiply(np.power(x-x3,3),np.heaviside(x-x3,0)*float(A[5])/6)\
         -np.multiply(np.power(x-x2-xa/2,3),np.heaviside(x-x2-xa/2,0)*float(P)*m.sin(theta)/6)\
         +A[8]*x+A[9])
         
deltaz = 1/E/Iyy*(m.sin(theta)*q*x**4/24+np.multiply(np.power(x-x1,3),np.heaviside(x-x1,0)*float(A[1])/6)\
         +np.multiply(np.power(x-x2,3),np.heaviside(x-x2,0)*float(A[4])/6)\
         +np.multiply(np.power(x-x2+xa/2,3),np.heaviside(x-x2+xa/2,0)*float(A[7])*m.cos(theta)/6)\
         +np.multiply(np.power(x-x3,3),np.heaviside(x-x3,0)*float(A[6])/6)\
         -np.multiply(np.power(x-x2-xa/2,3),np.heaviside(x-x2-xa/2,0)*float(P)*m.cos(theta)/6)\
         +A[10]*x+A[11])
dyTE = deltay.T + m.sin(theta)*(Ca-h/2) + np.sin(twist)*(Ca-h/2-zsc)
dyLE = deltay.T - m.sin(theta)*h/2- np.sin(twist)*(h/2-zsc)
dzTE = deltay.T + m.cos(theta)*(Ca-h/2) + (np.sin(twist)-np.ones(twist.shape))*(Ca-h/2-zsc)
dzLE = deltay.T - m.cos(theta)*h/2- (np.cos(twist)-np.ones(twist.shape))*(h/2-zsc)

#plt.figure(4)
#plt.plot(x,deltay.T-0.01245)
#plt.plot(x,deltaz.T)
#plt.show()


#plt.figure(1)
#plt.plot(x,dyLE)
#plt.plot(x,dyTE)
#plt.show()
#plt.figure(2)
#plt.plot(x,dzTE)
#plt.plot(x,dzLE)
#plt.show()