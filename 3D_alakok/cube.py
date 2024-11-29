import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 

def draw_cube(ax):

    r = [-1, 1]
    vertikalis_baszas = np.array([[x, y, z] for x in r for y in r for z in r])

    edges = [
        [0, 1], [1, 3], [3, 2], [2, 0],
        [4, 5], [5, 7], [7, 6], [6, 4],
        [0, 4], [1, 5], [2, 6], [3, 7]
    ]


    for edge in edges: ax.plot3D(*zip(*vertikalis_baszas[edge]), color="b")

def update_view(ax, angle):
    ax.view_init(elev=10., azim=angle)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

draw_cube(ax)
ax.set_xlabel('X mint xelkötöm magam a fára')
ax.set_ylabel('Y mint yajjj geci')
ax.set_zlabel('Z mint zsalmalé')


for angle in range(0, 360):
    update_view(ax, angle)
    plt.draw()
    plt.pause(0.01)
    
plt.show() 