import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation as ani
from matplotlib import rcParams
rcParams['font.family'] = 'DejaVu Sans'
import h5py

def animate_density(save=False):
    with h5py.File("data.hdf5") as f:
        Xmin = f.attrs['Xmin']
        Xmax = f.attrs['Xmax']
        Ymin = f.attrs['Ymin']
        Ymax = f.attrs['Ymax']
        Zmin = f.attrs['Zmin']
        ZN = f.attrs['ZN']
        density = f['density'][...]
        z = f['Z'][0,0,:]
    fig, axes = plt.subplots()
    IM = axes.imshow(density[:,:,0], origin='upper', vmin=np.min(density), vmax=np.max(density), extent=(Xmin,Xmax,Ymin,Ymax))
    axes.set_title("Przekrój w płaszczyźnie z")
    text = axes.text(0.95*Xmin, 0.9*Ymax, "z = {}".format(Zmin), color=(1,1,1,1))
    axes.set_xlabel("x")
    axes.set_ylabel("y")

    def init():
        text.set_text("")
        IM.set_array(density[:,:,0])
        return IM, text
    def animate(i):
        IM.set_array(density[:,:,i])
        text.set_text("z = {}".format(z[i]))
        return IM, text

    fig.colorbar(IM, orientation="vertical")
    anim = ani.FuncAnimation(fig, animate, interval=10, frames=ZN, blit=True, init_func=init)
    if save:
        anim.save("grafika/animation_density.mp4", fps=30, extra_args=['-vcodec', 'libx264'])
    plt.show()

if __name__ == "__main__":
    animate_density(save=True)
