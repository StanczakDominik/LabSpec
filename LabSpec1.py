import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fft

def f(x):
    return np.exp(-x*x)

def pochodna(x):
    return -2*x*f(x)
def drugapochodna(x):
    return -2*f(x) + 4*x*x*f(x)

def norm2(vec1, vec2):
    return np.sum(np.abs(vec1-vec2))/np.sum(np.abs(vec1))
    # return np.sqrt(np.abs(np.sum((vec1-vec2)**2)/np.sum(vec1**2)))

fig, axes = plt.subplots()
N = 1000 #liczba
Nvec = np.arange(4,1000,1)
x, dx = np.linspace(-5, 5, N, retstep=True)
f0 = f(x)
f1 = pochodna(x)
f2 = drugapochodna(x)
axes.plot(x, f0, "b-", label="funkcja")
axes.plot(x, f1, "c-", label="pochodna")
axes.plot(x, f2, "k-", label="druga pochodna")

relative_errors = np.zeros(len(Nvec), dtype=float)
relative_errors2 = np.zeros(len(Nvec), dtype=float)
for i, N in enumerate(Nvec):
    x, dx = np.linspace(-5, 5, N, retstep=True)
    f0 = f(x)
    f1 = pochodna(x)
    f2 = drugapochodna(x)
    fourier0 = fft.fft(f0)
    fourier_frequencies = fft.fftfreq(N, dx)
    fourier_step = fourier_frequencies[1]-fourier_frequencies[0]

    fourier1 = fourier0*(1j*fourier_frequencies)
    fourier2 = fourier1*(1j*fourier_frequencies)
    # fourier1[0] = 0+0j
    f1_z_fouriera = fft.ifft(fourier1)
    f1_z_fouriera *= np.max(f1)/np.max(f1_z_fouriera.real)
    f2_z_fouriera = fft.ifft(fourier2)
    f2_z_fouriera *= np.max(f2)/np.max(f2_z_fouriera.real)

    n1 = norm2(f1, f1_z_fouriera)
    # print(n1)
    relative_errors[i] = n1
    # print(relative_errors[i])
    relative_errors2[i] = norm2(f2, f2_z_fouriera)


    axes.plot(x, f1_z_fouriera, "r--", label="pochodna fourier")
    axes.plot(x, f2_z_fouriera, "g--", label="druga fourier")

plt.grid()
# plt.legend()
plt.show()

plt.loglog(Nvec, relative_errors, "bo-", label="pierwsza pochodna")
plt.loglog(Nvec, relative_errors2, "ro-", label="druga pochodna")
plt.legend()
plt.show()
# fig2, axes2 = plt.subplots()
#
# axes2.bar(fourier_frequencies, np.abs(fourier0), fourier_step)
# axes2.bar(fourier_frequencies, np.abs(fourier1), fourier_step, color=[1,0,0])
# axes2.set_xlim(-2,2)
plt.show()
