import numpy as np
import matplotlib.pyplot as plt



from calcul_beam import LG_Mode


helical_beam = LG_Mode(p=1,l=2,wavelength=405e-9,w0=1)


x = np.linspace(-5, 5, 2000)
y = np.linspace(-5, 5, 2000)
z = helical_beam.get_ZR()


X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
PHI = np.arctan2(Y,X)



fig, ax = plt.subplots(3,3,figsize=(10,10))


l_values=[0,1,2]
p_values=[0,1,2]

for l ,index_l in enumerate(l_values):
    for p ,index_p in enumerate(p_values):
        helical_beam = LG_Mode(p=index_p,l=index_l,wavelength=405e-9,w0=1)
        z = helical_beam.get_ZR()
        field_helical = helical_beam.get_field(R,z,PHI)

        
        #Intensity_helical = np.abs(field_helical)**2
        Intensity_helical=np.abs((np.exp(2*np.pi*1j)+field_helical)**2)
        Intensity_helical = Intensity_helical/np.max(Intensity_helical)
        ax[l,p].pcolormesh(X, Y, Intensity_helical,cmap="viridis",vmin=0,vmax=1)
        ax[l,p].set_aspect('equal')
        ax[l,p].set_axis_off()
        
        
        ax[l,p].text(-1, 5.5, str(index_p)+" , "+str(index_l) , fontsize=15, color='black')









plt.gca().set_aspect('equal')
plt.savefig('LG_beam_test.png',dpi=600,bbox_inches='tight')
plt.show()