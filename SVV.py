# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 14:03:03 2019

@author: tomhu
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt

def SkinPerimeter(slist,c,h,nst):
    zcoord=np.array([])
    ycoord=np.array([])
    
    for s in slist:
        
        if s < d :
             z = (c - h / 2) / d * s - c + h/2
             y = h / 2 / d * s
            
        elif s < d + np.pi * h / 2:
            beta = (s - d) / (h / 2)
            z = (c - h / 2) + (h / 2) * np.sin(beta) - c + h/2
            y = (h / 2) * np.cos(beta)
            
        elif s <= d * 2 + np.pi * h / 2 :
            z =  (c - h / 2) - (c - h / 2) / d * (s - d - np.pi * h / 2) - c + h/2
            y = -h / 2 + (h / 2) / d * (s - d - np.pi * h / 2)
        y = round(y, 13)
        z = round(z, 13)
        zcoord = np.append(zcoord , z)
        ycoord = np.append(ycoord , y)
    
    return zcoord, ycoord

            
def skin_init(parameters, c = 0.505,h = 16.1/100.,nst = 11):            
    global d
    d = parameters['skin_length']
    c = parameters['c']
    h = parameters['h']
    nst = parameters['n_stiffener']
    
    loc = dict()
    
    circumference = np.pi * h / 2 + 2 * d
    spacing_st = circumference / nst
    s_stiffeners = np.arange(spacing_st/2,circumference,spacing_st)
    s_sparcaps = np.array ([d, d + np.pi * h / 2])
    s_booms = np.sort(np.append(s_stiffeners , s_sparcaps ))
    s_skin = np. linspace (0, circumference , 1000)
    
    loc['z_stiffeners'] , loc['y_stiffeners'] = SkinPerimeter ( s_stiffeners,c,h,nst )
    loc['z_sparcaps'] , loc['y_sparcaps'] = SkinPerimeter ( s_sparcaps,c,h,nst )
    loc['z_booms'] , loc['y_booms'] = SkinPerimeter (s_booms,c,h,nst)
    loc['z_skin'] , loc['y_skin'] = SkinPerimeter (s_skin,c,h,nst)
    loc['s_booms'] = s_booms

    return loc
    
          