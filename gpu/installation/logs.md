# LOGS
## Add data in vim using :r !date
* CUDA VERSION
* system
```
uname -m
lsb_release -a
```

* bash installing_cuda.bash
* Check versions
```
nvidia-smi
nvcc -V
```

* bash installation_cudNN.bash 

* Packages size
cuda-repo-ubuntu2204....
cudnn-local-repo-ubuntu2204....


## Sat Dec  6 06:22:11 AM GMT 2025

```
$ uname -m
x86_64
$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 24.04.3 LTS
Release:	24.04
Codename:	noble
```

```
nvidia-smi 
Sat Dec  6 06:21:32 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX 2000 Ada Gene...    On  |   00000000:01:00.0 Off |                  N/A |
| N/A   38C    P8              1W /   35W |      15MiB /   8188MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A            3028      G   /usr/lib/xorg/Xorg                        4MiB |
+-----------------------------------------------------------------------------------------+
```

```
$ nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2025 NVIDIA Corporation
Built on Wed_Aug_20_01:58:59_PM_PDT_2025
Cuda compilation tools, release 13.0, V13.0.88
Build cuda_13.0.r13.0/compiler.36424714_0
```


* Before driver installation
```bash
dpkg -l | grep nvidia  # For Ubuntu/Debian

#with 
#nvidia-smi 
#NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.

ii  libnvidia-cfg1-550:amd64                      550.120-0ubuntu0.24.04.1                 amd64        NVIDIA binary OpenGL/GLX configuration library
ii  libnvidia-common-550                          550.120-0ubuntu0.24.04.1                 all          Shared files used by the NVIDIA libraries
ii  libnvidia-compute-550:amd64                   550.120-0ubuntu0.24.04.1                 amd64        NVIDIA libcompute package
ii  libnvidia-container-tools                     1.18.1-1                                 amd64        NVIDIA container runtime library (command-line tools)
ii  libnvidia-container1:amd64                    1.18.1-1                                 amd64        NVIDIA container runtime library
ii  libnvidia-decode-550:amd64                    550.120-0ubuntu0.24.04.1                 amd64        NVIDIA Video Decoding runtime libraries
ii  libnvidia-egl-wayland1:amd64                  1:1.1.13-1build1                         amd64        Wayland EGL External Platform library -- shared library
ii  libnvidia-encode-550:amd64                    550.120-0ubuntu0.24.04.1                 amd64        NVENC Video Encoding runtime library
ii  libnvidia-extra-550:amd64                     550.120-0ubuntu0.24.04.1                 amd64        Extra libraries for the NVIDIA driver
ii  libnvidia-fbc1-550:amd64                      550.120-0ubuntu0.24.04.1                 amd64        NVIDIA OpenGL-based Framebuffer Capture runtime library
ii  libnvidia-gl-550:amd64                        550.120-0ubuntu0.24.04.1                 amd64        NVIDIA OpenGL/GLX/EGL/GLES GLVND libraries and Vulkan ICD
ii  linux-modules-nvidia-550-6.11.0-17-generic    6.11.0-17.17~24.04.2+1                   amd64        Linux kernel nvidia modules for version 6.11.0-17
ii  linux-modules-nvidia-550-generic-hwe-24.04    6.11.0-17.17~24.04.2+1                   amd64        Extra drivers for nvidia-550 for the generic-hwe-24.04 flavour
ii  linux-objects-nvidia-550-6.11.0-17-generic    6.11.0-17.17~24.04.2+1                   amd64        Linux kernel nvidia modules for version 6.11.0-17 (objects)
ii  linux-signatures-nvidia-6.11.0-17-generic     6.11.0-17.17~24.04.2+1                   amd64        Linux kernel signatures for nvidia modules for version 6.11.0-17-generic
ii  nvidia-compute-utils-550                      550.120-0ubuntu0.24.04.1                 amd64        NVIDIA compute utilities
ii  nvidia-container-toolkit                      1.18.1-1                                 amd64        NVIDIA Container toolkit
ii  nvidia-container-toolkit-base                 1.18.1-1                                 amd64        NVIDIA Container Toolkit Base
ii  nvidia-driver-550                             550.120-0ubuntu0.24.04.1                 amd64        NVIDIA driver metapackage
ii  nvidia-firmware-550-550.120                   550.120-0ubuntu0.24.04.1                 amd64        Firmware files used by the kernel module
ii  nvidia-kernel-common-550                      550.120-0ubuntu0.24.04.1                 amd64        Shared files used with the kernel module
ii  nvidia-kernel-source-550                      550.120-0ubuntu0.24.04.1                 amd64        NVIDIA kernel source package
ii  nvidia-prime                                  0.8.17.2                                 all          Tools to enable NVIDIA's Prime
ii  nvidia-settings                               510.47.03-0ubuntu4                       amd64        Tool for configuring the NVIDIA graphics driver
ii  nvidia-utils-550                              550.120-0ubuntu0.24.04.1                 amd64        NVIDIA driver support binaries
ii  screen-resolution-extra                       0.18.3                                   all          Extension for the nvidia-settings control panel
ii  xserver-xorg-video-nvidia-550                 550.120-0ubuntu0.24.04.1                 amd64        NVIDIA binary Xorg driver
```

