from __future__ import print_function
import numpy as np
import scipy.integrate as scint
nx = ny = 160
nz = 1000
dx = dy = dz = 1

x = y = np.arange(0, nx*dx, dx)
z = np.arange(0, nz*dz, dz)
X,Y,Z = np.meshgrid(x,y,z)

psi = np.load("disp_psi.npy")
    # ZAPIS DANYCH Z TXT DO .NPY
    # data = np.loadtxt("pythondata3")
    # print(data, data.shape)
    # add_data = data[:,0]+1j*data[:,1]
    # print("added")
    # np.save("added_data", add_data)
    #
    # psi = reshaped = np.reshape(add_data, (nx, ny, nz))
    # print("reshaped")
    # print(reshaped.shape)
    # np.save("psi", psi)
    # print("saved")

##import scipy.fftpack as fft
##psi_transform = fft.fftn(psi)
##k_x = fft.fftfreq(nx, dx)
##k_y = fft.fftfreq(ny, dy)
##k_z = fft.fftfreq(nz, dz)
##KX, KY, KZ = np.meshgrid(k_x, k_y, k_z)

# gradx_transform = psi_transform*1j*KX
# gradx = fft.ifftn(gradx_transform)
# np.save("gradx", gradx)
# currents_x = psi.conjugate()
# currents_x *= gradx
# currents_x_p2 = psi
# currents_x_p2 *= gradx.conjugate()
# currents_x -= currents_x_p2
# currents_x /= 2.j
# np.save("currents_x", currents_x)
grad_x = np.load("disp_gradx.npy")

# grady_transform = psi_transform*1j*KY
# grady =fft.ifftn(grady_transform)
# np.save("grady", grady)
# currents_y = psi.conjugate()
# currents_y *= grady
# currents_y_p2 = psi
# currents_y_p2 *= grady.conjugate()
# currents_y -= currents_y_p2
# currents_y /= 2.j
# np.save("currents_y", currents_y)
grad_y = np.load("disp_grady.npy")

# gradz_transform = psi_transform*1j*KZ
# gradz = fft.ifftn(gradz_transform)
# np.save("gradz", gradz)
# currents_z = psi.conjugate()
# currents_z *= gradz
# currents_z_p2 = psi
# currents_z_p2 *= gradz.conjugate()
# currents_z -= currents_z_p2
# currents_z /= 2.j
# np.save("currents_z", currents_z)

with h5py.File("data.hdf5", "r") as f:


    grad_z= np.load("disp_gradz.npy")
    NX, NY, NZ = grad_x.shape

    dx = dy = dz = 1

    x = y = np.arange(0, NX*dx, dx)
    z = np.arange(0, NZ*dz, dz)
    X,Y,Z = np.meshgrid(x,y,z)

    X -= NX/2.0;
    Y -= NY/2.0;
    Z -= NZ/2.0;

    psi_Lz_psi = -1j*(X*grad_y - Y*grad_x)*psi.conjugate()
    psi_Lx_psi = -1j*(Y*grad_z - Z*grad_y)*psi.conjugate()
    psi_Ly_psi = -1j*(Z*grad_x - X*grad_z)*psi.conjugate()

    Intgr_Lx_x = scint.simps(psi_Lx_psi, axis=0)
    Intgr_Lx_x_y = scint.simps(Intgr_Lx_x, axis=0)
    Intgr_Lx_x_y_z = scint.simps(Intgr_Lx_x_y, axis=0)

    Intgr_Ly_x = scint.simps(psi_Ly_psi, axis=0)
    Intgr_Ly_x_y = scint.simps(Intgr_Ly_x, axis=0)
    Intgr_Ly_x_y_z = scint.simps(Intgr_Ly_x_y, axis=0)

    Intgr_Lz_x = scint.simps(psi_Lz_psi, axis=0)
    Intgr_Lz_x_y = scint.simps(Intgr_Lz_x, axis=0)
    Intgr_Lz_x_y_z = scint.simps(Intgr_Lz_x_y, axis=0)

    print(Intgr_Lx_x_y_z)
    print(Intgr_Ly_x_y_z)
    print(Intgr_Lz_x_y_z)
