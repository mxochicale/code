<<<<<<< HEAD
# mamba
> The Fast Cross-Platform Package Manager

## Installation of mamba
1. install [conda](../conda)
=======
# mamba, The Fast Cross-Platform Package Manager

## Installation of mamba
1. install [conda](conda)
>>>>>>> 61c7822fced2cb13d6a9571ecf1b901d532be150
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


## References
https://github.com/mamba-org/mamba#additional-features  
https://mamba.readthedocs.io/en/latest/user_guide/mamba.html  
https://pythonspeed.com/articles/faster-conda-install/  
https://twitter.com/QuantStack   




