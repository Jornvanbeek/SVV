# main file
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from definitionboomarea import Boomarea
from SVV import skin_init
from cog import center_gravity, I_yy, I_zz, I_zznon, ideal_cog
from ForceSolver import force_solver
from Normalstrss import Normalstress
from plot import plot
from q_shear import qb_z, qb_y
from q_torque import qb_T
from ShearInRib import ribshear_init
from input_parameters import inputparameters

parameters = dict()
inputparameters(parameters)

c = parameters['c']
h = parameters['h']
l = parameters['l']
n_stiffener = parameters['n_stiffener']
t_stiffener = parameters['t_stiffener']
h_stiffener = parameters['h_stiffener']
w_stiffener = parameters['w_stiffener']
t_skin = parameters['t_skin']
t_spar = parameters['t_spar']
d_1 = parameters['d_1']
  


parameters['skin_length'] = 0.43206538856983207

element_locations = skin_init(parameters)

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
element_locations = skin_init(parameters)

parameters['skin_length'] = np.sqrt( (c-h*0.5)**2 + (0.5*h)**2) #length of upper or lower angled part of skin in meters, checked
parameters['A_cell1'] = np.pi*(h/2)**2/2 #inside de circular part
parameters['A_cell2'] = h*(c-h/2)/2 #inside the triangular part

A_stiffener = t_stiffener * (h_stiffener + w_stiffener)

center_gravity(element_locations, parameters, c, h, l, t_skin, t_spar, A_stiffener, n_stiffener)

I_zznon(parameters, element_locations['y_stiffeners'],t_spar,h,c, t_skin, A_stiffener)

Boomarea(parameters,element_locations['z_booms'],element_locations['y_booms'],A_stiffener,element_locations['s_booms'],t_skin,t_spar,h)

ideal_cog(element_locations, parameters)
I_yy(element_locations['z_booms'], parameters)
I_zz(element_locations['y_booms'], parameters)

force_solver(parameters)

Normalstress(parameters,element_locations)


qb_z(parameters,element_locations)
qb_y(parameters,element_locations)

q_spar_arr = np.zeros(1)
q_skin_arr = np.zeros(len(element_locations['s_booms']))
rot_arr = np.zeros(1)
for T in parameters['Torque']:
    q_spar_arr, q_skin_arr, rot_arr = qb_T(parameters, element_locations,T,q_spar_arr,q_skin_arr,rot_arr)

parameters['q_spar_tq'] = q_spar_arr[1:]
parameters['q_skin_tq'] = q_skin_arr[1:]
parameters['rot_tq'] = rot_arr[1:]



ribshear_init(parameters)










#Z = plot(parameters, element_locations)
#
#
#x = np.arange(0,len(parameters['normalstress'][0]))
#fig= plt.figure()
#for i in range(len(parameters['normalstress'][:,0])):
#    plt.plot(x, parameters['normalstress'][i])
#plt.show()








