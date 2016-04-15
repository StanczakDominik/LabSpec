# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:49:42 2016

@author: Mateusz
"""

from __future__ import print_function
import numpy as np
import h5py

def calculate_L():
    with h5py.File("data.hdf5", "a") as f:
        nx, ny, nz = f.attrs['XN'], f.attrs['YN'], f.attrs['ZN']
        X = f['X']
        Y = f['Y']
        Z = f['Z']
        gradx_pointer = f['gradx']
        grady_pointer = f['grady']
        gradz_pointer = f['gradz']
        psi_pointer = f['psi']
        Lx_pointer = f.create_dataset(name="Lx", shape=(nx,ny,nz), dtype=float)
        Ly_pointer = f.create_dataset(name="Ly", shape=(nx,ny,nz), dtype=float)
        Lz_pointer = f.create_dataset(name="Lz", shape=(nx,ny,nz), dtype=float)
        for k in range(nz):
            print(k)
            grad_x = gradx_pointer[:,:,k]
            grad_y = grady_pointer[:,:,k]
            grad_z = gradz_pointer[:,:,k]
            psi = psi_pointer[:,:,k]
            psi_Lz_psi = (-1j*(X[:,:,k]*grad_y - Y[:,:,k]*grad_x)*psi.conjugate()).real
            psi_Lx_psi = (-1j*(Y[:,:,k]*grad_z - Z[:,:,k]*grad_y)*psi.conjugate()).real            #czy na pewno X, Y, Z są dobrze dobrane? może to trzeba sprawdzić i zrobić jeszcze raz?
            psi_Ly_psi = (-1j*(Z[:,:,k]*grad_x - X[:,:,k]*grad_z)*psi.conjugate()).real
            Lx_pointer[:,:,k] = psi_Lx_psi
            Ly_pointer[:,:,k] = psi_Ly_psi
            Lz_pointer[:,:,k] = psi_Lz_psi

if __name__ == "__main__":
    calculate_L()
