## :r !date
* CUDA VERSION
* system
```
uname -m
lsb_release -a
```



* bash installing_cuda.bash
```
...
```
* Check versions
```
nvidia-smi

nvcc -V

```

* bash installation_cudNN.bash 
```

```


* Packages size
cuda-repo-ubuntu2204....
cudnn-local-repo-ubuntu2204....



## Tue 27 Aug 18:32:54 BST 2024
cuda 12.6

* system
```

 uname -m
x86_64

lsb_release -a

No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.4 LTS
Release:	22.04
Codename:	jammy
```



* Check versions
```
nvidia-smi


Tue Aug 27 18:32:38 2024       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.28.03              Driver Version: 560.28.03      CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX A2000 8GB Lap...    Off |   00000000:01:00.0 Off |                  N/A |
| N/A   40C    P0              7W /   35W |      14MiB /   8192MiB |      5%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A      2426      G   /usr/lib/xorg/Xorg                              4MiB |
+-----------------------------------------------------------------------------------------+


nvcc -V

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Fri_Jun_14_16:34:21_PDT_2024
Cuda compilation tools, release 12.6, V12.6.20
Build cuda_12.6.r12.6/compiler.34431801_0
```




## Sun  2 Jun 16:44:38 BST 2024
CUDA Toolkit 12.5


* system
```

 uname -m
x86_64

lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 22.04.2 LTS
Release:	22.04
Codename:	jammy
```




