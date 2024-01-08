import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from cmap import Colormap
from mpl_toolkits.axes_grid1.inset_locator import InsetPosition

font = {'size'   : 5}

matplotlib.rc('font', **font)


x = np.linspace(-20, 20, 1000)
y = np.linspace(-20, 20, 1000)

X, Y = np.meshgrid(x, y)

def intensity(x, y,l):

    ref = np.exp(x*1j)

    heli = np.exp((l*(np.arctan2(y, x)+np.pi))*1j)

    output = np.abs(ref+heli)**2

    return output






fig, axs = plt.subplots(ncols=5, nrows=5)
# add an artist, in this case a nice label in the middle...

m_value = np.arange(0,25,1)
print(m_value)
count=0
for row in range(5):
    for col in range(5):
        plot = axs[row,col].pcolormesh(X, Y, intensity(X, Y,m_value[count])/np.max(intensity(X, Y,m_value[count])),cmap = Colormap('viridis').to_mpl())
        axs[row,col].set_box_aspect(1)
        axs[row,col].axis('off')
        count+=1


# m_value = np.linspace(0,25,1)
# for i in range(5):
#     for j in range(5):
#         plot = axis[i,j].pcolormesh(X, Y, intensity(X, Y,m_value[i+j])/np.max(intensity(X, Y,m_value[i+j])),cmap = Colormap('viridis').to_mpl())
#         axis[i,j].set_title("l = " +str(m_value[i+j]))
#         axis[i,j].set_box_aspect(1)
#         axis[i,j].axis('off')



plt.tight_layout()

plt.show()


