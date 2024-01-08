import matplotlib.pyplot as plt
import numpy as np

r = np.linspace(0, 10, 10)
phi = np.linspace(0, 2 * np.pi, 20)

R, PHI = np.meshgrid(r, phi)
X = R * np.cos(PHI)
Y = R * np.sin(PHI)

colors = ['tab:cyan', 'tab:red', 'tab:green', 'tab:orange', 'tab:red']
edge_props = {'linewidth': 0.5, 'edgecolors': 'black'}

fig, axes = plt.subplots(1, 3, figsize=(12, 12), subplot_kw=dict(projection='3d'))

#
# Plot separate discs
#
ax = axes[0]
ax.view_init(azim=-65, elev=35, roll=0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('PHI')

#Select a position along z for each disc
z_vals = [0, 1, 2]

for z in z_vals:
    ax.plot_surface(
        X, Y, np.full(Y.shape, z),
        alpha=0.8, color=colors[z_vals.index(z)],
        **edge_props
    )

#
# Plot a twister
#
ax = axes[1]
ax.view_init(azim=-65, elev=35, roll=0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('PHI')

Z = PHI
ax.plot_surface(
    X, Y, Z,
    alpha=1, color=colors[-1], **edge_props
)
ax.set_box_aspect(aspect=None, zoom=0.9)

#Optional arrows
ax.quiver(
    0, 0, 0,
    0, 0, Z.max() * 1.3,
    color='black', alpha=1, linewidth=4,
    arrow_length_ratio=0.2,
)
ax.quiver(
    0, 0, 0,
    X.max() * 1.1, 0, 0,
    color='black', alpha=1, linewidth=4,
    arrow_length_ratio=0.2,
)

#
# Plot multiple twisters
#
ax = axes[2]
ax.view_init(azim=0, elev=-40, roll=-90)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('PHI')

#Radian offset of each twister
phi0_per_twister = [0, 90 * np.pi / 180]

Z = PHI
for index, phi0 in enumerate(phi0_per_twister):
    ax.plot_surface(
        R * np.cos(PHI + phi0), R * np.sin(PHI + phi0), Z,
        alpha=[0.4, 1][index], color=colors[index], **edge_props
    )

for ax in axes:
    ax.set_box_aspect(aspect=None, zoom=0.9)
    
plt.show()