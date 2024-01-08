import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from cmap import Colormap
from mpl_toolkits.axes_grid1.inset_locator import InsetPosition

font = {'size'   : 5}

matplotlib.rc('font', **font)








def intensity(x, y,l):


    ref = np.exp(x*1j)

    heli = np.exp((l*(np.arctan2(y, x)+np.pi))*1j)

    output = np.abs(ref+heli)**2
    
    return output


x = np.linspace(-20, 20, 1000)
y = np.linspace(-20, 20, 1000)
X, Y = np.meshgrid(x, y)
fig , axis = plt.subplots(1,6)

m_value = [-1,0,1,2,3]
for i in range(5):
    plot = axis[i].pcolormesh(X, Y, intensity(X, Y,m_value[i])/np.max(intensity(X, Y,m_value[i])),cmap = Colormap('jet').to_mpl())
    axis[i].set_title("l = " +str(m_value[i]))
    axis[i].set_box_aspect(1)
    axis[i].axis('off')


ip = InsetPosition(axis[4], [1.05,0,0.05,1]) 
axis[5].set_axes_locator(ip)

fig.colorbar(plot, cax=axis[5],ax=axis)
plt.subplots_adjust(wspace=0.5)
#plt.show()
plt.savefig("Test.png",dpi=800,bbox_inches='tight',pad_inches=0.1,format="png") 





# x = np.linspace(-100, 100, 10000)
# y = np.linspace(-100, 100, 10000)


# X, Y = np.meshgrid(x, y)

# fig , axis = plt.subplots(1,1)

# m_value = 10000


# miaw = intensity(X, Y,m_value)

# plot = axis.pcolormesh(X, Y, miaw/np.max(miaw),cmap = Colormap('seaborn:mako').to_mpl())
# axis.set_box_aspect(1)
# axis.axis('off')



# plt.savefig("Intensity_"+str(m_value)+"_5.png",dpi=1500,bbox_inches='tight',pad_inches=0.1,format="png") 
