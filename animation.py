import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation as ani
# %matplotlib notebook
# %matplotlib inline
nx = ny = 160
nz = 1000
dx = dy = dz = 1

x = y = np.arange(0, nx*dx, dx)
z = np.arange(0, nz*dz, dz)

# ODCZY DANYCH
data = np.load("loadeddata.npy")

# ZAPIS DANYCH Z TXT DO .NPY
# data = np.loadtxt("pythondata2")
# print(data, data.shape)
# np.save("loadeddata", data)

reshaped = np.reshape(data, (nx, ny, nz))
print(reshaped.shape)

fig, axes = plt.subplots()
IM = axes.imshow(reshaped[:,:,0], origin='upper', extent=(0,nx*dx,0,ny*dy))
axes.set_title("przekroj przez $n_y = ${}".format(nz/2))
axes.set_xlabel("$z$")
axes.set_ylabel("$x$")
def animate(i):
    IM.set_array(reshaped[:,:,i])
    axes.set_title("przekroj przez $n_y = ${}".format(i))
    return IM, axes

anim = ani.FuncAnimation(fig, animate, interval=10, frames=nz)
anim.save("video.mp4", fps=30, extra_args=['-vcodec', 'libx264'])

# plt.colorbar(orientation="horizontal")
plt.show()
