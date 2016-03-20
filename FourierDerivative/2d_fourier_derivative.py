import numpy as np
import scipy.fftpack as fft
import matplotlib.pyplot as plt
import matplotlib.cm as cm

N=100
x, dx = y, dy = np.linspace(-5, 5, N, retstep=True)
X, Y = np.meshgrid(x,y)
F = np.exp(-X**2-Y**2)

k_x = fft.fftfreq(N, dx)
k_y = fft.fftfreq(N, dy)
KX, KY = np.meshgrid(k_x, k_y)
F_k = fft.fftn(F)
FX_k = 1j*F_k*KX
FY_k = 1j*F_k*KY
FX = fft.ifftn(FX_k)
FY = fft.ifftn(FY_k)


fig, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7,ax8,ax9)) = plt.subplots(3, 3, sharex='col', sharey='row')

ax1.imshow(F_k.real)
ax4.imshow(F.real, cmap=cm.gray)

ax2.imshow(FX_k.real)
ax5.imshow(FX.real, cmap=cm.gray)
ax8.imshow(-2*X*F.real, cmap=cm.gray)

ax3.imshow(FY_k.real)
ax6.imshow(FY.real, cmap=cm.gray)
ax9.imshow(-2*Y*F.real, cmap=cm.gray)

plt.show()
