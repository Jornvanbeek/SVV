import numpy as np
from math import *

def center_gravity(c, h, span,t_skin, t_spar, t_st,h_st, w_st, n_st,element_locations):
    cog = []
    y = 0
    x = .5* span
    cog.append(x)
    cog.append(y)
    
    
    A_st = t_st * (h_st + w_st)
    A_arc = 0.5 * h * pi * t_skin
    A_spar = t_spar * h
    A_skin = (((c-h)**2+(0.5*h)**2)**0.5)*2*t_skin
    A_tot = A_st * n_st + A_arc + A_spar + A_skin
    

    
    cg_spar = c-0.5*h
    cg_arc = 4*0.5*h/(3*pi) + c - 0.5*h

    
    
    z = (cg_arc * A_arc + A_spar * cg_spar + A_skin * 0.5*(c-0.5*h) + sum(element_locations['z_stiffeners'])*A_st)/A_tot
    cog.append(z)
    return cog #array in which x,y,z cg is given