* After driver installation
```
$ dpkg -l | grep nvidia  # For Ubuntu/Debian
ii  libnvidia-cfg1-550:amd64                        550.163.01-0ubuntu0.24.04.2              amd64        NVIDIA binary OpenGL/GLX configuration library
ii  libnvidia-cfg1-580:amd64                        580.95.05-0ubuntu1                       amd64        NVIDIA binary OpenGL/GLX configuration library
ii  libnvidia-common-550                            550.163.01-0ubuntu0.24.04.2              all          Shared files used by the NVIDIA libraries
ii  libnvidia-common-580                            580.95.05-0ubuntu1                       all          Shared files used by the NVIDIA libraries
ii  libnvidia-compute-550:amd64                     550.163.01-0ubuntu0.24.04.2              amd64        NVIDIA libcompute package
ii  libnvidia-compute-580:amd64                     580.95.05-0ubuntu1                       amd64        NVIDIA libcompute package
ii  libnvidia-container-tools                       1.18.1-1                                 amd64        NVIDIA container runtime library (command-line tools)
ii  libnvidia-container1:amd64                      1.18.1-1                                 amd64        NVIDIA container runtime library
ii  libnvidia-decode-550:amd64                      550.163.01-0ubuntu0.24.04.2              amd64        NVIDIA Video Decoding runtime libraries
ii  libnvidia-decode-580:amd64                      580.95.05-0ubuntu1                       amd64        NVIDIA Video Decoding runtime libraries
ii  libnvidia-egl-gbm1:amd64                        1.1.2.1-1ubuntu1                         amd64        GBM EGL external platform library for NVIDIA
ii  libnvidia-egl-wayland1:amd64                    1:1.1.20-1ubuntu1                        amd64        Wayland EGL External Platform library -- shared library
ii  libnvidia-egl-xcb1:amd64                        1.0.3-1ubuntu1                           amd64        This is an EGL platform library for the NVIDIA driver to support
ii  libnvidia-egl-xlib1:amd64                       1.0.3-1ubuntu1                           amd64        This is an EGL platform library for the NVIDIA driver to support
ii  libnvidia-encode-550:amd64                      550.163.01-0ubuntu0.24.04.2              amd64        NVENC Video Encoding runtime library
ii  libnvidia-encode-580:amd64                      580.95.05-0ubuntu1                       amd64        NVENC Video Encoding runtime library
ii  libnvidia-extra-550:amd64                       550.163.01-0ubuntu0.24.04.2              amd64        Extra libraries for the NVIDIA Server Driver
ii  libnvidia-extra-580:amd64                       580.95.05-0ubuntu1                       amd64        Extra libraries for the NVIDIA driver
ii  libnvidia-fbc1-550:amd64                        550.163.01-0ubuntu0.24.04.2              amd64        NVIDIA OpenGL-based Framebuffer Capture runtime library
ii  libnvidia-fbc1-580:amd64                        580.95.05-0ubuntu1                       amd64        NVIDIA OpenGL-based Framebuffer Capture runtime library
ii  libnvidia-gl-550:amd64                          550.163.01-0ubuntu0.24.04.2              amd64        NVIDIA OpenGL/GLX/EGL/GLES GLVND libraries and Vulkan ICD
ii  libnvidia-gl-580:amd64                          580.95.05-0ubuntu1                       amd64        NVIDIA OpenGL/GLX/EGL/GLES GLVND libraries and Vulkan ICD
ii  libnvidia-gpucomp-580:amd64                     580.95.05-0ubuntu1                       amd64        NVIDIA binary GPU compiler library
ii  linux-modules-nvidia-580-open-6.14.0-36-generic 6.14.0-36.36~24.04.1+1                   amd64        Linux kernel nvidia modules for version 6.14.0-36
ii  linux-modules-nvidia-580-open-generic-hwe-24.04 6.14.0-36.36~24.04.1+1                   amd64        Extra drivers for nvidia-580-open for the generic-hwe-24.04 flavour
ii  linux-objects-nvidia-550-6.11.0-17-generic      6.11.0-17.17~24.04.2+1                   amd64        Linux kernel nvidia modules for version 6.11.0-17 (objects)
ii  linux-objects-nvidia-580-6.14.0-36-generic      6.14.0-36.36~24.04.1+1                   amd64        Linux kernel nvidia modules for version 6.14.0-36 (objects)
ii  linux-signatures-nvidia-6.11.0-17-generic       6.11.0-17.17~24.04.2+1                   amd64        Linux kernel signatures for nvidia modules for version 6.11.0-17-generic
ii  linux-signatures-nvidia-6.14.0-36-generic       6.14.0-36.36~24.04.1+1                   amd64        Linux kernel signatures for nvidia modules for version 6.14.0-36-generic
iF  nvidia-dkms-580-open                            580.95.05-0ubuntu1                       amd64        NVIDIA DKMS package (open kernel module)
iU  nvidia-driver-580-open                          580.95.05-0ubuntu1                       amd64        NVIDIA driver (open kernel) metapackage
ii  nvidia-firmware-580                             580.95.05-0ubuntu1                       amd64        Firmware files used by the kernel module
ii  nvidia-kernel-common-580                        580.95.05-0ubuntu1                       amd64        Shared files used with the kernel module
ii  nvidia-kernel-source-580-open                   580.95.05-0ubuntu1                       amd64        NVIDIA kernel source package
ii  nvidia-modprobe                                 580.95.05-0ubuntu1                       amd64        Load the NVIDIA kernel driver and create device files
ii  nvidia-persistenced                             580.95.05-0ubuntu1                       amd64        daemon to maintain persistent software state in the NVIDIA driver
ii  nvidia-settings                                 580.95.05-0ubuntu1                       amd64        Tool for configuring the NVIDIA graphics driver
ii  screen-resolution-extra                         0.18.3ubuntu0.24.04.1                    all          Extension for the nvidia-settings control panel
ii  xserver-xorg-video-nvidia-550                   550.163.01-0ubuntu0.24.04.2              amd64        NVIDIA binary Xorg driver
ii  xserver-xorg-video-nvidia-580                   580.95.05-0ubuntu1                       amd64        NVIDIA binary Xorg driver

```


