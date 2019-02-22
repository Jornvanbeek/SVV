# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 13:35:04 2019

@author: Arthur
"""
import numpy as np

def qb_T(T):

    A_cellI = np.pi*(h/2)^2/2
    A_cellII = h*(c-h/2)/2

    Equations = np.matrix([[2*A_cellI,2*A_cellII,0],[(np.pi/(2*G*t_skin)+(G*t_spar))*ha/(2*A_cellI),-1*ha/(G*t_spar*2*A_cellI),-1],[-1*ha/(G*t_spar*2*A_cellII),2*parameters['skin_length']/(G*t_skin*2*A_cellII),-1]])
    ydistance = np.matrix([[0],[0],[T]])
    
    q_LE,q_TE,RoT = np.linalg.solve(Equations,ydistance)
    
    
    return q_LE, q_TE, RoT