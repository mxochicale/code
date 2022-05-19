# Optical flow

## Conda environment 
Current [ve.yml](../../conda-virtual-environment/ve.yml) was migrated to [codeVE.yml](../../../conda/create-virtual-environments/codeVE.yml)


## Script 
```
cd $HOME/repositories/code/pytorch/examples/optical_flow
conda activate codeVE
jupyter notebook
```

## Issues

* ModuleNotFoundError: No module named 'torchvision.models.optical_flow'
```
This module is only present in torchvision >= 0.12.*, for which don't have a stable release yet. You are viewing the "master" documentation, which corresponds to our main branch. Two possible ways out here:

    Build torch and torchvision from source or install them from our nightly releases.
    Wait for another week, since torchvision == 0.12.0 is tentatively scheduled to be released on the 10th of March.
```
https://github.com/pytorch/vision/issues/5516

Sorted by updating torchvision >= 0.12.* in conda env 



## References
https://pytorch.org/vision/stable/auto_examples/plot_optical_flow.html



