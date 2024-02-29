import pandas as pd
import geopandas as gpd
from camelsp import get_metadata, Station


def add_catchments_to_stations():
    """
    Add the catchment geometries to the stations in the camelsp
    folder structure.
    
    """
    # get CAMELS metadata
    meta = get_metadata()

    # create a list of camels ids
    camels_ids = meta["camels_id"].tolist()

    # save catchment geometries to stations
    for camels_id in camels_ids:
        try:
            # initiate Station
            s = Station(camels_id)

            # read geojson file
            gdf = gpd.read_file(f"/output_data/catchments/{camels_id}.geojson")

            # save geojson to Station output folder
            s.save_catchment_geometry(gdf, datasource='merit_hydro', if_exists='replace')

        except Exception as e:
            print(f"{camels_id} --- Error: {e}")


if __name__ == "__main__":
    add_catchments_to_stations()
