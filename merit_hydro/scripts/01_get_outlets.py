from camelsp import get_metadata
import numpy as np

def create_merit_hydro_outlets_csv():
    """
    Create a csv file with the outlets of the CAMELS basins. The csv file contains the following columns:
    - id: CAMELS id
    - lat: latitude
    - lng: longitude
    - name: name of the gauge
    - area: area of the basin in square kilometers

    The csv file is saved in the input_data folder.

    """

    # get CAMELS metadata
    meta = get_metadata()

    # select columns
    outlets = meta[["camels_id", "lat", "lon", "gauge_name", "area"]].copy()

    # rename columns
    outlets.columns = ["id", "lat", "lng", "name", "area"]

    # currently, not all rows are filled (e.g. some stations do not have lat and lon), remove those stations
    outlets = outlets.dropna(subset=["id", "lat", "lng"]).reset_index(drop=True)

    # save as csv
    outlets.to_csv('/output_data/outlets.csv', index=False)


if __name__ == "__main__":
    create_merit_hydro_outlets_csv()