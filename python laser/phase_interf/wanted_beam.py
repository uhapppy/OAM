import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3, 3, 1000)
y = np.linspace(-3, 3, 1000)

X, Y = np.meshgrid(x, y)

def phase(x, y,l):
    return l*(np.arctan2(y, x)+np.pi)%(2*np.pi)



plt.pcolormesh(X, Y, phase(X, Y,10))
plt.colorbar()
plt.show()