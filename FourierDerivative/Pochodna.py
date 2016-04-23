import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fft
import matplotlib
matplotlib.rc("font", family="Comic Sans MS")

def f(x):
    return np.exp(-x*x)

def pochodna(x):
    return -2*x*f(x)
def drugapochodna(x):
    return -2*f(x) + 4*x*x*f(x)

def norm(vec1, vec2):
    return np.sum(np.abs(vec1-vec2))/np.sum(np.abs(vec1))

fig, axes = plt.subplots()
N = 1000
Nvec = np.logspace(1,3,100).astype(int)
x, dx = np.linspace(-5, 5, N, retstep=True)
f0 = f(x)
f1 = pochodna(x)
f2 = drugapochodna(x)
axes.plot(x, f0, "b-", label="$f(x)$", lw=3)
axes.plot(x, f1, "c-", label="$f'(x)$", lw=3)
axes.plot(x, f2, "k-", label="$f''(x)$", lw=3)

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

    n1 = norm(f1, f1_z_fouriera)
    # print(n1)
    relative_errors[i] = n1
    # print(relative_errors[i])
    relative_errors2[i] = norm(f2, f2_z_fouriera)


    axes.plot(x, f1_z_fouriera, "r--")
    axes.plot(x, f2_z_fouriera, "g--")
plt.legend()
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid()
plt.show()


plt.loglog(Nvec, relative_errors, "bo-", label="pierwsza pochodna")
plt.loglog(Nvec, relative_errors2, "ro-", label="druga pochodna")
plt.xlabel("Liczba punktow na siatce $N$")
plt.ylabel("Blad wzgledny (norma rzedu 1)")
plt.legend()
plt.grid()
plt.show()
