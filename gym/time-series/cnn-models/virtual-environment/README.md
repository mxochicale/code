

## Create Virtual Environment 
Using `env.yml` create an environment
```
conda deactivate
conda env create -f env.yml
conda activate timeseries
```

## Update env

```
conda env update --file env.yml  --prune
conda activate timeseries
```
"The --prune option causes conda to remove any dependencies that are no longer required from the environment."
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html


## Run environment 
Open a terminal and run: 
```
conda activate timeseries
```

