# Creating virtual environments

## Sort of automatic creation 

### Creation
Using `ve.yml` create an environment
```
cd $HOME/x-files/code/playground/kalman-filter/code/python/create-virtual-environments
conda deactivate
conda env create -f ve.yml
conda activate $NAME_OF_VENV
```

### Update env
```
cd $HOME/x-files/code/playground/kalman-filter/code/python/create-virtual-environments
conda env update --file ve.yml  --prune
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

### List created VEs
Open a terminal and run: 
```
conda info --envs
```



### Delete env
Delete a no longer needed virtual environmnet
```
conda remove -n testing --all
```


## Learn more
* https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
* https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c