```
$ ubuntu-drivers devices
udevadm hwdb is deprecated. Use systemd-hwdb instead (displayed 10x)
== /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0 ==
modalias : pci:v000010DEd000028B8sv00001028sd00000CC8bc03sc00i00
vendor   : NVIDIA Corporation
model    : AD107GLM [RTX 2000 Ada Generation Laptop GPU]
driver   : nvidia-driver-570-server - distro non-free
driver   : nvidia-driver-570-server-open - distro non-free
driver   : nvidia-driver-535 - distro non-free
driver   : nvidia-driver-580-open - third-party non-free recommended
driver   : nvidia-driver-580-server - distro non-free
driver   : nvidia-driver-570 - distro non-free
driver   : nvidia-driver-535-server - distro non-free
driver   : nvidia-driver-535-open - distro non-free
driver   : nvidia-driver-580 - third-party non-free
driver   : nvidia-driver-580-server-open - distro non-free
driver   : nvidia-driver-570-open - distro non-free
driver   : nvidia-driver-535-server-open - distro non-free
driver   : xserver-xorg-video-nouveau - distro free builtin

== /sys/devices/pci0000:00/0000:00:1f.4 ==
modalias : pci:v00008086d00007E22sv00001028sd00000CC8bc0Csc05i00
vendor   : Intel Corporation
model    : Meteor Lake-P SMBus Controller
driver   : oem-somerville-magmar-meta - third-party free

== /sys/devices/pci0000:00/0000:00:05.0 ==
modalias : pci:v00008086d00007D19sv00001028sd00000CC8bc04sc80i00
vendor   : Intel Corporation
driver   : intel-ipu6-dkms - distro free
driver   : libcamhal-ipu6epmtl - third-party free
```


## Sat Sep  6 12:33:18 PM BST 2025: 13.0.1
* Before installation
```
nvidia-smi
Sat Sep  6 12:38:38 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.120                Driver Version: 550.120        CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA RTX 2000 Ada Gene...    Off |   00000000:01:00.0 Off |                  N/A |
| N/A   35C    P0            588W /   35W |       9MiB /   8188MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A      2358      G   /usr/lib/xorg/Xorg                              4MiB |
+-----------------------------------------------------------------------------------------+
```

* Installation
Length: 4035438226 (3.8G) [application/x-deb]
Saving to: ‘cuda-repo-ubuntu2404-13-0-local_13.0.1-580.82.07-1_amd64.deb’

```
nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2025 NVIDIA Corporation
Built on Wed_Aug_20_01:58:59_PM_PDT_2025
Cuda compilation tools, release 13.0, V13.0.88
Build cuda_13.0.r13.0/compiler.36424714_0
```






## Tue 27 Aug 18:32:54 BST 2024
cuda 12.6
Length: 3355715790 (3.1G) [application/x-deb]

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