* bash installing_cuda.bash
```

cuda-repo-ubuntu2204-12-5-local_12.5.0-555.42.02-1_a 100%[=====================================================================================================================>]   3.08G  2.41MB/s    in 9m 9s   


Get:1 file:/var/cuda-repo-ubuntu2204-12-5-local  InRelease [1,572 B]
Get:1 file:/var/cuda-repo-ubuntu2204-12-5-local  InRelease [1,572 B]
Hit:2 http://gb.archive.ubuntu.com/ubuntu jammy InRelease
Hit:3 http://gb.archive.ubuntu.com/ubuntu jammy-updates InRelease                                                                                                                                            
Hit:4 http://gb.archive.ubuntu.com/ubuntu jammy-backports InRelease                                                                                                                                               
Hit:5 http://security.ubuntu.com/ubuntu jammy-security InRelease                                                                                                                                                  
Get:6 file:/var/cuda-repo-ubuntu2204-12-5-local  Packages [40.9 kB]                                                                                                                                               
Hit:7 https://brave-browser-apt-release.s3.brave.com stable InRelease                           
Hit:8 https://download.docker.com/linux/ubuntu jammy InRelease      
Get:9 https://packages.microsoft.com/repos/vscode stable InRelease [3,594 B]
Hit:10 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease
Fetched 3,594 B in 1s (3,421 B/s)     
Reading package lists... Done
W: https://cloud.r-project.org/bin/linux/ubuntu/jammy-cran40/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libcmark-gfm-extensions0.29.0.gfm.3 libcmark-gfm0.29.0.gfm.3 libegl-mesa0:i386 libegl1:i386 libflashrom1 libftdi1-2 libgbm1:i386 libgles2:i386 libllvm13 libllvm13:i386 libnvidia-cfg1-520
  libnvidia-compute-520:i386 libnvidia-decode-520:i386 libnvidia-encode-520:i386 libnvidia-extra-520 libnvidia-fbc1-520:i386 libnvidia-gl-520:i386 libopengl0:i386 libvulkan1:i386 libwayland-client0:i386
  libwayland-server0:i386 libxcb-randr0:i386 mesa-vulkan-drivers:i386 pandoc-data
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  cuda-cccl-12-5 cuda-command-line-tools-12-5 cuda-compiler-12-5 cuda-crt-12-5 cuda-cudart-12-5 cuda-cudart-dev-12-5 cuda-cuobjdump-12-5 cuda-cupti-12-5 cuda-cupti-dev-12-5 cuda-cuxxfilt-12-5
  cuda-documentation-12-5 cuda-driver-dev-12-5 cuda-gdb-12-5 cuda-libraries-12-5 cuda-libraries-dev-12-5 cuda-nsight-12-5 cuda-nsight-compute-12-5 cuda-nsight-systems-12-5 cuda-nvcc-12-5 cuda-nvdisasm-12-5
  cuda-nvml-dev-12-5 cuda-nvprof-12-5 cuda-nvprune-12-5 cuda-nvrtc-12-5 cuda-nvrtc-dev-12-5 cuda-nvtx-12-5 cuda-nvvm-12-5 cuda-nvvp-12-5 cuda-opencl-12-5 cuda-opencl-dev-12-5 cuda-profiler-api-12-5
  cuda-sanitizer-12-5 cuda-toolkit-12-5-config-common cuda-toolkit-12-config-common cuda-tools-12-5 cuda-visual-tools-12-5 gds-tools-12-5 libcublas-12-5 libcublas-dev-12-5 libcufft-12-5 libcufft-dev-12-5
  libcufile-12-5 libcufile-dev-12-5 libcurand-12-5 libcurand-dev-12-5 libcusolver-12-5 libcusolver-dev-12-5 libcusparse-12-5 libcusparse-dev-12-5 libnpp-12-5 libnpp-dev-12-5 libnvfatbin-12-5
  libnvfatbin-dev-12-5 libnvjitlink-12-5 libnvjitlink-dev-12-5 libnvjpeg-12-5 libnvjpeg-dev-12-5 nsight-compute-2024.2.0 nsight-systems-2024.2.3
The following NEW packages will be installed
  cuda-cccl-12-5 cuda-command-line-tools-12-5 cuda-compiler-12-5 cuda-crt-12-5 cuda-cudart-12-5 cuda-cudart-dev-12-5 cuda-cuobjdump-12-5 cuda-cupti-12-5 cuda-cupti-dev-12-5 cuda-cuxxfilt-12-5
  cuda-documentation-12-5 cuda-driver-dev-12-5 cuda-gdb-12-5 cuda-libraries-12-5 cuda-libraries-dev-12-5 cuda-nsight-12-5 cuda-nsight-compute-12-5 cuda-nsight-systems-12-5 cuda-nvcc-12-5 cuda-nvdisasm-12-5
  cuda-nvml-dev-12-5 cuda-nvprof-12-5 cuda-nvprune-12-5 cuda-nvrtc-12-5 cuda-nvrtc-dev-12-5 cuda-nvtx-12-5 cuda-nvvm-12-5 cuda-nvvp-12-5 cuda-opencl-12-5 cuda-opencl-dev-12-5 cuda-profiler-api-12-5
  cuda-sanitizer-12-5 cuda-toolkit-12-5 cuda-toolkit-12-5-config-common cuda-toolkit-12-config-common cuda-tools-12-5 cuda-visual-tools-12-5 gds-tools-12-5 libcublas-12-5 libcublas-dev-12-5 libcufft-12-5
  libcufft-dev-12-5 libcufile-12-5 libcufile-dev-12-5 libcurand-12-5 libcurand-dev-12-5 libcusolver-12-5 libcusolver-dev-12-5 libcusparse-12-5 libcusparse-dev-12-5 libnpp-12-5 libnpp-dev-12-5 libnvfatbin-12-5
  libnvfatbin-dev-12-5 libnvjitlink-12-5 libnvjitlink-dev-12-5 libnvjpeg-12-5 libnvjpeg-dev-12-5 nsight-compute-2024.2.0 nsight-systems-2024.2.3
0 to upgrade, 60 to newly install, 0 to remove and 230 not to upgrade.


```

* Check versions
```
nvidia-smi
Sun Jun  2 16:50:57 2024       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.147.05   Driver Version: 525.147.05   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA RTX A200...  Off  | 00000000:01:00.0 Off |                  N/A |
| N/A   41C    P0    N/A /  35W |      5MiB /  8192MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      2182      G   /usr/lib/xorg/Xorg                  4MiB |
+-----------------------------------------------------------------------------+


nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Wed_Apr_17_19:19:55_PDT_2024
Cuda compilation tools, release 12.5, V12.5.40
Build cuda_12.5.r12.5/compiler.34177558_0
```


