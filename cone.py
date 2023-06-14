from math import sin, cos, pi, sqrt 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import numpy as np

fig = plt.figure(figsize=(6,3))
z = fig.add_subplot(111, projection='3d')

theta = np.linspace(0, 2*np.pi, 100)
r = np.linspace(0, 2, 100)
t,R =np.meshgrid(theta, r)

X = R*np.cos(t)
Y = R*np.sin(t)
Z = R*2.5


z.set_xlabel('x axis')
z.set_ylabel('y axis')
z.set_zlabel('z axis')
z.set_xlim(-2.5,2.5)
z.set_ylim(-2.5,2.5)
z.set_zlim(0,5)


z.plot_surface(X, Y, Z,alpha=0.8, cmap=cm.copper)
fig.savefig("Cone.png", dpi=100,transparent = False)


height = 5  # this is given as a solution to the equation I link above

# The angular rate at which the twists/ are wound. The larger the number, the denser the twists. 
# We need each twist to be 0.3 meters apart as measured on the surface of the cone. 
a = 2*pi/0.3 * sqrt(17)/4.0
# The radius of the cone at vertical distance 1. 
# Given by the restriction that the width of the base of the cone should be double its height.
# Initially I had equal height/4.0 which is wrong
r = 2/5.0  

# draw the spiral 
pointsPerUnit = 1000  # the density of points to draw our curve smooth (and also do our numerical validation at the end)
# define the domain of the vertical dimention z, because x and y are defined based on z
z = [i/float(pointsPerUnit) for i in range(0, int(height*pointsPerUnit) +1)] 
x = [t*r*cos(a*t) for t in z]
y = [t*r*sin(a*t) for t in z]


ax = fig.gca(projection='3d')
ax.plot(x, y, z, linewidth = 2, color='green')

plt.show() 


# verifying that the height solution given by the equation indeed produces a spiral wire of length 29.7 meters
px, py, pz = (0,0,0)
distance = 0
for cx,cy,cz in zip(x,y,z):
    distance += sqrt((cx-px)*(cx-px) + (cy-py)*(cy-py) + (cz-pz)*(cz-pz))
    px, py, pz = (cx, cy, cz)

print ('Total length of wire for height', height, 'is:', distance)
