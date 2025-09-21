import numpy as np
import glob
from scipy.interpolate import griddata
import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Specify the full file path
grd_files = glob.glob('/Users/kyle/python/分幅_臺北市100MDEM/96232049dem.grd')

# Read data from the specified file
data = []
for file_path in grd_files:
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            data.append(parts)


data = np.array(data, dtype=float)
print(data.shape)


# # # Extract x, y, z columns
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

# # Create grid for contouring
xi = np.linspace(x.min(), x.max(), 200)
yi = np.linspace(y.min(), y.max(), 200)
xi, yi = np.meshgrid(xi, yi)

# Interpolate z values onto grid
zi = griddata((x, y), z, (xi, yi), method='cubic')

# Plot 3D surface and contour
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(xi, yi, zi, cmap='viridis', edgecolor='none', alpha=0.8)
contour3d = ax.contour(xi, yi, zi, levels=20, colors='black', linewidths=0.5, offset=zi.min())
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='height')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Map')

# Plot contour map
plt.figure(figsize=(8, 6))
cp = plt.contourf(xi, yi, zi, levels=20, colors='white')
contours = plt.contour(xi, yi, zi, levels=20, colors='black', linewidths=0.5)
plt.clabel(contours, inline=True, fontsize=8, fmt="%.1f")
plt.colorbar(cp, label='height')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('GRD Contour Map')
plt.show()
