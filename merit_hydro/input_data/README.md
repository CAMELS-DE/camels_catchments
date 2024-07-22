# MERIT Hydro catchment boundaries

## Description

MERIT Hydro was released by Yamazaki et al. (2019); providing a global hydrography dataset based on the MERIT DEM and various maps of water bodies (e.g. Global 3 arc-second Water Body Map, OpenStreetMap water layer; Yamazaki et al., 2017). It includes information such as flow direction, flow accumulation, adjusted elevations for hydrological purposes, and the width of river channels. The delineator.py package (Heberger, 2023) was used to delineate catchment boundaries. The method automatically derives catchment boundaries from the MERIT Hydro dataset based on the longitude and latitude of a gauging station and snaps the catchment pour point to the closest stream.

## Data retrieval for this repository

All input data to run delineator.py need to be added to the `input_data` directory.  
It is important to download the data that covers the area of Germany, for CAMELS-DE we need Pfafstetter Level 2 basin codes `[22, 23, 24]`.  
The following data is required:
- MERIT-Hydro raster data from https://mghydro.com/watersheds/rasters/ (flow accumulation and flow direction) -> save to `input_data/raster/accum_basins/` and `input_data/raster/flowdir_basins/`
- MERIT-Basins vector data from https://www.reachhydro.org/home/params/merit-basins (unit catchments and river flowline) -> save to `input_data/shp/merit_catchments/` and `input_data/shp/merit_rivers/`
- Simplified MERIT-Basins data from https://mghydro.com/watersheds/share/catchments_simplified.zip -> save and unzip to `input_data/shp/catchments_simplified/`

You can also refer to the explanations at the GitHub page of [delineator.py](https://github.com/mheberger/delineator) for more information on the input data.

As CAMELS-DE can also use catchments that are entirely located inside Germany, the official Borders of Germany geopacakge is also required to run the container:
- Download from https://daten.gdz.bkg.bund.de/produkte/vg/vg250_ebenen_0101/aktuell/vg250_01-01.utm32s.gpkg.ebenen.zip and save to `input_data/assets_criteria/` and unzip.

## Citation
- MERIT Hydro: https://doi.org/10.1029/2019WR024873
- delineator.py: https://doi.org/10.5281/zenodo.7314287
- Boundaries of Germany: © GeoBasis-DE / BKG (2024)