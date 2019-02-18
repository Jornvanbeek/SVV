# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:03:03 2019

@author: tomhu
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt

def SkinPerimeter(slist):
    
    zcoord=np.array([])
    ycoord=np.array([])
    
    for s in slist:
        
        if s < d :
             z = (Ca - h / 2) / d * s
             y = h / 2 / d * s
            
        elif s < d + np.pi * h / 2:
            beta = (s - d) / (h / 2)
            z = (Ca - h / 2) + (h / 2) * np.sin(beta)
            y = (h / 2) * np.cos(beta)
            
        elif s < d * 2 + np.pi * h / 2 :
            z =  (Ca - h / 2) - (Ca - h / 2) / d * (s - d - np.pi * h / 2)
            y = -h / 2 + (h / 2) / d * (s - d - np.pi * h / 2)
            
    zcoord = np.append(zcoord , z)
    ycoord = np.append(ycoord , y)
    
    return ycoord, zcoord

            
            

            
            
            
            
            
            
Ca = 0.505
h = 0.161
d = np.sqrt((h/2)**2 + (Ca - h/2)**2)