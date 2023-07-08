# mamba
> The Fast Cross-Platform Package Manager

## Installation of mamba
1. install [conda](../conda)
2. install mamba:
```
conda update -n base -c defaults conda  ##UPDATE CONDA
conda install mamba -n base -c conda-forge ##INSTALL MAMBA in conda base env
mamba update -n base mamba ##UPDATE MAMBA
```

## Installation of mamba environmnets
```
mamba update -n base mamba
mamba env create -f *VE.yml
mamba activate *VE
mamba remove -n *VE --all
#Run 'mamba init' to be able to run mamba activate/deactivate
```

## Remove mamba


1. Any modifications to your shell rc files that were made by Miniforge:
```
conda init --reverse --dry-run
conda init --reverse
```


2. Remove the folder and all subfolders where the base environment for Miniforge was installed:
```
CONDA_BASE_ENVIRONMENT=$(conda info --base)
echo The next command will delete all files in ${CONDA_BASE_ENVIRONMENT}
rm -rf ${CONDA_BASE_ENVIRONMENT}
echo ${HOME}/.condarc will be removed if it exists
rm -f "${HOME}/.condarc"
```




## References
https://github.com/mamba-org/mamba#additional-features  
https://mamba.readthedocs.io/en/latest/user_guide/mamba.html  
https://pythonspeed.com/articles/faster-conda-install/  
https://twitter.com/QuantStack   
https://github.com/conda-forge/miniforge#uninstallation   


