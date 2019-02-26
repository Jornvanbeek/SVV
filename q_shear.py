import numpy as np
from math import pi

# shear flow qb in the z' axis



def qb_z(parameters, element_locations):
    qb_1 = np.array([0])
    qb_2 = np.array([0])
    qb_spar = 0
    I_yy = parameters['Iyy']
    z_booms = element_locations['z_booms']
    B_booms = parameters['Aboomsz'] #check if this should be y or z
    s_booms = element_locations['s_booms']
    S_z = parameters['Shear_z']
    z_cg = parameters['cog_z']
    h_a = parameters['h']
    n_stiffener = parameters['n_stiffener']
    d = parameters['skin_length']
    
    

    qb = 0
    for i in range(len(z_booms)):
        if s_booms[i]<d:
            qb = - (S_z/I_yy)*(B_booms[i] * (z_booms[i]-z_cg))
            qb_1 = np.append(qb_1, qb + qb_1[i-1])

    arc = (pi * h_a) / 4
    j_1 = np.where(np.logical_and(s_booms > d, s_booms < arc + d))[0][::-1]

    for j in j_1:
        qb = qb - (S_z/I_yy)*(B_booms[j] * (z_booms[j]-z_cg))
        qb_2 = np.append(qb_2, qb + qb_2[j-j_1[0]-1])
    qb_sym = np.append(qb_1, qb_2[::-1])

    if n_stiffener % 2 ==0:
        qb_panel = np.append(qb_sym, qb_sym[::-1])
    else:
        qb_panel = np.append(qb_sym, qb_sym[::-1][1:])



    parameters['qb_spar_z_shear'] = qb_spar
    parameters['qb_panel_shear'] = qb_panel
    


# shear flow qb in the y' axis
def qb_y(parameters, element_locations):
    

    
    I_zz = parameters['Izz']
    y_booms = element_locations['y_booms']
    B_booms = parameters['Aboomsy'] #check if this should be y or z
    s_booms = element_locations['s_booms']
    S_y = np.transpose(parameters['Shear_y'])
    A_cell1 = parameters['A_cell1']
    A_cell2 = parameters['A_cell2']
    h_a = parameters['h']
    t_sk = parameters['t_skin']
    t_sp = parameters['t_spar']
    G = parameters['G']
    C_a = parameters['c']
    d = parameters['skin_length']
    z_Sy = parameters['zcs']
    
    qb_1 = np.zeros([1,len(S_y[0])])
    qb_2 = np.zeros([1,len(S_y[0])])
    qb_3 = np.zeros([1,len(S_y[0])])


    for i in range(len(y_booms)):
        if s_booms[i] < d:
            qb = - (S_y / I_zz) * (B_booms[i] * (y_booms[i]))
            parameters['qb'] = qb
            
            qb_1 = np.vstack([qb_1, qb + qb_1[-1,:]])

        else:
            spar_number1 = i
            break
    qb_1 = qb_1[1:,:]
    parameters['qb1']= qb_1
    
    qb_spar = qb_1[-1,:] - (S_y / I_zz) * (B_booms[spar_number1] * (y_booms[spar_number1]))

    semi = (pi * h_a) / 2
    circ = (pi * h_a)

    j_1 = np.where(np.logical_and(s_booms > d, s_booms <= semi + d))[0][:-1]

    for j in j_1:
        qb = - (S_y / I_zz) * (B_booms[j] * (y_booms[j]))
        qb_2 = np.vstack([qb_2, qb + qb_2[-1,:]])
    
    qb_2 = qb_2[1:,:]
    
    
    k_1 = np.where(np.logical_and(s_booms >= (d + semi), s_booms < circ))[0][1:]

    spar_number2 = j_1[-1] + 1
    
    parameters['qb2'] = qb_2
    parameters['qbspar'] = qb_spar
    
    qb_3 = np.vstack([qb_3, qb_2[-1] + qb_spar - (S_y / I_zz) * (B_booms[spar_number2] * (y_booms[spar_number2]))])
    
    for k in k_1:
        
        qb = - S_y / I_zz * B_booms[k] * y_booms[k]
        qb_3 = np.vstack([qb_3, qb + qb_3[-1,:]])
    parameters['qb3'] = qb_3
    qb_3 = qb_3[1:,:]


