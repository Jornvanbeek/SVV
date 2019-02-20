import numpy as np

def Boomarea(zprime,yprime,Astiff,s_booms,tskin,tspar,sparlength):
    Aboomslist = [ ]
    for i in range(len(zprime)):

        #First boom
        if i == 0:
            #distance between precious boom and calculated boom
            dprev = s_booms[i]*2
            #distance between next boom and calculated boom
            dnext = abs(s_booms[i+1]-s_booms[i])
            #Area of first boom
            Aboom = Astiff + ((tskin*dprev)/6)*(2+(yprime[-1]/yprime[i])) \
            + ((tskin*dnext)/6)*(2+(yprime[i+1]/yprime[i]))
            
            
        #Last boom 
        elif i == (len(zprime) - 1):
            #distance between precious boom and calculated boom
            dprev = abs(s_booms[i-1]-s_booms[i])
            #distance between next boom and calculated boom
            dnext = s_booms[0]*2

            #Area of last boom
            Aboom = Astiff + ((tskin*dprev)/6)*(2+(yprime[i-1]/yprime[i])) \
            + ((tskin*dnext)/6)*(2+(yprime[0]/yprime[i]))
            
            
        #spar booms
        elif  yprime[i] == max(yprime) or  yprime[i] == min(yprime): 
            #distance between precious boom and calculated boom
            dprev = abs(s_booms[i-1]-s_booms[i])
            #distance between next boom and calculated boom
            dnext = abs(s_booms[i+1]-s_booms[i])
            #spar length
            dspar = sparlength
            
            Aboom = ((tskin*dprev)/6)*(2+(yprime[i-1]/yprime[i])) \
            + ((tskin*dnext)/6)*(2+(yprime[i+1]/yprime[i])) \
            + ((tspar*dspar)/6)*(2-1)
            #minus 1 here due to symmetry around the zprime axis, no Astiffener due to no stiffener here
            
        #boom on the z-axis
        elif yprime[i] == 0: 
            Aboom = Astiff

        #middle booms excluding spar booms and z-axis boom
        else:
            #distance between precious boom and calculated boom
            dprev = abs(s_booms[i-1]-s_booms[i])
            #distance between next boom and calculated boom
            dnext = abs(s_booms[i+1]-s_booms[i])
            
            
            #Area of middle booms excluding spar booms
            Aboom = Astiff + ((tskin*dprev)/6)*(2+(yprime[i-1]/yprime[i])) \
            + ((tskin*dnext)/6)*(2+(yprime[i+1]/yprime[i]))
            
     
        Aboomslist.append(Aboom)
        Abooms = np.array(Aboomslist)
        
    return(Abooms)