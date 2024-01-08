import numpy as np

import matplotlib.pyplot as plt

x=np.linspace(-3,3,1000)
y=np.linspace(-3,3,1000)

X,Y=np.meshgrid(x,y)


l=5
PHI_1=np.arctan2(Y,X)*l

f=1000000
PHI_2 = (2*np.pi/(405e-9))*(np.sqrt(X**2+Y**2+f**2)-f)



I = np.cos(PHI_1-PHI_2)*np.exp(-((X**2+Y**2)/2))





plt.figure()
plt.pcolormesh(X,Y,I,cmap='grey')
plt.colorbar()
plt.show()



