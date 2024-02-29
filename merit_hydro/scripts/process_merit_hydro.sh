#!/bin/bash
export PYTHONWARNINGS="ignore"

# make directories to store the output data if they do not exist
mkdir -p /output_data/catchments
mkdir -p /output_data/scripts

# logging
exec > >(tee -a /output_data/scripts/processing.log) 2>&1

# create outlets.csv from CAMELS metadata
echo "[$(date +%T)] Creating outlets.csv from CAMELS metadata..."
python /scripts/01_get_outlets.py
cp /scripts/01_get_outlets.py /output_data/scripts/01_get_outlets.py
echo "[$(date +%T)] Created outlets.csv from CAMELS metadata with 01_outlets.py"

# copy config.py from input_data to delineator
cp /input_data/config.py /delineator/config.py
echo "[$(date +%T)] Copied config.py from input_data to delineator."

# run delineator
echo "[$(date +%T)] Starting delineaton of MERIT HYDRO basins..."
cd /delineator && python delineate.py > /output_data/scripts/delineation.log 2>&1
echo "[$(date +%T)] Finished delineation of MERIT HYDRO basins, see delineation.log for details."

# fill potential holes in the delineated catchments
echo "[$(date +%T)] Filling holes in the delineated catchments..."
python /scripts/02_fill_holes.py
cp /scripts/02_fill_holes.py /output_data/scripts/02_fill_holes.py
echo "[$(date +%T)] Filled holes in the delineated catchments with 02_fill_holes.py"

# save the delineated catchments to camelsp stations
echo "[$(date +%T)] Saving the delineated catchments to CAMELS stations..."
python /scripts/03_add_catchments_to_stations.py
cp /scripts/03_add_catchments_to_stations.py /output_data/scripts/03_add_catchments_to_stations.py
echo "[$(date +%T)] Saved delineated catchments to CAMELS stations with 03_add_catchments_to_stations.py"

# select catchments based on criteria: inside of the borders of Germany (HYRAS availability), minimum area, maximum area, allowed difference to reported area
echo "[$(date +%T)] Adding station selection criteria to metadata..."
papermill /scripts/04_add_selection_criteria_to_metadata.ipynb /output_data/scripts/04_add_selection_criteria_to_metadata.ipynb -p min_years_of_q 10 -p min_area 5 -p max_area 15000 -p maximum_difference_to_reported_area 0.1 --no-progress-bar
echo "[$(date +%T)] Added station selection criteria to metadata with 04_add_selection_criteria_to_metadata.ipynb"

# copy scripts to /camelsp/output_data/scripts/catchments
mkdir -p /camelsp/output_data/scripts/catchments
cp /output_data/scripts/* /camelsp/output_data/scripts/catchments/

# change permissions of the output data
chmod -R 777 /camelsp/output_data/
chmod -R 777 /output_data/