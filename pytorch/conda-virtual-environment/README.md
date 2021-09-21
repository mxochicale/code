# Create Conda Virtual Environment 

## Create (update, or delete) VE
* creation
```
bash install-ve.bash
```

* update VE
```
conda deactivate
conda update --all
conda update -n base -c defaults conda
conda env update --file ve.yml  --prune
conda activate pytorchVE
bash install-update-ve.bash
```

* remove VE
```
conda deactivate
conda remove --name pytorchVE --all
```

## Run env 
Open a terminal and run: 
```
conda activate $NAME_OF_VE
```


## References
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html  


