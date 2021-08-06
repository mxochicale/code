# Creating virtual environments (VE)

## Creation VE
1. update base env: `conda update -n base -c defaults conda`
2. Using `venv.yml` create an environment
```
conda deactivate
conda env create -f venv.yml
conda activate $NAME_VE
```

## Update env
```
bash update-venv.bash
```

## Run env 
Open a terminal and run: 
```
conda activate $NAME_VE
```

## rename vitual environment
```
conda create --name new_name --copy --clone old_name
conda remove --name old_name --all # or its alias: `conda env remove --name old_name`
```

## list env
You can list all discoverable environments with `conda info --envs`.

## delete a no longer needed virtual environmnet
```
conda remove -n testing --all
```

## References 
* https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
* https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c
