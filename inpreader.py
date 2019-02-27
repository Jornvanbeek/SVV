import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

base = []
nset = []
eset = []


comments = 0
i = 0
with open('F100/F100n.inp') as file:
    for line in file:
        if line[0] == '*':
            comments +=1
            i+=1
        elif i<5000: 
            i +=1
            strlist = [float(str(x)) for x in line.split(',')]
            
            if i< 3235 +comments:
                base.append(strlist)
#            elif 3234+3250+comments <= i <= 3234+comments:
#                nset.append(strlist)
#            elif i >= 3234+3250+comments
        
#        i +=1
xs = np.array([])
ys = np.array([])
zs = np.array([])
val = np.array([])
for node in base:
    xs = np.append(xs,node[1])
    ys = np.append(ys,node[2])
    zs = np.append(zs,node[3])
    
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(min(zs)-max(zs)*.5, max(zs)*1.5)
ax.set_ylim(min(xs)-max(xs)*.5, max(xs)*1.5)
ax.set_zlim(min(ys)-max(ys)*.5, max(ys)*1.5)
ax.scatter(zs,xs,ys)
plt.show()

