import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.cm as cmx



head = 20
skiprows=list(range(0,head))+[head+1,head+2]
footer = 13
df = pd.read_fwf("../../F100/F100_SLC1.rpt",sep = '  ', skiprows = skiprows ,skipfooter = footer,skip_blank_lines=True, keep_default_na = False)



foot = df.loc[df['Element.Label'] == '']


first = foot.iloc[0].name
last = foot.iloc[-1].name+2
df2 = df[last:]
df = df[:first]


df_array = np.array(df,dtype = float)
arr = np.zeros([len(df_array),1])
df_array = np.hstack([df_array,arr])
df_array[:,-1] = (df_array[:,-3]+df_array[:,-2])/2

df_array2 = np.array(df2,dtype = float)
arr2 = np.zeros([len(df_array2),1])
df_array2 = np.hstack([df_array2,arr2])
df_array2[:,-1] = (df_array2[:,-3]+df_array2[:,-2])/2

#values = np.zeros(int(df_array[-1,0]))
#for data in df_array:
#    values[int(data[1])] = data[-1]

head = 16
skiprows=list(range(0,head))+[head+1,head+2]
footer = 43
df_dis = pd.read_fwf("../../F100/F100_ULC1.rpt",sep = '  ', skiprows = skiprows ,skipfooter = footer,skip_blank_lines=True, keep_default_na = False)

dfdis_arr = np.array(df_dis[:3234], dtype = float)[:,[0,5,6,7,8]]





base = []
nset = []
eset = []


comments = 0
i = 0
with open('../../F100/F100-19.inp') as file:
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
disp = np.array([])
base2 = []
xdisp =np.array([])
ydisp =np.array([])
zdisp =np.array([])
for i in range(len(base)): #add the displacements to the base for each node
    base[i].append(dfdis_arr[i,1]) #magnitude
    base[i].append(dfdis_arr[i,2]) #Z
    base[i].append(dfdis_arr[i,3]) #X
    base[i].append(dfdis_arr[i,4]) #Y
    
for v in df_array:
    if len(base[int(v[1])-1]) <9:
        base[int(v[1])-1].append(v[-1]) #add avg von mises stress
        
for i in range(len(base)):
    if len(base[i]) ==9:
     
        base2.append(base[i]) #new list with only featured nodes

multiplication_factor = 1
for node in base2: #make separate lists to plot
    xs = np.append(xs,node[1])
    ys = np.append(ys,node[2])
    zs = np.append(zs,node[3])
    val = np.append(val,node[-1])
    disp = np.append(disp,node[4])
    xdisp = np.append(xdisp,node[5])
    ydisp = np.append(ydisp,node[6])
    zdisp = np.append(zdisp,node[7])
    


xdisp = xs+xdisp*multiplication_factor
ydisp = ys+ydisp*multiplication_factor
zdisp = zs+zdisp*multiplication_factor


def scatter3d(x,y,z, cs, colorsMap='jet', title = None, save = False, savename = None):
    cm = plt.get_cmap(colorsMap)
    cNorm = matplotlib.colors.Normalize(vmin=min(cs), vmax=max(cs))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x, y, z, c=scalarMap.to_rgba(cs))
    scalarMap.set_array(cs)
    fig.colorbar(scalarMap)
    plt.title(title)
    if save:
        plt.savefig(savename, papertype = 'a0' )
    plt.show()
    



leading_edge = np.zeros(len(base2[0]))
trailing_edge = np.zeros(len(base2[0]))


for node in base2: 
    if node[3]>80:
        leading_edge = np.vstack([leading_edge, node])
        
        
    elif node[3]<-424:
        trailing_edge = np.vstack([trailing_edge, node])

#leading_edge = np.sort(leading_edge[1:])
#trailing_edge = np.sort(trailing_edge[1:])

def plotdeflections(x,dygLE, dygTE, dzgLE, dzgTE):
#    fig = plt.figure()
#    plt.plot(leading_edge[:,1], leading_edge[ + leading_edge[:,7])
#    plt.plot(trailing_edge[:,1], trailing_edge[:,7])
#    plt.title('Trailing and Leading edge deflection in x-direction')
#    plt.savefig('LE_TE_x')
    
    fig = plt.figure(1)
#    plt.plot(leading_edge[:,1], leading_edge[:,2]+leading_edge[:,8])
    plt.grid()
    plt.scatter(trailing_edge[1:,1]/1000, (trailing_edge[1:,6])/1000)
    plt.xlabel("Length of list (number)")
    plt.ylabel("Time taken (seconds)")
    
    plt.plot(x, dygTE.T)
    plt.title('y-deflection of trailing edge')
    plt.savefig('TE_y')
    
    fig = plt.figure(2)
    plt.grid()
    plt.scatter(trailing_edge[1:,1]/1000, (trailing_edge[1:,3]+trailing_edge[1:,5])/1000)
    plt.plot(x, dzgTE.T)
#    plt.plot(trailing_edge[:,1],(trailing_edge[:,3]- trailing_edge[:,6])/1000)
    plt.title('z-deflection of trailing edge')
    plt.savefig('TE_z')
    
    fig = plt.figure(3)
#    plt.plot(leading_edge[:,1], leading_edge[:,2]+leading_edge[:,8])
    plt.grid()
    plt.scatter(leading_edge[1:,1]/1000, (leading_edge[1:,6])/1000)
    plt.plot(x, dygLE.T)
    plt.title('y-deflection of leading edge')
    plt.savefig('LE_y')
    
    fig = plt.figure(4)
    plt.grid()
    plt.scatter(leading_edge[1:,1]/1000, (leading_edge[1:,3]+leading_edge[1:,5])/1000)
    plt.plot(x, dzgLE.T)
#    plt.plot(trailing_edge[:,1],(trailing_edge[:,3]- trailing_edge[:,6])/1000)
    plt.title('z-deflection of leading edge')
    plt.savefig('LE_z')
    
    
    scatter3d(zdisp,xdisp,ydisp, val)
    
   