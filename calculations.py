# -*- coding: utf-8 -*-
from __future__ import print_function
import numpy as np
import h5py
import scipy.fftpack as fft
import scipy.integrate as scint

def calculate_all(nz_slices = 50, slice = 20):
    with h5py.File("data.hdf5", "a") as f:
        nx, ny, nz = f.attrs['XN'], f.attrs['YN'], f.attrs['ZN']

        if 'X' not in f:
            x = y = np.arange(-80,80)
            z = np.arange(-500,500)

            X, Y, Z = np.meshgrid(x,y,z)
            f.create_dataset('X', data=X)
            f.create_dataset('Y', data=Y)
            f.create_dataset('Z', data=Z)
        if 'KX' not in f or 'KY' not in f or 'KZ' not in f:
            print("Calculating k vectors")
            k_x = fft.fftfreq(nx, 1)
            k_y = fft.fftfreq(ny, 1)
            k_z = fft.fftfreq(nz, 1)
            KX, KY, KZ = np.meshgrid(k_x, k_y, k_z)
            f['KX'] = KX
            f['KY'] = KY
            f['KZ'] = KZ
        if 'density' not in f:
            psi = f['psi'][...]
            f['density'] = (psi*psi.conjugate()).real
        if 'psi_transform' not in f:
            print("FFTing wavefunction")
            f['psi_transform'] = fft.fftn(f['psi'][...])

        if 'gradx_fft' not in f:
            f.create_dataset('gradx_fft', shape=f['psi'].shape, dtype=f['psi'].dtype)
            f.create_dataset('grady_fft', shape=f['psi'].shape, dtype=f['psi'].dtype)
            f.create_dataset('gradz_fft', shape=f['psi'].shape, dtype=f['psi'].dtype)

            print("Calculating gradients transforms")
            for k in range(nz_slices):
                start = slice*k
                print(start)
                end = start + slice


                KX = f['KX'][:,:,start:end]
                KY = f['KY'][:,:,start:end]
                KZ = f['KZ'][:,:,start:end]
                psi_fft = f['psi_transform'][:,:,start:end]

                f['gradx_fft'][:,:,start:end] = psi_fft*1j*KX
                f['grady_fft'][:,:,start:end] = psi_fft*1j*KY
                f['gradz_fft'][:,:,start:end] = psi_fft*1j*KZ

        if 'gradx' not in f:
            print("Calculating Grad")
            f['gradx'] = fft.ifftn(f['gradx_fft'][...])
            f['grady'] = fft.ifftn(f['grady_fft'][...])
            f['gradz'] = fft.ifftn(f['gradz_fft'][...])

        calculate_currents = False
        if 'currentsx' not in f:
            f.create_dataset('currentsx', shape=f['psi'].shape, dtype=f['psi'][0,0,0].real.dtype)
            f.create_dataset('currentsy', shape=f['psi'].shape, dtype=f['psi'][0,0,0].real.dtype)
            f.create_dataset('currentsz', shape=f['psi'].shape, dtype=f['psi'][0,0,0].real.dtype)
            calculate_currents=True
            print("Calculating currents")
        calculate_L = False
        if 'Lx' not in f:
            f.create_dataset('Lx', shape=f['psi'].shape, dtype=f['currentsx'].dtype)
            f.create_dataset('Ly', shape=f['psi'].shape, dtype=f['currentsx'].dtype)
            f.create_dataset('Lz', shape=f['psi'].shape, dtype=f['currentsx'].dtype)
            calculate_L=True
            print("Calculating L")

        calculate_L_integrals = not 'Lx' in f.attrs
        if calculate_L_integrals:
            print("Integrating L")
        L_integral_total = np.zeros(3)

        for k in range(nz_slices):
            start = slice*k
            print(start)
            end = start + slice

            grad_x = f['gradx'][:,:,start:end]
            grad_y = f['grady'][:,:,start:end]
            grad_z = f['gradz'][:,:,start:end]
            psi = f['psi'][:,:,start:end]

            if calculate_currents:
                f['currentsx'][:,:,start:end] = \
                    ((psi.conjugate() * grad_x - psi*grad_x.conjugate())/(2j)).real
                f['currentsy'][:,:,start:end] = \
                    ((psi.conjugate() * grad_z - psi*grad_y.conjugate())/(2j)).real
                f['currentsz'][:,:,start:end] = \
                    ((psi.conjugate() * grad_z - psi*grad_z.conjugate())/(2j)).real
            if calculate_L:
                f['Lx'][:,:,start:end] = (-1j*(f['X'][:,:,start:end]*grad_y -\
                    f['Y'][:,:,start:end]*grad_x)*psi.conjugate()).real
                f['Ly'][:,:,start:end] = (-1j*(f['Y'][:,:,start:end]*grad_z -\
                    f['Z'][:,:,start:end]*grad_y)*psi.conjugate()).real
                f['Lz'][:,:,start:end] = (-1j*(f['Z'][:,:,start:end]*grad_x -\
                    f['X'][:,:,start:end]*grad_z)*psi.conjugate()).real
            if calculate_L_integrals:
                for index, direction in enumerate(("x", "y", "z")):
                    L = f['L' + direction][:,:,start:end]
                    Intgr_L_x = scint.simps(L, axis=0)
                    L_integral_total[index] += scint.simps(scint.simps(Intgr_L_x, axis=0), axis=0)
        if calculate_L_integrals:
            print("L integrals: {}".format(L_integral_total))
            Lx, Ly, Lz = L_integral_total
            f.attrs['Lx'] = Lx
            f.attrs['Ly'] = Ly
            f.attrs['Lz'] = Lz
if __name__ == "__main__":
    calculate_all()
