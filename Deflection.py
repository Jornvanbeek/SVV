# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 14:05:36 2019

@author: tomhu
"""
import math as m
import numpy as np
import matplotlib.pyplot as plt
import ForceSolver
def deflection(parameters):
    l = parameters['l']
    n = parameters['n']
    E = parameters['E']
    theta = parameters['theta']
    Izz = parameters['Izz']
    Iyy = parameters['Iyy']

    q = parameters['q']
    P = parameters['P_2']
    x1 = parameters['x_1']
    A = parameters['A']
    x2 = parameters['x_2']
    xa = parameters['x_a']
    x3 = parameters['x_3']
    zsc = parameters['zsc']
    Ca = parameters['c']
    h = parameters['h']
    twist = parameters['twist']
    Izz = 4.609*10**-6  #m^4 moment of inertia z
    Iyy = 7.797*10**-5    #m^4 moment of inertia y 




    

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
#    print(twist.shape)
    dyTE = deltay + m.sin(theta)*(Ca-h/2)*np.ones(twist.T.shape) + np.sin(twist.T)*(Ca-h/2-zsc)
    dyLE = deltay - m.sin(theta)*h/2*np.ones(twist.T.shape)- np.sin(twist.T)*(h/2-zsc)
    dzTE = deltaz + m.cos(theta)*(Ca-h/2)*np.ones(twist.T.shape) + (np.sin(twist.T)-np.ones(twist.T.shape))*(Ca-h/2-zsc)
    dzLE = deltaz - m.cos(theta)*h/2*np.ones(twist.T.shape)- (np.cos(twist.T)-np.ones(twist.T.shape))*(h/2-zsc)
    
#    plt.figure(4)
#    plt.plot(x,twist)
#    plt.plot(x,deltaz.T)
#    plt.show()
    return dyTE,dyLE,dzTE,dzLE,x
    
    
    
    #plt.figure(1)
    #plt.plot(x,dyLE)
    #plt.plot(x,dyTE)
    #plt.show()
    #plt.figure(2)
    #plt.plot(x,dzTE)
    #plt.plot(x,dzLE)
    #plt.show()