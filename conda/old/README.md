Anaconda [:link:](https://www.anaconda.com/)
---


# Installation 
Check the lastest version of Anaconda at https://repo.anaconda.com/archive/ (See more [ [1] (sep2018) ](https://www.ceos3c.com/open-source/install-anaconda-ubuntu-18-04/), [ [2] ](https://linuxhint.com/install_anaconda_python_ubuntu_1804/)).

```
cd ~/Downloads
wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh #04 November 2018 ## Length: 667822837 (637M) 
md5sum Anaconda3*.sh
bash Anaconda3*.sh #ENTER/yes/yes/no
source ~/.bashrc
#rm Anaconda3*.sh #don't delete in case of reinstallation
```

* verify installation 
```
conda info
conda --version
```


# Using virtual environments

* create an virtual environment
```
cd
conda create -n testing python=3.6 pip numpy #remember to initialize the env with pip here.
```


* activate the virtual environment
```
conda activate testing
```


* deactivate your tensorflow conda env 
```
conda deactivate
conda deactivate
```


* delete a no longer needed virtual environmnet
```
conda remove -n testing --all
```



# Learn more
* https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
* https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c





