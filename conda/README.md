# Anaconda [:link:](https://www.anaconda.com/)

## Download the lastest version of conda 
* Check latest version: https://repo.anaconda.com/archive/
* Change version of anaconda

## 01 Installation in Ubuntu 18.04, 20.04, 22.04, 22.10 
In the terminal, enter: bash [download-install.sh](download-install.sh):
```
bash download-install.bash
```

During the installation:


```

Welcome to Anaconda3 $YEAR

In order to continue the installation process, please review the license
agreement.
Please, press ENTER to continue
>>> 


Do you accept the license terms? [yes|no]
[no] >>> yes



Anaconda3 will now be installed into this location:
/home/mxochicale/anaconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/mxochicale/anaconda3] >>> [PRESS ENTER]

installation finished.
Do you wish the installer to initialize Anaconda3
by running conda init? [yes|no]
[no] >>> yes


```

Open and close terminal


## 02 Update conda 
```
conda update -n base -c defaults conda
```

* auto deactivation
conda config --set auto_activate_base false



## 03 Deactivate conda base

### (Suggested) auto deactivation
```
conda config --set auto_activate_base false
```
https://github.com/stereolabs/zed-ros-wrapper/issues/569#issuecomment-780035597


### (Optional) Deactivate/actiavet conda base from the bashrc

Comment and uncomment the following lines in `.bashrc`:

```

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/mx19/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/mx19/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/mx19/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/mx19/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

```



```
## 05 Source PATH 
source ~/.bashrc
```


## Path of installation
```
Anaconda3 will now be installed into this location:
$HOME/anaconda3
```


## Uninstalling Anaconda  
```
rm -rf ~/anaconda3 ~/.condarc ~/.conda ~/.continuum
#### Open the ~/.bashrc file and remove the Anaconda directory from the PATH environment variable:
```


