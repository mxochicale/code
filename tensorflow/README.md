# Tensorboard

## Hardware 
GPU: rtx 2070
OS: Ubuntu 20.04


## Nvidia drivers 
```
$ nvidia-smi
Fri Aug  6 21:36:11 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.57.02    Driver Version: 470.57.02    CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:01:00.0  On |                  N/A |
| N/A   58C    P8    10W /  N/A |    724MiB /  7973MiB |      2%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A       997      G   /usr/lib/xorg/Xorg                 35MiB |
|    0   N/A  N/A      1647      G   /usr/lib/xorg/Xorg                235MiB |
|    0   N/A  N/A      1773      G   /usr/bin/gnome-shell               41MiB |
|    0   N/A  N/A      2240      G   /usr/lib/firefox/firefox          332MiB |
|    0   N/A  N/A     14168      G   /usr/lib/firefox/firefox            1MiB |
|    0   N/A  N/A     25900      G   ..._19099.log --shared-files       64MiB |
+-----------------------------------------------------------------------------+
```

```
$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2021 NVIDIA Corporation
Built on Wed_Jul_14_19:41:19_PDT_2021
Cuda compilation tools, release 11.4, V11.4.100
Build cuda_11.4.r11.4/compiler.30188945_0
```
