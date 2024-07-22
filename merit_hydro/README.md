# MERIT Hydro catchment boundaries

## Description

Repository to delineate catchments for CAMELS-DE dataset using the MERIT Hydro dataset.  
The [Global Watersheds delineator](https://github.com/mheberger/delineator) (DOI: 10.5281/zenodo.7314287) is used to delineate MERIT Hydro catchments for all gauging stations in CAMELS-DE.  
Extracted catchment boundaries are copied to the camelsp `output_data` directory as a .geojson file for each station, where other tools process the data further and organize it in the folder structure.

## Container

### Build the container

```bash
docker build -t merit_hydro .
```

### Run the container

Necessary input data to run `delineator.py` needs to be added to the `input_data` directory, follow the instructions given in `input_data/README.md`.

To run the container, the local `input_data`, `output_data` and `camelsp/output_data` directories have to be mounted inside the container:

```bash
docker run -v ./input_data:/input_data -v ./output_data:/output_data -v /path/to/local/camelsp/output_data:/camelsp/output_data -it --rm merit_hydro
```

## Output

The output is a .geojson file for each station containing its delineated catchment boundary.