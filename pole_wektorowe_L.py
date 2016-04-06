# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:49:42 2016

@author: Mateusz
"""

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import h5py
nx = ny = 160
nz = 1000
dx = dy = dz = 1

x = y = np.arange(nx)
z = np.arange(nz)
X,Y,Z = np.meshgrid(x,y,z)
NX, NY, NZ = nx, ny, nz
X -= int(NX/2)
Y -= int(NY/2)
Z -= int(NZ/2)

with h5py.File("data.hdf5", "r+") as f:
    gradx_pointer = f['gradx']
    grady_pointer = f['grady']
    gradz_pointer = f['gradz']
    psi_pointer = f['psi']

    j = int(ny/2)
    X = X[j,:,:]
    Y = Y[j,:,:]
    Z = Z[j,:,:]
    grad_x = gradx_pointer[j,:,:]
    grad_y = grady_pointer[j,:,:]
    grad_z = gradz_pointer[j,:,:]
    psi = psi_pointer[j,:,:]
    Lz = (-1j*(X*grad_y - Y*grad_x)*psi.conjugate()).real
    Lx = (-1j*(Y*grad_z - Z*grad_y)*psi.conjugate()).real
    Ly = (-1j*(Z*grad_x - X*grad_z)*psi.conjugate()).real

    every_n_point = 2
    def thin(X):
        return X[::every_n_point, ::every_n_point]

    fig, (vector_ax, im_ax) = plt.subplots(2, figsize=(16,16))
    # Z, X, Lz, Lx = one_d_quantities
    vector_ax.quiver(thin(Z), thin(X), thin(Lz), thin(Lx), np.hypot(thin(Lx), thin(Lz)), scale_units='xy', scale=1e-7, angles='xy')
    # vector_ax.scatter(Z, X, np.hypot(Lx, Lz), cmap=cm.coolwarm, norm=)
    vector_ax.set_xlabel("z")
    vector_ax.set_ylabel("x")
    vector_ax.set_xlim(-500,500)
    vector_ax.set_ylim(-80,80)

    im_ax.imshow(np.hypot(Lx,Ly,Lz), extent=(-500,500,-80,80))
    plt.show()
