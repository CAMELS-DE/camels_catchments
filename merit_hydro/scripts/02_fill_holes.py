from glob import glob
import geopandas as gpd
from shapely.geometry import Polygon


def fill_holes():
    """
    Fill holes in the catchment geometries.

    """
    # get all catchment files
    catchments = glob("/output_data/catchments/*.geojson")

    ids_hole = []

    # iterate over all catchment files
    for catchment in catchments:
        # get ID of catchment
        id = catchment.split("/")[-1].split(".")[0]

        # read catchment file
        gdf = gpd.read_file(catchment)

        # check for interiors -> holes
        if len(gdf.geometry.iloc[0].interiors) > 0:
            # use exterior coords to create a new polygon without holes
            new_geom = Polygon(gdf.exterior[0].coords)

            # replace the old geometry with the new geometry
            gdf["geometry"] = new_geom

            # save the new geometry to the output folder
            gdf.to_file(catchment, driver="GeoJSON")

            # append id to list
            ids_hole.append(id)

            
    print(f"Filled holes for IDs: {ids_hole}")


if __name__ == "__main__":
    fill_holes()