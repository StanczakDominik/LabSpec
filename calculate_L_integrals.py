# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:49:42 2016

@author: Mateusz
"""

from __future__ import print_function
import numpy as np
import h5py
import scipy.integrate as scint

def calculate_L_integrals():
    with h5py.File("data.hdf5", "a") as f:
        nz = f.attrs['ZN']
        N_z_step = 10
        calki = np.zeros(3)
        for k in range(int(nz/N_z_step)):
            print(k)
            for index, direction in enumerate(("x", "y", "z")):
                L = f['L' + direction][:,:,k*N_z_step:(k+1)*N_z_step]
                Intgr_L_x = scint.simps(L, axis=0)
                calki[index] += scint.simps(scint.simps(Intgr_L_x, axis=0), axis=0)
        print(calki)

if __name__=="__main__":
    calculate_L_integrals()
