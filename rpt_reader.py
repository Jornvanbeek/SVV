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

dfdis_arr = np.array(df_dis, dtype = float)[:,[0,5,6,7,8]]





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
for i in range(len(base)):
    base[i].append(dfdis_arr[i,1])
    base[i].append(dfdis_arr[i,2])
    base[i].append(dfdis_arr[i,3])
    base[i].append(dfdis_arr[i,4])
    
for v in df_array:
    if len(base[int(v[1])-1]) <9:
        base[int(v[1])-1].append(v[-1])
for i in range(len(base)):
    if len(base[i]) ==9:
     
        base2.append(base[i])

multiplication_factor = 100
for node in base2:
    xs = np.append(xs,node[1])
    ys = np.append(ys,node[2])
    zs = np.append(zs,node[3])
    val = np.append(val,node[4])
    disp = np.append(disp,node[5])
    xdisp = np.append(xdisp,node[6])
    ydisp = np.append(ydisp,node[7])
    zdisp = np.append(zdisp,node[8])
    


xdisp = xs+xdisp*multiplication_factor
ydisp = ys+ydisp*multiplication_factor
zdisp = zs+zdisp*multiplication_factor


def scatter3d(x,y,z, cs, colorsMap='jet'):
    cm = plt.get_cmap(colorsMap)
    cNorm = matplotlib.colors.Normalize(vmin=min(cs), vmax=max(cs))
    scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x, y, z, c=scalarMap.to_rgba(cs))
    scalarMap.set_array(cs)
    fig.colorbar(scalarMap)
    plt.show()
    
##    
#
##ax.set_xlim(min(zs)-max(zs)*.5, max(zs)*1.5)
##ax.set_ylim(min(xs)-max(xs)*.5, max(xs)*1.5)
##ax.set_zlim(min(ys)-max(ys)*.5, max(ys)*1.5)
scatter3d(zs,xs,ys, val)
scatter3d(zs,xs,ys,disp)
scatter3d(zs,xs,ydisp,disp)

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot_surface(zs,xs,np.vstack([ys,np.ones(len(ys))]))




