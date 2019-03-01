import math as m
import numpy as np
import matplotlib.pyplot as plt
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
    theta = m.radians(theta)


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

    dyTE = deltay + np.sin(twist.T)*(Ca-h/2+zsc) #+ m.sin(theta)*(Ca-h/2)*np.ones(twist.T.shape) 
    dyLE = deltay - np.sin(twist.T)*(h/2-zsc)#- m.sin(theta)*h/2*np.ones(twist.T.shape)
    dzTE = deltaz + (np.cos(twist.T)-np.ones(twist.T.shape))*(Ca-h/2+zsc)#- m.cos(theta)*(Ca-h/2)*np.ones(twist.T.shape) 
    dzLE = deltaz - (np.cos(twist.T)-np.ones(twist.T.shape))*(h/2-zsc)#+ m.cos(theta)*h/2*np.ones(twist.T.shape)
    
    return dyTE,dyLE,dzTE,dzLE,x
    
    
