# main file
import numpy as np
import math as m
from definitionboomarea import Boomarea
from SVV import skin_init
from cog import center_gravity, I_yy, I_zz, I_zznon, ideal_cog
from ForceSolver import force_solver
from Normalstrss import Normalstress
from q_shear import qb_z, qb_y
from q_torque import qb_T
from ShearInRib import ribshear_init
from input_parameters import inputparameters
from Deflection import deflection
from rpt_reader import scatter3d, plotdeflections

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
  


#calculation of first parameters
element_locations = skin_init(parameters)
A_stiffener = t_stiffener * (h_stiffener + w_stiffener)
center_gravity(element_locations, parameters, c, h, l, t_skin, t_spar, A_stiffener, n_stiffener)
I_zznon(parameters, element_locations['y_stiffeners'],t_spar,h,c, t_skin, A_stiffener)
Boomarea(parameters,element_locations['z_booms'],element_locations['y_booms'],A_stiffener,element_locations['s_booms'],t_skin,t_spar,h)
ideal_cog(element_locations, parameters)
I_yy(element_locations['z_booms'], parameters)
I_zz(element_locations['y_booms'], parameters)

#calculation of forces, stresses and shear
force_solver(parameters)
Normalstress(parameters,element_locations)
qb_z(parameters,element_locations)
qb_y(parameters,element_locations)
q_spar_arr = np.zeros(1)
q_skin_arr = np.zeros(len(element_locations['s_booms']))

rot_arr = np.zeros(1)
for T in parameters['Torque']:
    q_spar_arr, q_skin_arr, rot_arr = qb_T(parameters, element_locations,T,q_spar_arr,q_skin_arr,rot_arr)

ribshear_init(parameters)

#calculation of final parameters
parameters['q_spar_tq'] = q_spar_arr[1:]
parameters['q_skin_tq'] = q_skin_arr[1:]
parameters['rot_tq'] = rot_arr[1:]
parameters['shear_booms'] = (np.transpose(parameters['q_skin_tq']) +parameters['qb_skin_shear'])/(parameters['t_skin']*10**6)
parameters['vonmises'] = np.sqrt((parameters['normalstress'])**2 + 3*(parameters['shear_booms'])**2)
vonmises =parameters['vonmises']# np.sqrt(parameters['normalstress']**2)


#plotting all results
def plotinit(values):
    values = np.abs(values)
    val = np.array([])
    zs = np.array([])
    ys = np.array([])
    xs = np.array([])
    for i in range(len(values)):
        val = np.hstack([val,values[i]])
        zs = np.hstack([zs,np.ones(len(values[i])) * element_locations['z_booms'][i]])
        xs = np.hstack([xs, np.linspace(0,parameters['l'],parameters['n'])])
        ys = np.hstack([ys, np.ones(len(values[i])) * element_locations['y_booms'][i]])

    scatter3d(zs,xs,ys, val,title = 'von Mises stresses in booms', save = True, savename = 'num_mises')
    
plotinit(parameters['vonmises'])



dyTE,dyLE,dzTE,dzLE,x = deflection(parameters)
theta = m.radians(parameters['theta'])
twist = parameters['twist']


dygLE = dyLE*m.cos(theta) - dzLE*m.sin(theta) - m.sin(theta)*h/2*np.ones(twist.T.shape)
dygTE = dyTE*m.cos(theta) - dzTE*m.sin(theta) + m.sin(theta)*(c-h/2)*np.ones(twist.T.shape) 
dzgLE = dzLE*m.cos(theta) + dyLE*m.sin(theta)+ m.cos(theta)*h/2*np.ones(twist.T.shape)
dzgTE = dzTE*m.cos(theta) + dyTE*m.sin(theta)- m.cos(theta)*(c-h/2)*np.ones(twist.T.shape) 

plotdeflections(x,dygLE, dygTE, dzgLE, dzgTE)

