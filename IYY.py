# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 16:30:47 2019

@author: Arthur
"""

import numpy as np
#idealized
def I_yy(z_booms,A_booms,z_cg):
    #moment of inertia
    I_YY = 0
    
    for i in range(len(y_booms)):
        I_YY = I_YY + A_booms[i]*(z_booms[i]-z_cg)**2 
        
    return I_YY
    