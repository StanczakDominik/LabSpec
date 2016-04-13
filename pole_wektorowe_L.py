import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'DejaVu Sans'
import h5py

nx = ny = 160
nz = 1000
dx = dy = dz = 1
x = y = np.arange(nx)
z = np.arange(nz)
X,Y,Z = np.meshgrid(x,y,z)
NX, NY, NZ = nx, ny, nz
# X -= int(NX/2)
# Y -= int(NY/2)
# Z -= int(NZ/2)

with h5py.File("data.hdf5") as f:
    i = int(ny/2)
    x_min = 40
    x_max = 120
    z_min = 500
    z_max = 600
    nz = f.attrs['ZN']
    nx, ny = f.attrs['XN'], f.attrs['YN']

    X = f['X'][:,x_min:x_max,z_min:z_max]
    Z = f['Z'][:,x_min:x_max,z_min:z_max]
    Currents_z = f['currentsz'][:,x_min:x_max,z_min:z_max]
    Currents_y = f['currentsy'][:,x_min:x_max,z_min:z_max]
    Currents_x = f['currentsx'][:,x_min:x_max,z_min:z_max]
    lengths_2d = np.hypot(Currents_x,Currents_z)
    arrows_values = np.hypot(Currents_x,Currents_y,Currents_z)
    arrows_horizontal = Currents_z/lengths_2d
    arrows_vertical = Currents_x/lengths_2d

    fig, vector_ax = plt.subplots(figsize=(8,8))
    every_n_point = 1
    def thin(X):
        return X[::every_n_point, ::every_n_point]

    vector_ax.set_title(u"Prądy w płaszczyźnie x-z, przekrój w połowie osi y")
    vector_ax.grid()
    vector_ax.quiver(thin(Z[i, :, :]), thin(X[i, :, :]),
        thin(arrows_horizontal[i, :, :]), thin(arrows_vertical[i, :, :]),
        thin(arrows_values[i, :, :]), scale_units='xy', scale=1, angles='xy',
        alpha=0.9)
    vector_ax.set_xlabel(u"z")
    vector_ax.set_ylabel(u"x")
    plt.savefig("grafika/wektor.png")
    plt.show()
