# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:49:42 2016

@author: Mateusz
"""

from __future__ import print_function
import numpy as np
import h5py
import scipy.integrate as scint
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

calki_po_przekrojach = np.zeros(nz)
with h5py.File("data.hdf5", "r+") as f:
    gradx_pointer = f['gradx']
    grady_pointer = f['grady']
    gradz_pointer = f['gradz']
    psi_pointer = f['psi']
    for k in range(nz):
        print(k)
        grad_x = gradx_pointer[:,:,k]
        grad_y = grady_pointer[:,:,k]
        grad_z = gradz_pointer[:,:,k]
        psi = psi_pointer[:,:,k]
        psi_Lz_psi = (-1j*(X[:,:,k]*grad_y - Y[:,:,k]*grad_x)*psi.conjugate()).real
        psi_Lx_psi = (-1j*(Y[:,:,k]*grad_z - Z[:,:,k]*grad_y)*psi.conjugate()).real
        psi_Ly_psi = (-1j*(Z[:,:,k]*grad_x - X[:,:,k]*grad_z)*psi.conjugate()).real
        L = np.hypot(psi_Lz_psi, psi_Lx_psi, psi_Ly_psi)

        Intgr_L_x = scint.simps(L, axis=0)
        Intgr_L_x_y = scint.simps(L, axis=0)
        print(Intgr_L_x_y.dtype, Intgr_L_x_y.shape)

        calki_po_przekrojach[k] = Intgr_L_x_y.real
    calki_przekrojowe = f.create_dataset('calki_full', data=calki_po_przekrojach)
calki_full = scint.simps(calki_po_przekrojach, axis=0)
print(calki_full)