# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:14:54 2019

@author: Arthur
"""

import numpy as np

def I_zz(y_booms,A_booms):
    #moment of inertia
    I_ZZ = 0
    
    for i in range((y_booms)):
        I_ZZ = I_ZZ + A_booms[i]*y_booms[i]**2
        
    return I_ZZ
    