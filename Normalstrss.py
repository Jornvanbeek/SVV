import numpy as np

def Normalstress(parameters,element_locations,Izzprimeid,Iyyprimeid,Minternalz,Minternaly,centroidid,yprime_booms,zprime_booms):
    #normalstress along booms due to bending around z axis
    ycentroid = parameters['ideal_cog_y']
    zcentroid = parameters['iedal_cog_z']
    
    totalstressz = np.zeros[len(yprime_booms),len(Minternalz)]
    totalstressy = np.zeros[len(yprime_booms),len(Minternalz)]
    
    #Calculates normal stress due to bending around zprime axis
    for i in range(len(parameters['Moment_z'])):
        for j in range(len(element_locations['z_booms'])):
            sigmazx = (parameters['Moment_z'][i]*(ycentroid-element_locations['y_booms'][j]))/Izzprimeid
            totalstressz[j,i] = sigmazx
            
    #Calculates normal stress due to bending around yprime axis
    for i in range(len(parameters['Moment_y'])):
        for j in range(len(zprime_booms)):
            sigmayx = (parameters['Moment_y'][i]*(zcentroid-element_locations['z_booms'][j]))/Iyyprimeid
            totalstressy[j,i] = sigmayx
    
    parameters['normalstress'] = totalstressy + totalstressz
    
    