# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 13:35:04 2019

@author: Arthur
"""
import numpy as np

def qb_T(parameters, element_locations, T, q_spar_arr, q_skin_arr, rot_arr):
    s_booms = element_locations['s_booms']
    ha = parameters['h']
    t_skin = parameters['t_skin']
    t_spar = parameters['t_spar']
    G = parameters['G']
    d = parameters['skin_length']
    A_cellI = parameters['A_cell1']
    A_cellII = parameters['A_cell2']
#    T = parameters['Torque']

    Equations = np.matrix([[(np.pi/(2*G*t_skin)+(G*t_spar))*ha/(2*A_cellI),-1*ha/(G*t_spar*2*A_cellI),-1],[-1*ha/(G*t_spar*2*A_cellII),2*parameters['skin_length']/(G*t_skin*2*A_cellII),-1],[2*A_cellI,2*A_cellII,0]])
    ydistance = np.matrix([[0],[0],[T]])
    
    q_LE,q_TE,RoT = np.linalg.solve(Equations,ydistance)
    q_spar = q_TE - q_LE
    
    #flow around the aileron    
    i = np.array([0])
    j = np.array([0])
    k = np.array([0])
    
    i = np.where(s_booms <= d)[0]  #flow over top trailing edge
    j = np.where(np.logical_and(s_booms > d, s_booms < d + np.pi*ha/2))[0]  #flow from top trailing edge over circular leading edge
    k = np.where(np.logical_and(s_booms>=d+np.pi*ha/2, s_booms<= 2*parameters['skin_length']+np.pi*ha/2))[0]  #flow from beginning bottom trailing edge to end
        
    q1 = np.ones(len(i))*q_TE[0,0]
    q2 = np.ones(len(j))*q_LE[0,0]
    q3 = np.ones(len(k))*q_TE[0,0]
    
    q_skin = np.append(np.append(q1,q2),q3)    
    
    q_spar_arr = np.vstack([q_spar_arr,q_spar])
    q_skin_arr = np.vstack([q_skin_arr,q_skin])
    rot_arr = np.vstack([rot_arr,RoT])
    return q_spar_arr, q_skin_arr, rot_arr
    
    #I might change the i,j,k things into our slist, so wait to implement
