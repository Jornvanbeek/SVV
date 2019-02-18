import numpy as np
from math import *
def center_gravity(c, h, span,t_skin, t_spar, t_st,h_st, w_st n_st):
    y = 0
    x = .5* span
    A_st = t_st*(h_st+w_st)*n_st
    z_spar = t_spar*h*(c-0.5*h)
    z_arc = 4*0.5*h/(3*pi) + c - 0.5*h
    A_skin = (((c-h)**2+(0.5*h)**2)**0.5)*2*t_skin
    
    cog = A_skin*(c-h)*0.5 +z_arc*t_skin*pi*0.5*h +z_spar*t_spar*h
    return cog #array in which x,y,z cg is given