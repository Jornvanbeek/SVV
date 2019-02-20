import numpy as np
from math import *

def Normalstress(Izzprimeid,Iyyprimeid,Minternalz,Minternaly,centroid,yprime_booms,zprime_booms,boomareas):
    #normalstress along booms due to bending around z axis
    ycentroid = centroid[0]
    zcentroid = centroid[1]
    
    totalstressz = np.zeros[len(boomareas),3]
    totalstressy = np.zeros[len(boomareas),3]
    
    for i in range(len(Minternalz)):
        totalstressz[0,i] = Minternalz
        for j in range(len(y_booms)):
            sigmaz = (Minternalz[i]*(ycentroid-y_booms[j]))/Izz
            totalstressz[1,j] = boomareas[j]
            totalstressz[2,j] = sigmaz
    
    for i in range(len(Minternaly)):
        totalstressz[0,i] = Minternaly
        for j in range(len(z_booms)):
            sigmay = (Minternalz[i]*(zcentroid-z_booms[j]))/Iyy
            totalstressy[1,j] = boomareas[j]
            totalstressy[2,j] = sigmay
    
    return(totalstressz,totalstressy)