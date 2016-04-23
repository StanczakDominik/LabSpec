import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'DejaVu Sans'
import h5py
from matplotlib import animation

def animate_quiver(save=False):
    with h5py.File("data.hdf5") as f:
        x_min = 40
        x_max = 120
        z_min = 500
        z_max = 600
        y_min = 0
        y_max = 160
        X = f['X'][:,x_min:x_max,z_min:z_max]
        Z = f['Z'][:,x_min:x_max,z_min:z_max]
        Y = f['Y'][:,0,0]
        Currents_z = f['currentsz'][:,x_min:x_max,z_min:z_max]
        Currents_y = f['currentsy'][:,x_min:x_max,z_min:z_max]
        Currents_x = f['currentsx'][:,x_min:x_max,z_min:z_max]

    lengths_2d = np.hypot(Currents_x,Currents_z)
    arrows_values = np.hypot(lengths_2d,Currents_y)
    arrows_horizontal = Currents_z/lengths_2d
    arrows_vertical = Currents_x/lengths_2d


    every_n_point = 1
    def thin(X):
        """optional reduction of number of arrows on plot"""
        return X[::every_n_point, ::every_n_point]

    fig, vector_ax = plt.subplots(figsize=(8,8))

    initial_y = 80
    text = vector_ax.text(0.90*np.min(Z), 0.9*np.min(X), "y = {}".format(initial_y),
        color=(0,0,0,1))
    vector_ax.set_title(u"Prądy w płaszczyźnie x-z")
    vector_ax.grid()
    quiver = vector_ax.quiver(thin(Z[initial_y]), thin(X[initial_y]),
        thin(arrows_horizontal[initial_y]), thin(arrows_vertical[initial_y]),
        thin(arrows_values[initial_y]), scale_units='xy', scale=1, angles='xy',
        alpha=0.9, clim=(np.min(arrows_values), np.max(arrows_values)))
    vector_ax.set_xlabel(u"z")
    vector_ax.set_ylabel(u"x")
    quiver_zeroes = thin(np.zeros_like(Z[0]))
    def init():
        text.set_text("y = ")
        quiver.set_UVC(quiver_zeroes, quiver_zeroes, quiver_zeroes)
        return text, quiver

    if save:
        plt.savefig("grafika/quiver.png")
    def animate(i):
        text.set_text("y = {}".format(Y[i]))
        quiver.set_UVC(thin(arrows_horizontal[i]), thin(arrows_vertical[i]), thin(arrows_values[i]))
        return text, quiver
    anim = animation.FuncAnimation(fig, animate, frames=np.arange(y_min, y_max), interval=10, blit=True, init_func = init)
    if save:
        anim.save("grafika/animation_quiver.mp4", fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()
if __name__ == "__main__":
    animate_quiver(save=True)
