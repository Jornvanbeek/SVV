'''
======================
3D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

def plot(parameters, element_locations):
    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    
    # Make data.
    X = np.arange(0, len(parameters['normalstress'][0]), dtype = float)
    Y = element_locations['z_booms']
    X, Y = np.meshgrid(X, Y)
    
#    elements = (np.arange(0,len(parameters['normalstress'][0]), dtype = float))
#    Z = elements
    ybooms = np.vstack(element_locations['y_booms'])
    boomsmatrix = ybooms
    for i in range(1, len(parameters['normalstress'][0])):
        boomsmatrix = np.hstack([boomsmatrix,ybooms])

    Z = boomsmatrix
    print(Z)
    print(np.shape(Z), 'shape z')
    print(np.shape(X), 'shape x')
    print( np.shape(Y), 'shape y')
    

    
    
    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    
    # Customize the z axis.
#    ax.set_zlim(int(Z.min()),int(Z.max()))
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    
    # Add a color bar which maps values to colors.
    fig.colorbar(X,Y,parameters['normalstress'], shrink=0.5, aspect=5)
    
    plt.show()
    return Z
