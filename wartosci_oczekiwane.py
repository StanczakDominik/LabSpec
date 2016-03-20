import numpy as np
import scipy.integrate as scint
import h5py
nx = ny = 160
nz = 1000
dx = dy = dz = 1

x = y = np.arange(nx)
z = np.arange(nz)
X,Y,Z = np.meshgrid(x,y,z)

with h5py.File("data.hdf5", "r") as f:
    psi = f['psi'][...]
    grad_x = f['gradx'][...]
    grad_y = f['grady'][...]
    grad_z = f['gradz'][...]
    NX, NY, NZ = grad_x.shape

    dx = dy = dz = 1

    x = y = np.arange(0, NX*dx, dx)
    z = np.arange(0, NZ*dz, dz)
    X,Y,Z = np.meshgrid(x,y,z)

    X = X - NX/2
    Y = Y - NY/2
    Z = Z - NZ/2

    # psi_Lz_psi = -1j*(X*grad_y - Y*grad_x)*psi.conjugate()
    # Intgr_Lz_x = scint.simps(psi_Lz_psi, axis=0)
    # Intgr_Lz_x_y = scint.simps(Intgr_Lz_x, axis=0)
    # Intgr_Lz_x_y_z = scint.simps(Intgr_Lz_x_y, axis=0)
    # print(Intgr_Lz_x_y_z)

    psi_Lx_psi = -1j*(Y*grad_z - Z*grad_y)*psi.conjugate()
    Intgr_Lx_x = scint.simps(psi_Lx_psi, axis=0)
    Intgr_Lx_x_y = scint.simps(Intgr_Lx_x, axis=0)
    Intgr_Lx_x_y_z = scint.simps(Intgr_Lx_x_y, axis=0)
    print(Intgr_Lx_x_y_z)

    # psi_Ly_psi = -1j*(Z*grad_x - X*grad_z)*psi.conjugate()
    # Intgr_Ly_x = scint.simps(psi_Ly_psi, axis=0)
    # Intgr_Ly_x_y = scint.simps(Intgr_Ly_x, axis=0)
    # Intgr_Ly_x_y_z = scint.simps(Intgr_Ly_x_y, axis=0)
    # print(Intgr_Ly_x_y_z)
