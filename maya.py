import numpy as np
import mayavi.mlab as mlab

reshaped = np.abs(np.load("psi.npy"))**2

contour_plot = mlab.contour3d(reshaped, transparent=True, opacity=0.5, contours=10)
mlab.show()
