# Creating virtual environments

## Sort of automatic creation 

### Creation
Using `ve.yml` create an environment
```
conda deactivate
conda update --all 
#conda env create -f ve-cpu.yml
#conda env create -f ve-gpu.yml
conda activate $VE
```

### Update env
```
#conda env update --file ve-cpu.yml --prune
#conda env update --file ve-gpu.yml --prune
```
"The --prune option causes conda to remove any dependencies that are no longer required from the environment."
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html


### Run env 
Open a terminal and run: 
```
conda activate $NAME_OF_VENV
```


* delete a no longer needed virtual environmnet
```
conda deactivate
conda remove -n pytorch-ve --all
```

## Test pytorch with CUDA
``` 
conda activate pytorch-ve
python
import torch
torch.cuda.is_available()
```

## Learn more
* https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
* https://medium.freecodecamp.org/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c


## CUDA versions 
* do you have cuda?
```
$which nvcc
/usr/local/cuda/bin/nvcc
```
* which version of CUDA?
``` 
$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Wed_Oct_23_19:24:38_PDT_2019
Cuda compilation tools, release 10.2, V10.2.89
```
* CUDA driver version
```
$ cat /proc/driver/nvidia/version
NVRM version: NVIDIA UNIX x86_64 Kernel Module  460.39  Thu Jan 21 21:54:06 UTC 2021
GCC version:  gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04) 
```
* Check GPU card and driver version 
```
$ nvidia-smi
Mon May 17 02:22:33 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.39       Driver Version: 460.39       CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce RTX 2070    Off  | 00000000:01:00.0  On |                  N/A |
| N/A   59C    P8     8W /  N/A |    378MiB /  7973MiB |     20%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1293      G   /usr/lib/xorg/Xorg                 18MiB |
|    0   N/A  N/A      1353      G   /usr/bin/gnome-shell               69MiB |
|    0   N/A  N/A      1744      G   /usr/lib/xorg/Xorg                143MiB |
|    0   N/A  N/A      1906      G   /usr/bin/gnome-shell              140MiB |
|    0   N/A  N/A     25835      G   ..._15641.log --shared-files        2MiB |
+-----------------------------------------------------------------------------+
``` 


