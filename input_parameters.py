import numpy as np
def inputparameters(parameters):
    parameters['c'] = 0.505                   #m, chord lenght
    parameters['l'] = 1.611                   #m, span
    parameters['x_1'] = 0.125                 #m, x location of hinge 1
    parameters['x_2'] = 0.498                 #m, x location of hinge 2
    parameters['x_3'] = 1.494                 #m, x location of hinge 3
    parameters['x_a'] = 24.5/100.             #cm, distance between actuator 1 and 2
    parameters['h'] = 16.1/100.               #cm, height of aileron
    parameters['t_skin'] = 1.1/1000.          #mm, thickness
    parameters['t_spar'] = 2.4/1000.          #mm, thickness
    parameters['t_stiffener'] = 1.2/1000.     #mm, thickness
    parameters['h_stiffener'] = 1.3/100.      #cm, height
    parameters['w_stiffener'] = 1.7/100.      #cm, width of stiffener
    parameters['n_stiffener'] = 11            #number of stiffeners
    parameters['d_1'] = 0.389/100.            #cm, displacement hinge 1
    parameters['d_3'] = 1.245/100.            #cm, displacement hinge 3
    parameters['theta'] = 30.                 #degrees, max upward deflection
    parameters['P_2'] = 49.2*1000             #kN, load actuator 2
    parameters['q'] = 3.86*1000               #kN/m, aerodynamic load
    
    parameters['G'] = 28. * ( 10. ** 9. )
    parameters['E']  = 73.1*10**9             #Pa E-modulus
    parameters['n'] = 1000
    parameters['skin_length'] = np.sqrt( (parameters['c']-parameters['h']*0.5)**2 + (0.5*parameters['h'])**2) #length of upper or lower angled part of skin in meters, checked
    parameters['A_cell1'] = np.pi*(parameters['h']/2)**2/2 #inside de circular part
    parameters['A_cell2'] = parameters['h']*(parameters['c']-parameters['h']/2)/2 #inside the triangular part

