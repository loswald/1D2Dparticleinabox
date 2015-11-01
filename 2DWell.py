import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show

print ("Enter X Length of 1D Potential Well:")
lengthxstring = input()
lengthx = float(lengthxstring)

print ("Enter Y Length of 1D Potential Well:")
lengthystring = input()
lengthy = float(lengthystring)

print ("Enter nx:")
nxstring = input()
nx = float(nxstring)

print ("Enter ny:")
nystring = input()
ny = float(nystring)

x = np.arange(0., lengthx, (lengthx-0)/100)
y = np.arange(0., lengthy, (lengthy-0)/100)

def func_vec(x, y):
    return (np.sqrt(2/lengthx)*np.sqrt(2/lengthx)*np.sin((x)*(nx*3.14/lengthx))*np.sin((y)*(ny*3.14/lengthy)))
X1,Y1 = meshgrid(x, y)
Z = func_vec(X1, Y1)
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X1, Y1, Z, rstride=1, cstride=1, 
                      cmap=cm.RdBu,linewidth=0, antialiased=False)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.set_xlabel('LOCATION')
ax.set_ylabel('LOCATION')
ax.set_zlabel('WAVE FUNCTION')

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
