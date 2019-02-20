import numpy as np
from math import pi

def center_gravity(c, h, span,t_skin, t_spar, A_st, n_st,element_locations, parameters):
    
    y = 0
    x = .5* span
    parameters['cog_x'] = x
    parameters['cog_y'] = y
    
    
    A_arc = 0.5 * h * pi * t_skin
    A_spar = t_spar * h
    A_skin = (((c-h)**2+(0.5*h)**2)**0.5)*2*t_skin
    A_tot = A_st * n_st + A_arc + A_spar + A_skin
    
    cg_spar = c-0.5*h
    cg_arc = 4*0.5*h/(3*pi) + c - 0.5*h

    z = (cg_arc * A_arc + A_spar * cg_spar + A_skin * 0.5*(c-0.5*h) + sum(element_locations['z_stiffeners'])*A_st)/A_tot
    parameters['cog_z'] = z
    

def ideal_cog(parameters):
    
    parameters['ideal_cog_x'] = 1
    parameters['ideal_cog_x'] = 1
    parameters['ideal_cog_x'] = 1   

#idealized
def I_yy(z_booms, parameters):
    #moment of inertia
    A_booms = parameters['Abooms']
    z_cg =parameters['cog_z']
    I_YY = 0
    
    for i in range(len(z_booms)):
        I_YY = I_YY + A_booms[i]*(z_booms[i]-z_cg)**2 
        
    parameters['Iyy'] = I_YY
    

def I_zz(y_booms, parameters):
    #moment of inertia
    A_booms = parameters['Abooms']
    I_ZZ = 0
    
    for i in range(len(y_booms)):
        I_ZZ = I_ZZ + A_booms[i]*y_booms[i]**2
        
    parameters['Izz'] = I_ZZ
    
def I_zznon(y_stiff,t_spar,h,c, t_skin,skinlength, A_stiff, parameters):
    I_zzspar = t_spar*(h)**3/12
    I_zzLE = pi*t_skin*(0.5*h)**3*0.5
    I_zzTE = 2*(c-0.5*h)**3*t_skin*(0.5*h/skinlength)**2/12
    I_zzstiff = 0
    for i in range(len(y_stiff)):
        
        I_zzstiff = I_zzstiff + A_stiff * y_stiff**2
        
        
        
    I_zzstiff = I_zzstiff + I_zzLE + I_zzTE + I_zzspar
    
    parameters['Izz_non_ideal'] = I_zzstiff
    