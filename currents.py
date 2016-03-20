import numpy as np
nx = ny = 160
nz = 1000
dx = dy = dz = 1

x = y = np.arange(0, nx*dx, dx)
z = np.arange(0, nz*dz, dz)
X,Y,Z = np.meshgrid(x,y,z)

psi = np.load("psi.npy")
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

import scipy.fftpack as fft
psi_transform = fft.fftn(psi)
k_x = fft.fftfreq(nx, dx)
k_y = fft.fftfreq(ny, dy)
k_z = fft.fftfreq(nz, dz)
KX, KY, KZ = np.meshgrid(k_x, k_y, k_z)

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
currents_x = np.load("currents_x.npy")

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
currents_y = np.load("currents_y.npy")

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
currents_z = np.load("currents_z.npy")

# density = np.abs(psi)**2
# np.save("density", density)
density = np.load("density.npy")

velocity_x = currents_x/density
velocity_y = currents_y/density
velocity_z = currents_z/density

# loop = np.array([[0,ny/2,0], [0,ny/2,nz], [nx/2, ny/2, nz], [nx/2, ny/2, 0], [0,ny/2, 0]])


from scipy.integrate import simps
# z_min, z_max = 400, 650
# integral_1 = simps(velocity_z[0,ny/2,z_min:z_max], dx=dz)
# integral_2 = simps(velocity_x[0:nx/2+1, ny/2, z_max], dx=dx)
# integral_3 = simps(velocity_z[nx/2,ny/2,z_min:z_max], dx=-dz)
# integral_4 = simps(velocity_x[0:nx/2+1, ny/2, z_min], dx=-dx)
z_int = 550
integral_1 = simps(velocity_x[:,0,z_int], dx=dx)
integral_2 = simps(velocity_y[-1,:,z_int], dx=dy)
integral_3 = simps(velocity_x[:,-1,z_int], dx=-dx)
integral_4 = simps(velocity_y[0,:,z_int], dx=-dy)
total = integral_1 + integral_2 + integral_3 + integral_4
print(integral_1, integral_2, integral_3, integral_4, total, total/2/np.pi, sep="\n")










#
# every_X_vector = 3
# X=X[::every_X_vector,::every_X_vector,::every_X_vector]
# Y=Y[::every_X_vector,::every_X_vector,::every_X_vector]
# Z=Z[::every_X_vector,::every_X_vector,::every_X_vector]
# psi = psi[::every_X_vector,::every_X_vector,::every_X_vector]
# density=density[::every_X_vector,::every_X_vector,::every_X_vector]
#
# np.save("disp_X", X)
# np.save("disp_Y", Y)
# np.save("disp_Z", Z)
# np.save("disp_psi", psi)
# np.save("disp_density", density)

# currents_x = np.load("currents_x.npy")
# gradx = np.load("gradx.npy")
# gradx=gradx[::every_X_vector,::every_X_vector,::every_X_vector]
# currents_x=currents_x[::every_X_vector,::every_X_vector,::every_X_vector]
# np.save("disp_gradx", gradx)
# np.save("disp_currentsx", currents_x)
#
# grady = np.load("grady.npy")
# currents_y =np.load("currents_y.npy")
# grady=grady[::every_X_vector,::every_X_vector,::every_X_vector]
# currents_y=currents_y[::every_X_vector,::every_X_vector,::every_X_vector]
# np.save("disp_grady", grady)
# np.save("disp_currentsy", currents_y)
#
# gradz = np.load("gradz.npy")
# currents_z = np.load("currents_z.npy")
# gradz=gradz[::every_X_vector,::every_X_vector,::every_X_vector]
# currents_z=currents_z[::every_X_vector,::every_X_vector,::every_X_vector]
# np.save("disp_gradz", gradz)
# np.save("disp_currentsz", currents_z)
