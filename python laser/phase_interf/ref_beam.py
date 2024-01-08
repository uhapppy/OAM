import numpy as np 
import matplotlib.pyplot as plt
import math

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)

X, Y = np.meshgrid(x, y)

def phase(x, y):
    return x%2*np.pi

plt.pcolormesh(X, Y, phase(X, Y),cmap="hsv")
plt.colorbar()
plt.show()
