# camels_catchments
Repository to delineate / obtain, process and quality check catchments for the CAMELS-DE dataset.


## Merit Hydro
docker command:  
`docker run -v /home/alexd/Projekte/CAMELS/Github/camelsp/output_data_docker:/camelsp/output_data -v ./input_data:/input_data -v ./scripts:/scripts -v ./output_data:/output_data -it --rm merit_hydro`



In this repository, we use the [Global Watersheds delineator](https://github.com/mheberger/delineator) to delineate MERIT Hydro catchments for all measuring stations in `metadata.csv`.  

cite Global Watersheds delineator: 10.5281/zenodo.7314287 