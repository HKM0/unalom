import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Gúla csúcsai
vertices = np.array([[0, 0, 0],  # A pont (0)
                     [1, 0, 0],  # B pont (1)
                     [1, 1, 0],  # C pont (2)
                     [0, 1, 0],  # D pont (3)
                     [0.5, 0.5, 1]])  # E pont, a gúla csúcsa (4)

# Gúla oldalai (háromszögek)
faces = [[vertices[0], vertices[1], vertices[4]],  # ABE
         [vertices[1], vertices[2], vertices[4]],  # BCE
         [vertices[2], vertices[3], vertices[4]],  # CDE
         [vertices[3], vertices[0], vertices[4]],  # DAE
         [vertices[0], vertices[1], vertices[2], vertices[3]]]  # ABCD (alap)

# 3D ábra létrehozása
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Gúla oldalainak hozzáadása
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

# Tengelyek beállítása
ax.set_xlabel('X tengely')
ax.set_ylabel('Y tengely')
ax.set_zlabel('Z tengely')

# Tengelyhatárok beállítása
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Megjelenítés
plt.show()