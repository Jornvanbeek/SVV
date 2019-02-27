# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:25:56 2019

@author: Arthur
"""

import numpy as np
from math import *

def I_zznon(y_stiff,t_spar,h,c, t_skin,skinlength, A_stiff, parameters):
    I_zzspar = t_spar*(h)**3/12
    I_zzLE = pi*t_skin*(0.5*h)**3*0.5
    I_zzTE = 2*(c-0.5*h)**3*t_skin*(0.5*h/skinlength)**2/12
    I_zzstiff = 0
    for i in range(len(y_stiff)):
        
        I_zzstiff = I_zzstiff + A_stiff * y_stiff**2
        
        
        
    I_zz = I_zzstiff + I_zzLE + I_zzTE + I_zzspar
    
    parameters['Izz_non_ideal'] = I_zz
