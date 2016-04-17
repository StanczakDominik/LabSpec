import h5py

f = h5py.File("data.hdf5")
for key, item in f.items():
    print(key, item)
    # if key !="psi":
    #     f.__delitem__(key)
    # print(item[0])
for key, item in f.attrs.items():
    print(key, item)
    # if key not in ("XN, ZN, YN"):
    #     f.__delattr__(key)
    # psi = f.create_dataset("psi", data=np.load("psi.npy"))
    # gradx = f.create_dataset("gradx", data=np.load("gradx.npy"))
    # grady = f.create_dataset("grady", data=np.load("grady.npy"))
    # gradz = f.create_dataset("gradz", data=np.load("gradz.npy"))
    # currentsx = f.create_dataset("currentsx", data=np.load("currents_x.npy"))
    # currentsy = f.create_dataset("currentsy", data=np.load("currents_y.npy"))
    # currentsz = f.create_dataset("currentsz", data=np.load("currents_z.npy"))
