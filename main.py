# main file
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from definitionboomarea import Boomarea
from SVV import skin_init
from cog import center_gravity, I_yy, I_zz, I_zznon, ideal_cog
from ForceSolver import force_solver

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


parameters['skin_length'] = 0.43206538856983207

element_locations = skin_init()

#plt.figure(1)
#plt.plot(element_locations['z_stiffeners'], element_locations['y_stiffeners'])
#plt.plot(element_locations['z_booms'], element_locations['y_booms'])

#testing part of the code

center_gravity(element_locations, parameters)
if round(parameters['cog_z']/ -0.13361282329336502 , 8) != 1:
    print ('center of gravity calculation is incorrect')

I_zznon(parameters, element_locations['y_stiffeners']) #should calculate by hand




Boomarea(parameters)
correctans_y = 0.00013819538452374162
correctans_z = 0.00013819538541666665
if round(parameters['Aboomsy'][1]/correctans_y, 8)!= 1 or round(parameters['Aboomsz'][1]/correctans_z, 8)!= 1:
    print('boom area calculation, or previous calculation incorrect')
    print(parameters['Aboomsy'][1], "in y",parameters['Aboomsz'][1] , " in z, are the answers you get")  






#actual calculations
element_locations = skin_init(c,h,n_stiffener)

parameters['skin_length'] = np.sqrt( (c-h*0.5)**2 + (0.5*h)**2) #length of upper or lower angled part of skin in meters, checked

A_stiffener = t_stiffener * (h_stiffener + w_stiffener)

center_gravity(element_locations, parameters, c, h, l, t_skin, t_spar, A_stiffener, n_stiffener)

I_zznon(parameters, element_locations['y_stiffeners'],t_spar,h,c, t_skin, A_stiffener)

Boomarea(parameters,element_locations['z_booms'],element_locations['y_booms'],A_stiffener,element_locations['s_booms'],t_skin,t_spar,h)

ideal_cog(element_locations, parameters)
I_yy(element_locations['z_booms'], parameters)
I_zz(element_locations['y_booms'], parameters)

force_solver(parameters)























