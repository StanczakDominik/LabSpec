import numpy as np
import h5py


nx = ny = 160
nz = 1000
dx = dy = dz = 1

x = y = np.arange(0, nx*dx, dx) - nx/2
z = np.arange(0, nz*dz, dz) - nz/2
X,Y,Z = np.meshgrid(x,y,z)
print(Z.dtype)

with h5py.File("data.hdf5") as f:
    # for name, data in (('X', X), ('Y', Y), ('Z', Z)):
        # f.create_dataset(name, data=data)
        # f.attrs[name + "min"] = np.min(data)
        # f.attrs[name + "max"] = np.max(data)
    for name, data in (('X', x), ('Y', y), ('Z', z)):
        f.attrs[name + "N"] = len(data)
    for i, v in f.attrs.items():
        print(i, v)
