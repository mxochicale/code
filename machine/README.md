# Machine features

## OS
```
$ hostnamectl

 Static hostname: --
       Icon name: computer-laptop
         Chassis: laptop
      Machine ID: --
         Boot ID: --
Operating System: Ubuntu 22.04.1 LTS              
          Kernel: Linux 5.15.0-56-generic
    Architecture: x86-64
 Hardware Vendor: --

```

## GPU
```
$ nvidia-smi -q

==============NVSMI LOG==============

Timestamp                                 : Sat Dec 17 13:27:52 2022
Driver Version                            : 520.61.05
CUDA Version                              : 11.8

Attached GPUs                             : 1
GPU 00000000:01:00.0
    Product Name                          : NVIDIA RTX A2000 8GB Laptop GPU
    Product Brand                         : NVIDIA RTX
    Product Architecture                  : Ampere

```

## Python and package versions
```
cd ~/repositories/mxochicale/code/conda/create-virtual-environments$ 
conda activate aiVE
python packages_versions.py 


python: 3.10.9 (main, Jan 11 2023, 15:21:40) [GCC 11.2.0]
torch: 1.13.1+cu117
torchvision: 0.14.1+cu117
functorch: 1.13.1+cu117
torch cuda_is_available: True
torch cuda version: 11.7
torch cuda.device_count  1
PIL: 9.4.0
```