#q_0 and angle of twist of airfoil
    
    i_1 = range(len(qb_1))
    i_2 = range(len(qb_1), len(qb_1) + len(qb_2))
    i_3 = range(len(qb_1) + len(qb_2), len(qb_1) + len(qb_2) + len(qb_3))
    


#finding the redundant shear flow in both the two cells

    o_TE = 0
    o_LE = 0

    for i in i_1:
        if i==0:
            o_TE = o_TE + qb_1[i] * (s_booms[i] - 0 )/(t_sk * G)
        else:
            o_TE = o_TE + qb_1[i] * (s_booms[i] - s_booms[i-1] )/(t_sk * G)
        o_TE = o_TE + (qb_spar * h_a) / (t_sp * G)



    for i in i_3:
        if i == i_3[-1]:

            o_TE = o_TE + qb_3[i - i_2[-1] -1] * (s_booms[i] - s_booms[i-1] )/(t_sk * G)
        else:
            o_TE = o_TE + qb_3[i - i_2[-1] -1] * (s_booms[i] - s_booms[i-2] )/(t_sk * G)


    for i in i_2:
        o_LE = o_LE + qb_2[i - i_1[-1] -1 ] * (s_booms[i] - s_booms[i-1])/(t_sk * G)

    o_LE = o_LE + (qb_spar * h_a) /(t_sp *G)

    #moment arm

    r = (h_a /2) * np.cos(np.arctan2((h_a/2), C_a - h_a / 2))

    M = 0


    for i in i_1:
        if i ==0:
            F = (s_booms[i] - 0) * qb_1[0]
            M = M + (F*r)

        else:
             F = (s_booms[i] - s_booms[i-1]) * qb_1[i]
             M = M + (F*r)

        F = h_a * (qb_spar)
        M = M + (F*r)

    for i in i_3:
         if i == i_3[-1]:
             F = (s_booms[i] - s_booms[i-1]) * qb_3[i - i_2[-1] -1]
             M = M + F*r

         else:
             F = (s_booms[-1] - s_booms[i-1]) * qb_3[i - i_1[-1] -1]
             M = M + (F*r)

    for i in i_2:
        F = (s_booms[i] - s_booms[i-1]) * qb_2[i-i_1[-1] -1]
        M = M + (F * (h_a/2))


# finding matrix A and y to find the shear flow in the sections
#matrix A has entries a(1-3)(1-3)

    a11 = ((semi)/(t_sk *G) + h_a/(t_sp * G)) / (2 * A_cell1)
    a12 = -h_a /( t_sk *G) /(2 * A_cell1)
    a13 = -1

    a21 = - h_a / (t_sp * G ) /(2 *A_cell2)
    a22 = (2 * d/ (t_sk * G ) + h_a / ( t_sp * G)) / (2 * A_cell2)
    a23 = -1

    a31 = 2 * A_cell1
    a32 = 2 * A_cell2
    a33 = 0

    y1 = -o_LE
    y2 = -o_TE
    y3 = -S_y * (z_Sy - (C_a -h_a/2)) - M


    A = np.array([[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]])
    y = np.vstack([y1, y2, y3])
    
    q0_LE, q0_TE, RoT = np.dot(np.linalg.inv(A), y)
    
    
    q1 = qb_1 + q0_TE
    q2 = qb_2 + q0_LE
    q3 = qb_3 + q0_TE

    q_spar = qb_spar + q0_TE + q0_LE
    parameters['q1'] = q1
    parameters['q2'] = q2
    parameters['q3'] = q3
    q_skin = np.vstack([np.vstack([q1,q2]),q3])
    
    parameters['qb_spar_y_shear'] = q_spar
    parameters['qb_skin_shear'] = q_skin
    parameters['rot_shear'] = RoT
    




















