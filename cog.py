import numpy as np
from math import pi

def center_gravity(element_locations, parameters, c = 0.505, h = 16.1/100., span = 1.611,t_skin = 1.1/1000., t_spar = 2.4/1000., A_st = 3.6*10**-5, n_st = 11 ):
    
    y = 0
    x = .5* span
    parameters['cog_x'] = x
    parameters['cog_y'] = y
    
    
    parameters['cog_z'] = ((t_skin*h**2)/3 + parameters['skin_length']*t_skin*(-c+0.5*h) + sum(A_st*element_locations['z_stiffeners']))/(0.5*h*t_skin+h*t_spar+parameters['skin_length']*2*t_skin+A_st*n_st)
    

def ideal_cog(element_locations, parameters):
    
    z = sum(element_locations['z_booms']*parameters['Aboomsy'])/sum(parameters['Aboomsy'])
    
    parameters['ideal_cog_z'] = z   
    
    y = sum(element_locations['y_booms']*parameters['Aboomsz'])/sum(parameters['Aboomsz'])
    parameters['ideal_cog_y'] = y  #this value should be zero

#idealized
def I_yy(z_booms, parameters):
    #moment of inertia
    A_booms = parameters['Aboomsy']
    z_cg =parameters['ideal_cog_z']
    I_YY = 0
    
    for i in range(len(z_booms)):
        I_YY = I_YY + A_booms[i]*(z_booms[i]-z_cg)**2 
        
    parameters['Iyy'] = I_YY
    

def I_zz(y_booms, parameters):
    #moment of inertia
    A_booms = parameters['Aboomsz']
    I_ZZ = 0
    
    for i in range(len(y_booms)):
        I_ZZ = I_ZZ + A_booms[i]*y_booms[i]**2
        
    parameters['Izz'] = I_ZZ
    
def I_zznon(parameters, y_stiff,t_spar = 2.4/1000.,h = 16.1/100.,c = 0.505, t_skin= 1.1/1000., A_stiff = 3.6*10**-5):
    
    I_zzspar = t_spar*(h)**3/12
    I_zzLE = pi*t_skin*(0.5*h)**3*0.5
    I_zzTE = 2*(c-0.5*h)**3*t_skin*(0.5*h/parameters['skin_length'])**2/12
    I_zzstiff = 0
    for i in range(len(y_stiff)):
        
        I_zzstiff = I_zzstiff + A_stiff * y_stiff[i]**2
        
        
        
    I_zzstiff = I_zzstiff + I_zzLE + I_zzTE + I_zzspar
    
    parameters['Izz_non_ideal'] = I_zzstiff
    