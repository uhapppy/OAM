import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from cmap import Colormap
from mpl_toolkits.axes_grid1.inset_locator import InsetPosition

font = {'size'   : 5}

matplotlib.rc('font', **font)

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)

X, Y = np.meshgrid(x, y)

def phase_heli(x, y,l):
    return (l*(np.arctan2(y, x)-np.pi))%(2*np.pi)



def phase_ref(x, y):
    return x%(2*np.pi)


fig, axis = plt.subplots(1,4)

#color = Colormap('cet_c5').to_mpl()
color = Colormap('hsv').to_mpl()
l=3

plot_1 = axis[0].pcolormesh(X, Y, phase_heli(X, Y,l),cmap=color)
axis[0].set_title("Helical Phase (l = "+str(l)+")")
axis[0].set_box_aspect(1)
axis[0].axis('off')


plot_2 = axis[1].pcolormesh(X, Y, phase_ref(X, Y),cmap=color)
axis[1].set_title("Reference Phase")
axis[1].set_box_aspect(1)
axis[1].axis('off')

plot_3 = axis[2].pcolormesh(X, Y, (phase_heli(X, Y,l)+phase_ref(X, Y))%(2*np.pi),cmap=color)
axis[2].set_title("Combined Phase")
axis[2].set_box_aspect(1)
axis[2].axis('off')

ip = InsetPosition(axis[2], [1.05,0,0.05,1]) 
axis[3].set_axes_locator(ip)


fig.colorbar(plot_3, cax=axis[3],ax=axis)

plt.subplots_adjust(wspace=0.5)
plt.savefig("phase.png",dpi=600,bbox_inches='tight',pad_inches=0.1) 

plt.show()