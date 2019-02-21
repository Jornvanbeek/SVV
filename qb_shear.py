from numpy import *

# shear flow qb in the z' axis



def qb_z(I_yy, z_booms, B_booms, s_booms, S_z, z_cg):
    qb_1 = array([0])
    qb_2 = array([0])
    qb_spar = 0


    for i in range(len(z_booms)):
        if s_booms([i])<d:
            qb = - (S_z/I_yy)*(B_booms[i] * (z_booms[i]-z_cg))
            qb_1 = append(qb_1, qb + qb_1[i-1])

    arc = (pi * h_a) / 4
    j_1 = where(logical_and(s_booms > d, s_booms < arc + d))[0][::-1]

    for j in j_1:
        qb = qb - (S_z/I_yy)*(B_booms[j] * (z_booms[j]-z_cg))
        qb_2 = append(qb_2, qb + qb_2[j-j_1[0]-1])
    qb_sym = append(qb_1, qb_2[::-1])

    if n_stiffner % 2 ==0:
        qb_panel = append(qb_sym, qb_sym[::-1])
    else:
        qb_panel = append(qb_sym, qb_sym[::-1][1:])



    return qb_panel, qb_spar


# shear flow qb in the y' axis
def qb_y(I_zz, y_booms, B_booms, s_booms, S_y):
    qb_1 = array([0])
    qb_2 = array([0])
    qb_3 = array([])



    for i in range(len(y_booms)):
        if s_booms([i]) < d:
            qb = - (S_y / I_zz) * (B_booms[i] * (y_booms[i]))
            qb_1 = append(qb_1, qb + qb_1[-1])

        else:
            spar_number1 = i
            break

    qb_spar = qb_1[-1] - (S_y / I_zz) * (B_booms[spar_number1] * (y_booms[spar_number1]))

    semi = (pi * h_a) / 2
    circ = (pi * h_a)

    j_1 = where(logical_and(s_booms > d, s_booms <= semi + d))[0][:-1]

    for j in j_1:
        qb = - (S_y / I_zz) * (B_booms[j] * (y_booms[j]))
        qb_2 = append(qb_2, qb + qb_2[-1])

    k_1 = where(logical_and(s_booms >= (d + semi), s_booms < circ))[0][1:]

    spar_number2 = j_1[-1] + 1

    qb_3 = append(qb_3, qb_2[-1] + qb_spar - (S_y / I_zz) * (B_booms[spar_number2] * (y_booms[spar_number2])))

    for k in k_1:
        qb = - Sy / I_zz * B_booms[k] * y_booms[k]
        qb_3 = append(qb_3, qb + qb_3[-1])

