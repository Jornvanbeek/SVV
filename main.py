# main file
import numpy as np
import matplotlib.pyplot as plt
from math import pi
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

parameters['skin_length'] = np.sqrt( (c-h*0.5)**2 + (0.5*h)**2) #length of upper or lower angled part of skin in meters, checked
A_stiffener = t_stiffener * (h_stiffener + w_stiffener)


element_locations = skin_init(c,h,n_stiffener)

center_gravity(c, h, l, t_skin, t_spar, A_stiffener, n_stiffener,element_locations, parameters)
I_zznon(element_locations['y_stiffeners'],t_spar,h,c, t_skin,parameters['skin_length'], A_stiffener, parameters)

Boomarea(element_locations['z_booms'],element_locations['y_booms'],A_stiffener,element_locations['s_booms'],t_skin,t_spar,h, parameters)

ideal_cog(element_locations, parameters)
I_yy(element_locations['z_booms'], parameters)
#assertEqual(I_zz(), 10)
I_zz(element_locations['y_booms'], parameters)


























