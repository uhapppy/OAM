import matplotlib.pyplot as plt
import numpy as np




fig, ax = plt.subplots(2,2,figsize=(10,10),subplot_kw=dict(projection='3d'))


l_values=[0,1,2,3]
label_values = ["(a)","(b)","(c)","(d)"]
index_values = [[0,0],[0,1],[1,0],[1,1]]




for l ,index in zip(l_values , index_values):

    if l>=1:
        phase_interval = 2*np.pi/(l)
        for j in range(0,l):
            r = np.linspace(0, 1, 20)
            phi=np.linspace(0, phase_interval, 100)
            R, PHI = np.meshgrid(r, phi)
            X, Y = R*np.cos(PHI+j*phase_interval), R*np.sin(PHI+j*phase_interval)
            Z = PHI*l
            print(Z)
            #surface = ax[index[0],index[1]].plot_surface(Z, Y, X, alpha=1,linewidth=0.5,edgecolors='black',color='red')
            ax[index[0],index[1]].plot_surface(Z, Y, X, alpha=1,linewidth=0.5,cmap='cool',edgecolors='black')
            ax[index[0],index[1]].set_aspect('equalyz')
            ax[index[0],index[1]].set_axis_off()
            #ax[index[0],index[1]].text(0, 0, 1.5, label_values[l], fontsize=15, color='black')


    elif l==0:
        r = np.linspace(0, 1, 20)
        phi=np.linspace(0, 2*np.pi, 100)
        R, PHI = np.meshgrid(r, phi)
        X, Y = R*np.cos(PHI), R*np.sin(PHI)
        Z = np.pi
        ax[index[0],index[1]].plot_surface(Z, Y, X, alpha=1,linewidth=0.5,cmap='cool',edgecolors='black')
        ax[index[0],index[1]].set_aspect('equalyz')
        ax[index[0],index[1]].set_xlim(0,2*np.pi)
        ax[index[0],index[1]].set_axis_off()
        #ax[index[0],index[1]].text(0, 0, 1.5, label_values[l], fontsize=15, color='black')


ax[1,1].view_init(elev=25, azim=-60)
# yepi=ax[1,1].get_axes()
# print(yepi.azim,yepi.elev)

fig.tight_layout()
#plt.savefig("beam.png",dpi=600,bbox_inches='tight') 
plt.show()