* bash installation_cudNN.bash 
```
cudnn-local-repo-ubuntu2204-9.1.1_1.0-1_amd64.deb    100%[======================>]   1.63G  5.47MB/s    in 4m 57s  

Get:1 file:/var/cuda-repo-ubuntu2204-12-5-local  InRelease [1,572 B]
Get:2 file:/var/cudnn-local-repo-ubuntu2204-9.1.1  InRelease [1,572 B]
Get:1 file:/var/cuda-repo-ubuntu2204-12-5-local  InRelease [1,572 B]
Get:2 file:/var/cudnn-local-repo-ubuntu2204-9.1.1  InRelease [1,572 B]
Hit:3 http://gb.archive.ubuntu.com/ubuntu jammy InRelease                                       
Get:4 http://gb.archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]                                                                                                                                        
Get:5 file:/var/cudnn-local-repo-ubuntu2204-9.1.1  Packages [3,106 B]                                                                                                                                             
Hit:6 https://download.docker.com/linux/ubuntu jammy InRelease                                                                                                                                                    
Get:7 https://packages.microsoft.com/repos/vscode stable InRelease [3,594 B]                                                                                                             
Hit:8 https://brave-browser-apt-release.s3.brave.com stable InRelease                                                                                  
Get:9 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]                                                                              
Hit:10 http://gb.archive.ubuntu.com/ubuntu jammy-backports InRelease                        
Hit:11 https://cloud.r-project.org/bin/linux/ubuntu jammy-cran40/ InRelease                 
Fetched 261 kB in 1s (227 kB/s)                                        
Reading package lists... Done
W: https://cloud.r-project.org/bin/linux/ubuntu/jammy-cran40/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libcmark-gfm-extensions0.29.0.gfm.3 libcmark-gfm0.29.0.gfm.3 libegl-mesa0:i386 libegl1:i386 libflashrom1 libftdi1-2 libgbm1:i386 libgles2:i386 libllvm13 libllvm13:i386 libnvidia-cfg1-520
  libnvidia-compute-520:i386 libnvidia-decode-520:i386 libnvidia-encode-520:i386 libnvidia-extra-520 libnvidia-fbc1-520:i386 libnvidia-gl-520:i386 libopengl0:i386 libvulkan1:i386 libwayland-client0:i386
  libwayland-server0:i386 libxcb-randr0:i386 mesa-vulkan-drivers:i386 pandoc-data
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  cudnn9 cudnn9-cuda-12 cudnn9-cuda-12-4 libcudnn9-cuda-12 libcudnn9-dev-cuda-12 libcudnn9-samples libcudnn9-static-cuda-12
The following NEW packages will be installed
  cudnn cudnn9 cudnn9-cuda-12 cudnn9-cuda-12-4 libcudnn9-cuda-12 libcudnn9-dev-cuda-12 libcudnn9-samples libcudnn9-static-cuda-12
0 to upgrade, 8 to newly install, 0 to remove and 230 not to upgrade.
Need to get 0 B/877 MB of archives.


Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Note, selecting 'cudnn9-cuda-12' instead of 'cudnn-cuda-12'
cudnn9-cuda-12 is already the newest version (9.1.1.17-1).
cudnn9-cuda-12 set to manually installed.
The following packages were automatically installed and are no longer required:
  libcmark-gfm-extensions0.29.0.gfm.3 libcmark-gfm0.29.0.gfm.3 libegl-mesa0:i386 libegl1:i386 libflashrom1 libftdi1-2 libgbm1:i386 libgles2:i386 libllvm13 libllvm13:i386 libnvidia-cfg1-520
  libnvidia-compute-520:i386 libnvidia-decode-520:i386 libnvidia-encode-520:i386 libnvidia-extra-520 libnvidia-fbc1-520:i386 libnvidia-gl-520:i386 libopengl0:i386 libvulkan1:i386 libwayland-client0:i386
  libwayland-server0:i386 libxcb-randr0:i386 mesa-vulkan-drivers:i386 pandoc-data
Use 'sudo apt autoremove' to remove them.
0 to upgrade, 0 to newly install, 0 to remove and 230 not to upgrade.
cp: cannot stat 'include/*': No such file or directory
cp: cannot stat 'lib/libcudnn*': No such file or directory
chmod: cannot access '/usr/local/cuda/lib64/libcudnn*': No such file or directory

```

* Packages size
3.1G May 15 20:03 cuda-repo-ubuntu2204-12-5-local_12.5.0-555.42.02-1_amd64.deb
1.7G May  2 00:46 cudnn-local-repo-ubuntu2204-9.1.1_1.0-1_amd64.deb





## Sat  5 Nov 17:02:01 GMT 2022

