import numpy as np

def Normalstress(parameters,Izzprimeid,Iyyprimeid,Minternalz,Minternaly,centroidid,yprime_booms,zprime_booms):
    #normalstress along booms due to bending around z axis
    ycentroid = centroidid[0]
    zcentroid = centroidid[1]
    
    totalstressz = np.zeros[len(yprime_booms),len(Minternalz)]
    totalstressy = np.zeros[len(yprime_booms),len(Minternalz)]
    
    #Calculates normal stress due to bending around zprime axis
    for i in range(len(Minternalz)):
        for j in range(len(zprime_booms)):
            sigmazx = (Minternalz[i]*(ycentroid-yprime_booms[j]))/Izzprimeid
            totalstressz[j,i] = sigmazx
            
    #Calculates normal stress due to bending around yprime axis
    for i in range(len(Minternaly)):
        for j in range(len(zprime_booms)):
            sigmayx = (Minternaly[i]*(zcentroid-zprime_booms[j]))/Iyyprimeid
            totalstressy[j,i] = sigmayx
    
    parameters['stress'] = totalstressy + totalstressz
    
    