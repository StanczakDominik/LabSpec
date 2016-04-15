import numpy as np
import h5py
import mayavi.mlab as mlab


with h5py.File("data.hdf5") as f:
    density = f['density'][...]

for i in (4,):
    contour_plot = mlab.contour3d(density, transparent=True, opacity=0.5, contours=i)
    mlab.show()
