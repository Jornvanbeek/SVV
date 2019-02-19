# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 17:25:56 2019

@author: Arthur
"""

import numpy as np
from math import *

def I_zznon(y_stiff,A_stiff):
    I_zzspar = thick*(2*semicirc)**3/12
    I_zzLE = pi*thick*semicirc**3*0.5
    I_zzTE = 2*ha**3*thick*(semicirc/skinlength)**2/12
    I_zzstiff = 0
    for i in range(len(y_stiff)):
        
        I_zzstiff = I_zzstiff + A_stiff * y_stiff**2
        
        
        
    I_zzstiff = I_zzstiff + I_zzLE + I_zzTE + I_zzspar
        