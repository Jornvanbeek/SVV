import numpy as np

def Boomarea(zprime,yprime,Astiff,s_booms,tskin,tspar,sparlength,parameters):
    Aboomslistz = [ ]
    Aboomslisty = [ ]
    neutralaxisy = parameters['cog_z']
    
    #--------------------distance to zprime-axis-------------------
    for i in range(len(zprime)):
        #First boom
        if i == 0:
            #distance between precious boom and calculated boom
            dprev = s_booms[i]*2
            #distance between next boom and calculated boom
            dnext = abs(s_booms[i+1]-s_booms[i])
            #Area of first boom
            Aboomz = Astiff + ((tskin*dprev)/6)*(2+(yprime[-1]/yprime[i])) \
            + ((tskin*dnext)/6)*(2+(yprime[i+1]/yprime[i])) \
          
            + ((tskin*dprev)/6)*(2+((neutralaxisy-zprime[-1])/(neutralaxisy-zprime[i]))) \
            + ((tskin*dnext)/6)*(2+((neutralaxisy-zprime[-1])/(neutralaxisy-zprime[i])))
            
            
        #Last boom 
        elif i == (len(zprime) - 1):
            #distance between precious boom and calculated boom
            dprev = abs(s_booms[i-1]-s_booms[i])
            #distance between next boom and calculated boom
            dnext = s_booms[0]*2

            #Area of last boom
            Aboomz = Astiff + ((tskin*dprev)/6)*(2+(yprime[i-1]/yprime[i])) \
            + ((tskin*dnext)/6)*(2+(yprime[0]/yprime[i]))
            
            
        #spar booms
        elif  yprime[i] == max(yprime) or  yprime[i] == min(yprime): 
            #distance between precious boom and calculated boom
            dprev = abs(s_booms[i-1]-s_booms[i])
            #distance between next boom and calculated boom
            dnext = abs(s_booms[i+1]-s_booms[i])
            #spar length
            dspar = sparlength
            
            Aboomz = ((tskin*dprev)/6)*(2+(yprime[i-1]/yprime[i])) \
            + ((tskin*dnext)/6)*(2+(yprime[i+1]/yprime[i])) \
            + ((tspar*dspar)/6)*(2-1)
            #minus 1 here due to symmetry around the zprime axis, no Astiffener due to no stiffener here
            
        #boom on the z-axis
        elif yprime[i] == 0: 
            Aboomz = Astiff

        #middle booms excluding spar booms and z-axis boom
        else:
            #distance between precious boom and calculated boom
            dprev = abs(s_booms[i-1]-s_booms[i])
            #distance between next boom and calculated boom
            dnext = abs(s_booms[i+1]-s_booms[i])
            
            
            #Area of middle booms excluding spar booms
            Aboomz = Astiff + ((tskin*dprev)/6)*(2+(yprime[i-1]/yprime[i])) \
            + ((tskin*dnext)/6)*(2+(yprime[i+1]/yprime[i]))
            
            Aboomslistz.append(Aboomz)
    Aboomsz = np.array(Aboomslistz)
    parameters['Aboomsz'] = Aboomsz
            
    
    #-------------------ybooms so distance to vertical line through centroid---------------
    for i in range(len(zprime)):
        #First boom
        if i == 0:
            #distance between precious boom and calculated boom
            dprev = s_booms[i]*2
            #distance between next boom and calculated boom
            dnext = abs(s_booms[i+1]-s_booms[i])
            #Area of first boom
            Aboomy = Astiff \
            + ((tskin*dprev)/6)*(2+((neutralaxisy-zprime[-1])/(neutralaxisy-zprime[i]))) \
            + ((tskin*dnext)/6)*(2+((neutralaxisy-zprime[-1])/(neutralaxisy-zprime[i])))
            
            
        #Last boom 
        elif i == (len(zprime) - 1):
            #distance between precious boom and calculated boom
            dprev = abs(s_booms[i-1]-s_booms[i])
            #distance between next boom and calculated boom
            dnext = s_booms[0]*2

            #Area of last boom
            Aboomy = Astiff \
            + ((tskin*dprev)/6)*(2+((neutralaxisy-zprime[i-1])/(neutralaxisy-zprime[i]))) \
            + ((tskin*dnext)/6)*(2+((neutralaxisy-zprime[0])/(neutralaxisy-zprime[i])))
            
            
        #spar booms
        elif  yprime[i] == max(yprime) or  yprime[i] == min(yprime): 
            #distance between precious boom and calculated boom
            dprev = abs(s_booms[i-1]-s_booms[i])
            #distance between next boom and calculated boom
            dnext = abs(s_booms[i+1]-s_booms[i])
            #spar length
            dspar = sparlength
            
            Aboomy = ((tskin*dprev)/6)*(2+((neutralaxisy-zprime[i-1])/(neutralaxisy-zprime[i]))) \
            + ((tskin*dnext)/6)*(2+((neutralaxisy-zprime[i+1])/(neutralaxisy-zprime[i]))) \
            + ((tskin*dspar)/6)*(2+1)
            #plus 1 here due to being on the same side of the axis

        #middle booms excluding spar booms and z-axis boom
        else:
            #distance between precious boom and calculated boom
            dprev = abs(s_booms[i-1]-s_booms[i])
            #distance between next boom and calculated boom
            dnext = abs(s_booms[i+1]-s_booms[i])
            
            
            #Area of middle booms excluding spar booms
            Aboomy = Astiff \
            + ((tskin*dprev)/6)*(2+((neutralaxisy-zprime[i-1])/(neutralaxisy-zprime[i]))) \
            + ((tskin*dnext)/6)*(2+((neutralaxisy-zprime[i+1])/(neutralaxisy-zprime[i])))
     
        Aboomslisty.append(Aboomy)
        Aboomsy = np.array(Aboomslisty)
        parameters['Aboomsy'] = Aboomsy