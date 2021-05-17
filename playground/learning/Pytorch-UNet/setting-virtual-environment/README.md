# Creating virtual environments

## Sort of automatic creation 

### Creation
Using `ve.yml` create an environment
```
conda deactivate
conda update --all 
conda env create -f ve.yml
conda activate pytorch-ve
```

### Update env
```
conda activate quantum-ve
conda env update --file ve.yml --prune
conda activate $NAME_OF_VENV
```
"The --prune option causes conda to remove any dependencies that are no longer required from the environment."
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

or

bash 


### Run env 
Open a terminal and run: 
```
conda activate $NAME_OF_VENV
```


* delete a no longer needed virtual environmnet
```
conda remove -n $NAME_OF_VENV --all
```


## Learn more
* https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
* https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c


