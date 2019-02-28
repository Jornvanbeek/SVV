import numpy as np

def Normalstress(parameters,element_locations):
    #normalstress along booms due to bending around z axis
    ycentroid = parameters['ideal_cog_y']
    zcentroid = parameters['ideal_cog_z']
    Iyyprimeid = parameters['Iyy']
    Izzprimeid = parameters['Izz']
    
    
    totalstressz = np.zeros([len(element_locations['y_booms']),len(parameters['Moment_z'])])
    totalstressy = np.zeros([len(element_locations['y_booms']),len(parameters['Moment_z'])])
    
    #Calculates normal stress due to bending around zprime axis
    for i in range(len(parameters['Moment_z'])):
        for j in range(len(element_locations['z_booms'])):
            sigmazx = (parameters['Moment_z'][i]*(-element_locations['y_booms'][j]-ycentroid))/Izzprimeid
            totalstressz[j,i] = sigmazx
            
    #Calculates normal stress due to bending around yprime axis
    for i in range(len(parameters['Moment_y'])):
        for j in range(len(element_locations['z_booms'])):
            sigmayx = (parameters['Moment_y'][i]*(element_locations['z_booms'][j]-zcentroid))/Iyyprimeid
            totalstressy[j,i] = sigmayx
    
    parameters['normalstress'] = totalstressy + totalstressz
    
    