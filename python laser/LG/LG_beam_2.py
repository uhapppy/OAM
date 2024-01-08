import numpy as np
import matplotlib.pyplot as plt



from calcul_beam import LG_Mode , Gaussian_Mode








fig , ax = plt.subplots(1,3)



for i  in range(0,3):
    l=3
    helical_beam = LG_Mode(p=0,l=l,wavelength=632.8e-9,w0=1)
    gaussian_beam = Gaussian_Mode(wavelength=632.8e-9,w0=1)

    x = np.linspace(-5, 5, 2000)
    y = np.linspace(-5, 5, 2000)

    print(helical_beam.get_ZR())

    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    PHI_1 = np.arctan2(Y,X)

    z_helical = helical_beam.ZR+1000000
    z_gaussian = gaussian_beam.ZR



    if i == 0 :
        Intensity_total = helical_beam.get_intensity(R,1)
    elif i == 1 :
        field_helical = helical_beam.get_field(R,1,PHI_1)
        Intensity_total = np.abs((np.exp(1*1j)+field_helical)**2) 
    elif i == 2 :
        field_helical = helical_beam.get_field(R,z_helical,PHI_1)
        Intensity_total = np.abs((np.exp(1*1j)+field_helical)**2) 


    ax[i].pcolormesh(X, Y, Intensity_total,cmap="coolwarm")
    ax[i].set_aspect('equal')
    ax[i].axis('off')












# fig , ax = plt.subplots(1,3)



# surface_1 = ax[0].pcolormesh(X, Y, Intensity_gaussian,cmap="grey")
# ax[0].set_title("Gaussian beam")
# ax[0].set_aspect('equal')


# surface_2 = ax[1].pcolormesh(X, Y, Intensity_helical,cmap="grey")
# ax[1].set_title("Helical beam")
# ax[1].set_aspect('equal')

# surface_3 = ax[2].pcolormesh(X, Y, Intensity_total,cmap="inferno")
# ax[2].set_title("Total beam")
# ax[2].set_aspect('equal')


# fig.tight_layout()

# plt.pcolormesh(X, Y, Intensity_total,cmap="coolwarm")
# plt.axis('off')
# plt.colorbar()
    
ax[0].set_title("Input mode")
ax[1].set_title("Beam waist")
ax[2].set_title("Rayleight range")

plt.savefig('LG_beam.png',dpi=600,bbox_inches='tight')
plt.show()










