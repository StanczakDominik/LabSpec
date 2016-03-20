import numpy as np
import matplotlib.pyplot as plt
import h5py
from scipy.integrate import simps

nx = ny = 160
nz = 1000
dx = dy = dz = 1

x = y = np.arange(0, nx*dx, dx)
z = np.arange(0, nz*dz, dz)
X,Y,Z = np.meshgrid(x,y,z)

with h5py.File("data.hdf5", "r") as f:
    psi = f['psi']
    gradx = f['gradx']
    grady = f['grady']
    gradz = f['gradz']
    currents_x = f['currentsx']
    currents_y = f['currentsy']
    currents_z = f['currentsz']

    z_min, z_max = 450, 650
    x_min = 10

    Z1 = Z[x_min,ny/2,z_min:z_max]
    VZ1 = currents_z[x_min,ny/2,z_min:z_max]/np.abs(psi[x_min,ny/2,z_min:z_max])**2
    plt.plot(Z1, VZ1, label=1)
    integral_1 = simps(VZ1, dx=dz)

    X2 = Y[x_min:int(nx/2)+1, ny/2, z_max]

    # print(X2)
    VX2 = currents_x[x_min:int(nx/2)+1, ny/2, z_max]/np.abs(psi[x_min:int(nx/2)+1, ny/2, z_max])**2
    plt.plot(X2, VX2, label=2)
    integral_2 = simps(VX2, dx=dx)

    Z3 = Z[nx/2,ny/2,z_min:z_max]
    # print(Z3)
    VZ3 = currents_z[nx/2,ny/2,z_min:z_max]/np.abs(psi[nx/2,ny/2,z_min:z_max])**2
    plt.plot(Z3, VZ3, label=3)
    integral_3 = simps(VZ3, dx=-dz)

    X4 = Y[x_min:int(nx/2)+1, ny/2, z_min]
    # print(X4)
    VX4 = currents_x[x_min:int(nx/2)+1, ny/2, z_min]/np.abs(psi[x_min:int(nx/2)+1, ny/2, z_min])**2
    plt.plot(X4, VX4, label=4)
    integral_4 = simps(VX4, dx=-dx)

    total = integral_1 + integral_2 + integral_3 + integral_4
    print(integral_1, integral_2, integral_3, integral_4, total, total/2/np.pi, sep="\n")
    plt.legend()
    plt.show()
    # print(integral_1, integral_3, integral_1+integral_3)
    # integral_2 = simps(velocity_x[0:nx/2+1, ny/2, z_max], dx=dx)
    # integral_4 = simps(velocity_x[0:nx/2+1, ny/2, z_min], dx=-dx)
