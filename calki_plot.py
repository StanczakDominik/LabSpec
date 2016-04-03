# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 13:46:50 2016

@author: Mateusz
"""
import numpy as np
import h5py as h5
import scipy.integrate as scint
import matplotlib.pyplot as matpl

with h5.File('data.hdf5', 'r') as f:
    calki = f['calki'][:,:].T
    x, y, z = calki
    Lx, Ly, Lz = scint.simps(calki, axis=1)
    print(Lx, Ly, Lz, Lx+Ly+Lz)
    fig,(axes) = matpl.subplots(figsize=(12,8))
    axes.plot(x, label="Lx")
    axes.plot(y, label="Ly")
    axes.plot(z, label="Lz")
    axes.plot(x+y+z, label="L")
    axes.set_xlabel('x')
    axes.set_ylabel('L')    
    y_lim = 0.0000001
    axes.set_ylim(-y_lim,y_lim)
    axes.grid()
    axes.legend()    
    matpl.show()
    
    
     