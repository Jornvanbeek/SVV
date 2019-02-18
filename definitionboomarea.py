import numpy as np
from math import sqrt

def Boomarea(zprime,yprime,Astiff,zcg,tskin,tspar,sparlength):
    
    for i in range(len(zprime)):
        Aboomslist = [ ]
        #First boom
        if i == 0:
            #distance between precious boom and calculated boom
            dprev = 2*sqrt(abs(zprime[i]-0)**2+abs(yprime[i]-0)**2)
            #distance between next boom and calculated boom
            dnext = sqrt(abs(zprime[i]-zprime[i+1])**2+abs(yprime[i]-yprime[i+1])**2)
            
            #Area of first boom
            Aboom = Astiff + ((tskin*dprev)/6)*(2+(yprime[-1]/yprime[i])) \
            + ((tspar*dnext)/6)*(2+(yprime[i+1]/yprime[i]))
            
        #Last boom 
        elif i == (len(zprime) - 1):
            #distance between precious boom and calculated boom
            dprev = sqrt(abs(zprime[i]-zprime[0])**2+abs(yprime[i]-yprime[0])**2)
            #distance between next boom and calculated boom
            dnext = 2*sqrt(abs(zprime[i]-0)**2+abs(yprime[i]-0)**2)
            
            #Area of last boom
            Aboom = Astiff + ((tskin*dprev)/6)*(2+(yprime[i-1]/yprime[i])) \
            + ((tskin*dnext)/6)*(2+(yprime[0]/yprime[i]))
            
        #spar booms
        elif  yprime[i] == max(yprime) or  yprime[i] == min(yprime): 
            #distance between precious boom and calculated boom
            dprev = sqrt(abs(zprime[i]-zprime[i-1])**2+abs(yprime[i]-yprime[i-1]**2))
            #distance between next boom and calculated boom
            dnext = sqrt(abs(zprime[i]-zprime[i+1])**2+abs(yprime[i]-yprime[i+1]**2))
            #spar length
            dspar = sparlength
            
            Aboom = ((tskin*dprev)/6)*(2+(yprime[i-1]/yprime[i])) \
            + ((tskin*dnext)/6)*(2+(yprime[i+1]/yprime[i])) \
            + ((tspar*dspar)/6)*(2-1)
            #minus 1 here due to symmetry around the zprime axis, no Astiffener due to no stiffener here
            
        #boom on the z-axis
        elif yprime[i] == 0: 
            Abooms = Astiff

        #middle booms excluding spar booms and z-axis boom
        else:
            #distance between precious boom and calculated boom
            dprev = sqrt(abs(zprime[i]-zprime[i-1])**2+abs(yprime[i]-yprime[i-1]**2))
            #distance between next boom and calculated boom
            dnext = sqrt(abs(zprime[i]-zprime[i+1])**2+abs(yprime[i]-yprime[i+1]**2))
            
            #Area of middle booms excluding spar booms
            Aboom = Astiff + ((tskin*dprev)/6)*(2+(yprime[i-1]/yprime[i])) \
            + ((tskin*dnext)/6)*(2+(yprime[i+1]/yprime[i]))
            
     
        Aboomslist.append(Aboom)
        Abooms = np.array(Aboomslist)
#        Abooms = np.transpose(Abooms)
        
    return(Abooms)

    

