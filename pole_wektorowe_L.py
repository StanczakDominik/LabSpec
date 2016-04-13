# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:49:42 2016

@author: Mateusz
"""

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import rcParams
rcParams['font.family'] = 'Comic Sans MS'
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

with h5py.File("../data.hdf5", "r+") as f:
    j = int(ny/2)
    x_min = 40
    x_max = 120
    z_min = 500
    z_max = 600
    X = X[j,x_min:x_max,z_min:z_max]
    Y = Y[j,x_min:x_max,z_min:z_max]
    Z = Z[j,x_min:x_max,z_min:z_max]
    print(X, Y, Z, sep='\n')
    Currents_z = f['currentsz'][j,x_min:x_max,z_min:z_max].real
    Currents_y = f['currentsy'][j,x_min:x_max,z_min:z_max].real
    Currents_x = f['currentsx'][j,x_min:x_max,z_min:z_max].real
    print(Currents_x.shape, np.min(Currents_x), np.max(Currents_x), np.mean(Currents_x))
    every_n_point = 1
    def thin(X):
        return X[::every_n_point, ::every_n_point]

    fig, vector_ax = plt.subplots(figsize=(8,8))
    vector_ax.set_title("Prądy w płaszczyźnie $x-z$, przekrój w połowie osi $y$")
    vector_ax.grid()
    vector_ax.quiver(thin(Z), thin(X), thin(Currents_z/np.hypot(Currents_x,Currents_z)), thin(Currents_x/np.hypot(Currents_x,Currents_z)), thin(np.hypot(Currents_x, Currents_y, Currents_z)), scale_units='xy', scale=1, angles='xy', alpha=0.9)
    vector_ax.set_xlabel("$z$")
    vector_ax.set_ylabel("$x$")
    plt.savefig("wektor.png")
    plt.savefig("wektor.pdf")
    plt.show()
