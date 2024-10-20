import h5py
import numpy as np


def resave_catalog(catalog_name, output_name):
    # Load the original .mat file
    with h5py.File(catalog_name, "r") as catalog:
        # Extract the arrays and cast them as needed, keeping their original shape
        in_dr9 = catalog["in_dr9"][:].astype(np.bool_)
        in_dr10 = catalog["in_dr10"][:].astype(np.bool_)
        z_qsos = catalog["z_qsos"][:]
        filter_flags = catalog["filter_flags"][:]
        thing_ids = catalog["thing_ids"][:].astype(np.int64)

        # Save the extracted arrays to a new HDF5 file
        with h5py.File(output_name, "w") as new_catalog:
            new_catalog.create_dataset("in_dr9", data=in_dr9)
            new_catalog.create_dataset("in_dr10", data=in_dr10)
            new_catalog.create_dataset("z_qsos", data=z_qsos)
            new_catalog.create_dataset("filter_flags", data=filter_flags)
            new_catalog.create_dataset("thing_ids", data=thing_ids)


# Example usage
catalog_name = "catalog.mat"  # Replace with the path to the original catalog
output_name = "new_catalog.mat"  # Replace with the path for the new HDF5 file
resave_catalog(catalog_name, output_name)
