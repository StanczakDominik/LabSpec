import numpy as np
import mayavi.mlab as mlab
nx = ny = 160
nz = 1000
dx = dy = dz = 1
X = np.load("disp_X.npy")
Y = np.load("disp_Y.npy")
Z = np.load("disp_Z.npy")
# psi = np.load("disp_psi.npy")
# every_X_vector = 3

currents_x = np.abs(np.load("disp_currentsx.npy"))
currents_y = np.abs(np.load("disp_currentsy.npy"))
currents_z = np.abs(np.load("disp_currentsz.npy"))
density = np.load("disp_density.npy")
velocity_x = currents_x/density
velocity_y = currents_y/density
velocity_z = currents_z/density


z_min, z_max = 550, 551
loop = np.array([[0,ny/2,z_min], [0,ny/2,z_max], [nx/2, ny/2, z_max], [nx/2, ny/2, z_min], [0,ny/2, z_min]])
loop_x, loop_y, loop_z = loop[:,0], loop[:,1], loop[:,2]
quiver = mlab.quiver3d(X, Y, Z,currents_x, currents_y, currents_z)
# quiver = mlab.quiver3d(X, Y, Z,velocity_x, velocity_y, velocity_y)
pipes = mlab.plot3d(loop_x, loop_y, loop_z, tube_radius=5)
mlab.show()
