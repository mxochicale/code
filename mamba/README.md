# mamba
> The Fast Cross-Platform Package Manager

## Installation of mamba
1. install mamba
Download mamba 
```
cd ~/Downloads  
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh"

#82M Jun 29 07:28  Mambaforge-Linux-x86_64.sh
```

installation
```

bash Mambaforge-$(uname)-$(uname -m).sh

1. Do you accept the license terms? [yes|no]
[no] >>> 


2. Mambaforge will now be installed into this location:
/home/mxochicale/mambaforge

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/mxochicale/mambaforge] >>> 
PREFIX=/home/mxochicale/mambaforge



3. Do you wish the installer to initialize Mambaforge
by running conda init? [yes|no]
[no] >>> yes

4. If you'd prefer that conda's base environment not be activated on startup, 
   set the auto_activate_base parameter to false: 

conda config --set auto_activate_base false

5. Update base mamba 
 
mamba update -n base mamba


```




2. install mamba environment:

## install simpel mamba envirohment
```
mamba update -n base mamba
mamba create -n VE python=3.8 pip -c conda-forge
mamba activate VE
```

## Installation of mamba environmnets using yml
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


