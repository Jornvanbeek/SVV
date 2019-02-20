import numpy as np
from math import *

def Normalstress(Izzprimeid,Iyyprimeid,Minternalz,Minternaly,centroid,yprime_booms,zprime_booms,boomareas):
    #normalstress along booms due to bending around z axis
    ycentroid = centroid[0]
    zcentroid = centroid[1]
    
    totalstressz = np.zeros[len(boomareas),2]
    totalstressy = np.zeros[len(boomareas),2]
    
    for i in range(len(Minternalz)):
        totalstressz[0,i] = Minternalz
        for j in range(len(yprime_booms)):
            sigmaz = (Minternalz[i]*(ycentroid-yprime_booms[j]))/Izzprimeid
            totalstressz[1,j] = sigmaz
    
    for i in range(len(Minternaly)):
        totalstressz[0,i] = Minternaly
        for j in range(len(zprime_booms)):
            sigmay = (Minternalz[i]*(zcentroid-zprime_booms[j]))/Iyyprimeid
            totalstressy[1,j] = sigmay
    
    return(totalstressz,totalstressy)