# main file
import numpy as np
from math import *
import matplotlib.pyplot as plt
from definitionboomarea import Boomarea
from SVV import skin_init
from cog import center_gravity, I_yy, I_zz, I_zznon, ideal_cog
parameters = dict()

c = 0.505                   #m, chord lenght
l = 1.611                   #m, span
x_1 = 0.125                 #m, x location of hinge 1
x_2 = 0.498                 #m, x location of hinge 2
x_3 = 1.494                 #m, x location of hinge 3
x_a = 24.5/100.             #cm, distance between actuator 1 and 2
h = 16.1/100.               #cm, height of aileron
t_skin = 1.1/1000.          #mm, thickness
t_spar = 2.4/1000.          #mm, thickness
t_stiffener = 1.2/1000.     #mm, thickness
h_stiffener = 1.3/100.      #cm, height
w_stiffener = 1.7/100.      #cm, width of stiffener
n_stiffener = 11            #number of stiffeners
d_1 = 0.389/100.            #cm, displacement hinge 1
d_3 = 1.245/100.            #cm, displacement hinge 3
theta = 30.                 #degrees, max upward deflection
P_2 = 49.2*1000             #kN, load actuator 2
q = 3.86*1000               #kN/m, aerodynamic load

skin_length = np.sqrt( (c-h*0.5)**2 + (0.5*h)**2) #length of upper or lower angled part of skin in meters
A_stiffener = t_stiffener * (h_stiffener + w_stiffener)

element_locations = skin_init(c,h,n_stiffener)
center_gravity(c, h, l, t_skin, t_spar, A_stiffener, n_stiffener,element_locations, parameters)
I_zznon(element_locations['y_stiffeners'],t_spar,h,c, t_skin,skin_length, A_stiffener, parameters)
Boomarea(element_locations['z_booms'],element_locations['y_booms'],A_stiffener,element_locations['s_booms'],t_skin,t_spar,h, parameters)
ideal_cog(element_locations, parameters)
I_yy(element_locations['z_booms'], parameters)
I_zz(element_locations['y_booms'], parameters)


























#zprime = z coordinate of boom
#zcg = center of gravity in z direction
#sparlength = h
#Abooms = Boomarea(zprime,yprime,A_stiff,cg_z,t_skin,t_spar,h)
#output not completely defined yet

#def SkinPerimeter(slist,d):
#    
#    zcoord=np.array([])
#    ycoord=np.array([])
#    
#    for s in slist:
#        
#        if s < d :
#             z = (c - h / 2) / d * s
#             y = h / 2 / d * s
#            
#        elif s < d + np.pi * h / 2:
#            beta = (s - d) / (h / 2)
#            z = (c - h / 2) + (h / 2) * np.sin(beta)
#            y = (h / 2) * np.cos(beta)
#            
#        elif s < d * 2 + np.pi * h / 2 :
#            z =  (c - h / 2) - (c - h / 2) / d * (s - d - np.pi * h / 2)
#            y = -h / 2 + (h / 2) / d * (s - d - np.pi * h / 2)
#            
#            zcoord = np.append(zcoord , z)
#            ycoord = np.append(ycoord , y)
#    
#    return zcoord, ycoord
#
#            
#def SkinPerimeterInit():
#    nst = n_stiffener
#    d = np.sqrt(((h/2)**2 + c - h/2)**2)
#    circumference = np.pi * h / 2 + 2 * d
#    spacing_st = circumference / (nst + 2)
#    s_stiffeners = np. linspace (0, circumference , nst + 2) [: -1][1:]
#    s_sparcaps = np.array ([d, d + np.pi * h / 2])
#    s_booms = np.sort(np.append(s_stiffeners , s_sparcaps ))
#    s_skin = np. linspace (0, circumference , 1000)
#    
#    z_stiffeners , y_stiffeners = SkinPerimeter ( s_stiffeners,d )
#    z_sparcaps , y_sparcaps = SkinPerimeter ( s_sparcaps,d )
#    z_booms , y_booms = SkinPerimeter (s_booms,d)
#    z_skin , y_skin = SkinPerimeter (s_skin,d)