* Installation
```
...

Setting up cuda-libraries-dev-11-8 (11.8.0-1) ...
Setting up gcc (4:11.2.0-1ubuntu1) ...
Setting up dkms (2.8.7-2ubuntu2) ...
Setting up g++ (4:11.2.0-1ubuntu1) ...
update-alternatives: using /usr/bin/g++ to provide /usr/bin/c++ (c++) in auto mode
Setting up build-essential (12.9ubuntu3) ...
Setting up cuda-nvcc-11-8 (11.8.89-1) ...
Setting up nvidia-dkms-520 (520.61.05-0ubuntu1) ...
update-initramfs: deferring update (trigger activated)

A modprobe blacklist file has been created at /etc/modprobe.d to prevent Nouveau
from loading. This can be reverted by deleting the following file:
/etc/modprobe.d/nvidia-graphics-drivers.conf

A new initrd image has also been created. To revert, please regenerate your
initrd by running the following command after deleting the modprobe.d file:
`/usr/sbin/initramfs -u`

*****************************************************************************
*** Reboot your computer and verify that the NVIDIA graphics driver can   ***
*** be loaded.                                                            ***
*****************************************************************************

INFO:Enable nvidia
DEBUG:Parsing /usr/share/ubuntu-drivers-common/quirks/put_your_quirks_here
DEBUG:Parsing /usr/share/ubuntu-drivers-common/quirks/lenovo_thinkpad
DEBUG:Parsing /usr/share/ubuntu-drivers-common/quirks/dell_latitude
Loading new nvidia-520.61.05 DKMS files...
Building for 5.15.0-43-generic
Building for architecture x86_64
Building initial module for 5.15.0-43-generic
Can't load /var/lib/shim-signed/mok/.rnd into RNG
4047B7761D7F0000:error:12000079:random number generator:RAND_load_file:Cannot open file:../crypto/rand/randfile.c:106:Filename=/var/lib/shim-signed/mok/.rnd


```
* Versions

```

nvidia-smi
Sat Nov  5 17:11:54 2022       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 520.61.05    Driver Version: 520.61.05    CUDA Version: 11.8     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA RTX A200...  On   | 00000000:01:00.0 Off |                  N/A |
| N/A   47C    P8     3W /  N/A |      4MiB /  8192MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      2090      G   /usr/lib/xorg/Xorg                  4MiB |
+-----------------------------------------------------------------------------+



nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Wed_Sep_21_10:33:58_PDT_2022
Cuda compilation tools, release 11.8, V11.8.89
Build cuda_11.8.r11.8/compiler.31833905_0


```


* size of deb package
3.0G Sep 29 19:51 cuda-repo-ubuntu2204-11-8-local_11.8.0-520.61.05-1_amd64.deb



## Tue Sep 21 19:29:19 2021       
```
nvidia-smi
Tue Sep 21 19:29:19 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.63.01    Driver Version: 470.63.01    CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:01:00.0  On |                  N/A |
| N/A   55C    P8    21W /  N/A |    393MiB / 16116MiB |      3%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      3279      G   /usr/lib/xorg/Xorg                 35MiB |
|    0   N/A  N/A      8090      G   /usr/lib/xorg/Xorg                155MiB |
|    0   N/A  N/A      8219      G   /usr/bin/gnome-shell               41MiB |
|    0   N/A  N/A     10010      G   /usr/lib/firefox/firefox          140MiB |
|    0   N/A  N/A     12963      G   /usr/lib/firefox/firefox            3MiB |
|    0   N/A  N/A     13426      G   /usr/lib/firefox/firefox            3MiB |
+-----------------------------------------------------------------------------+
```


```
nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Sun_Jul_28_19:07:16_PDT_2019
Cuda compilation tools, release 10.1, V10.1.243
```



## Mon Feb  8 22:42:28 2021       
* Check versions
```
mx19@sie085-lap:~$ nvidia-smi
Mon Feb  8 22:42:28 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.100      Driver Version: 440.100      CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce RTX 207...  Off  | 00000000:01:00.0  On |                  N/A |
| N/A   48C    P8     6W /  N/A |    246MiB /  7973MiB |      6%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1357      G   /usr/lib/xorg/Xorg                            18MiB |
|    0      1417      G   /usr/bin/gnome-shell                          49MiB |
|    0      1811      G   /usr/lib/xorg/Xorg                            96MiB |
|    0      1968      G   /usr/bin/gnome-shell                          77MiB |
+-----------------------------------------------------------------------------+

mx19@sie085-lap:~$ nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Wed_Oct_23_19:24:38_PDT_2019
Cuda compilation tools, release 10.2, V10.2.89
```




