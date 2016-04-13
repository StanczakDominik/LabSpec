with h5py.File(input,  "a") as f:
    f.__delitem__(datasetname)
