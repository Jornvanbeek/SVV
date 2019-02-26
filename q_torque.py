# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 13:35:04 2019

@author: Arthur
"""
import numpy as np

def qb_T(parameters, element_locations):

    A_cellI = parameters['A_cell1']
    A_cellII = parameters['A_cell2']

    Equations = np.matrix([[2*A_cellI,2*A_cellII,0],[(np.pi/(2*G*t_skin)+(G*t_spar))*ha/(2*A_cellI),-1*ha/(G*t_spar*2*A_cellI),-1],[-1*ha/(G*t_spar*2*A_cellII),2*parameters['skin_length']/(G*t_skin*2*A_cellII),-1]])
    ydistance = np.matrix([[0],[0],[T]])
    
    q_LE,q_TE,RoT = np.linalg.solve(Equations,ydistance)
    q_spar = q_TE - q_LE
    
    #flow around the aileron    
    
    i = np.where(s_boom < d)[0] = np.append(i, i[-1]+1) #flow over top trailing edge
    j = np.where(np.logical_and(s_boom > d, s_boom < d + np.pi*h/2))[0] = np.append(j, j[-1]+1) #flow from top trailing edge over circular leading edge
    k = np.where(np.logical_and(s_boom>d+np.pi*h/2 <= 2*parameters['skin_length']+np.pi*h/2)) [0] = np.append(k, k[-1]+1) #flow from beginning bottom trailing edge to end
        
    q1 = np.matrix(len(i)*[q_TE])
    q2 = np.matrix(len(j)*[q_LE])
    q3 = np.matrix(len(k)*[q_TE])
    
    q_skin = np.append(np.append(q1,q2),q3)    
    
    parameters['q_spar_tq'] = q_spar
    parameters['q_skin_tq'] = q_skin
    parameters['rot_tq'] = RoT
    
    
    #I might change the i,j,k things into our slist, so wait to implement