## Thu Apr  8 00:23:34 2021       
```
mx19@sie085-lap:~$ nvidia-smi
Thu Apr  8 00:23:34 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.39       Driver Version: 460.39       CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce RTX 2070    Off  | 00000000:01:00.0  On |                  N/A |
| N/A   46C    P8     7W /  N/A |    259MiB /  7973MiB |      1%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1065      G   /usr/lib/xorg/Xorg                 18MiB |
|    0   N/A  N/A      1120      G   /usr/bin/gnome-shell               69MiB |
|    0   N/A  N/A      1523      G   /usr/lib/xorg/Xorg                124MiB |
|    0   N/A  N/A      1684      G   /usr/bin/gnome-shell               40MiB |
|    0   N/A  N/A      4205      G   /usr/lib/firefox/firefox            1MiB |
+-----------------------------------------------------------------------------+
mx19@sie085-lap:~$ nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Wed_Oct_23_19:24:38_PDT_2019
Cuda compilation tools, release 10.2, V10.2.89

```






## Tue Sep 21 19:29:19 2021       
```
nvidia-smi
Tue Sep 21 19:29:19 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.63.01    Driver Version: 470.63.01    CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:01:00.0  On |                  N/A |
| N/A   55C    P8    21W /  N/A |    393MiB / 16116MiB |      3%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      3279      G   /usr/lib/xorg/Xorg                 35MiB |
|    0   N/A  N/A      8090      G   /usr/lib/xorg/Xorg                155MiB |
|    0   N/A  N/A      8219      G   /usr/bin/gnome-shell               41MiB |
|    0   N/A  N/A     10010      G   /usr/lib/firefox/firefox          140MiB |
|    0   N/A  N/A     12963      G   /usr/lib/firefox/firefox            3MiB |
|    0   N/A  N/A     13426      G   /usr/lib/firefox/firefox            3MiB |
+-----------------------------------------------------------------------------+
```


```
nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Sun_Jul_28_19:07:16_PDT_2019
Cuda compilation tools, release 10.1, V10.1.243
```


* size of deb package
```
2.4G Aug 30 22:13 cuda-repo-ubuntu2004-11-4-local_11.4.2-470.57.02-1_amd64.deb
```




## Mon Feb  8 22:42:28 2021       
* Check versions
```
mx19@sie085-lap:~$ nvidia-smi
Mon Feb  8 22:42:28 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.100      Driver Version: 440.100      CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce RTX 207...  Off  | 00000000:01:00.0  On |                  N/A |
| N/A   48C    P8     6W /  N/A |    246MiB /  7973MiB |      6%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1357      G   /usr/lib/xorg/Xorg                            18MiB |
|    0      1417      G   /usr/bin/gnome-shell                          49MiB |
|    0      1811      G   /usr/lib/xorg/Xorg                            96MiB |
|    0      1968      G   /usr/bin/gnome-shell                          77MiB |
+-----------------------------------------------------------------------------+

mx19@sie085-lap:~$ nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Wed_Oct_23_19:24:38_PDT_2019
Cuda compilation tools, release 10.2, V10.2.89
```




## Thu Apr  8 00:23:34 2021       
```
mx19@sie085-lap:~$ nvidia-smi
Thu Apr  8 00:23:34 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.39       Driver Version: 460.39       CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce RTX 2070    Off  | 00000000:01:00.0  On |                  N/A |
| N/A   46C    P8     7W /  N/A |    259MiB /  7973MiB |      1%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1065      G   /usr/lib/xorg/Xorg                 18MiB |
|    0   N/A  N/A      1120      G   /usr/bin/gnome-shell               69MiB |
|    0   N/A  N/A      1523      G   /usr/lib/xorg/Xorg                124MiB |
|    0   N/A  N/A      1684      G   /usr/bin/gnome-shell               40MiB |
|    0   N/A  N/A      4205      G   /usr/lib/firefox/firefox            1MiB |
+-----------------------------------------------------------------------------+
mx19@sie085-lap:~$ nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Wed_Oct_23_19:24:38_PDT_2019
Cuda compilation tools, release 10.2, V10.2.89

```





