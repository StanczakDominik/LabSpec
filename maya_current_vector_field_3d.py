import numpy as np
import mayavi.mlab as mlab
import h5py
nx = ny = 160
nz = 1000
dx = dy = dz = 1
x = y = np.arange(0, nx*dx, dx)
z = np.arange(0, nz*dz, dz)
X,Y,Z = np.meshgrid(x,y,z)
# psi = np.load("disp_psi.npy")
# every_X_vector = 3

with h5py.File("data.hdf5", "r") as f:
    X = f['X']
    Y = f['Y']
    Z = f['Z']
    currents_x = f['currentsx']
    currents_y = f['currentsy']
    currents_z = f['currentsz']

    z_min, z_max = 450, 650
    x_min = 10

    X1, Y1, Z1 = X[x_min,ny/2,z_min:z_max], Y[x_min,ny/2,z_min:z_max], Z[x_min,ny/2,z_min:z_max]
    mlab.plot3d(X1, Y1, Z1, tube_radius=5)
    X2, Y2, Z2 = X[x_min:int(nx/2)+1, ny/2, z_max], Y[x_min:int(nx/2)+1, ny/2, z_max], Z[x_min:int(nx/2)+1, ny/2, z_max]
    mlab.plot3d(X2, Y2, Z2, tube_radius=5)
    X3, Y3, Z3 = X[nx/2,ny/2,z_min:z_max], Y[nx/2,ny/2,z_min:z_max], Z[nx/2,ny/2,z_min:z_max]
    mlab.plot3d(X3, Y3, Z3, tube_radius=5)
    X4, Y4, Z4 = X[x_min:int(nx/2)+1, ny/2, z_min], Y[x_min:int(nx/2)+1, ny/2, z_min], Z[x_min:int(nx/2)+1, ny/2, z_min]
    mlab.plot3d(X4, Y4, Z4, tube_radius=5)
    NS = 5
    quiver = mlab.quiver3d(X[::NS,::NS,::NS], Y[::NS,::NS,::NS], Z[::NS,::NS,::NS],
        currents_x[::NS,::NS,::NS], currents_y[::NS,::NS,::NS], currents_z[::NS,::NS,::NS])
    mlab.show()
