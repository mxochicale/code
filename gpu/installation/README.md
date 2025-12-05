# Installation of CUDA Toolkit and cuDNN

1. Run bash in a terminal 

```bash
bash installing_cuda.bash
```

1.1 Install the NVIDIA Container Toolkit:
```bash
bash install-nvidia-container-toolkit.bash
```

1.2 Verify NVIDIA Container Toolkit
```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
#docker rmi --force <ID>
#docker system prune -f --volumes
```


2. Reboot device

3. Remove package
```bash
~/Desktop/$CUDA_REPO_PKG
```

4. Check versions
```bash
nvidia-smi
nvcc -V
```

5. cuDNN Installation
```bash
bash installation_cudNN.bash
```

6. Logs
* See [logs.md](logs.md)


## Notes
* "nvidia-smi shows the highest version of CUDA supported by your driver.
nvcc -V shows the version of the current CUDA installation.
As long as your driver-supported version is higher than your installed version, it's fine.
You can even have several versions of CUDA installed at the same time." [ https://stackoverflow.com/questions/53422407 ]

* $ubuntu-drivers devices
```bash
udevadm hwdb is deprecated. Use systemd-hwdb instead.
== /sys/devices/pci0000:00/0000:00:01.0/0000:01:00.0 ==
modalias : pci:v0000
vendor   : NVIDIA Corporation
model    : AD107GLM [RTX 2000 Ada Generation Laptop GPU]
driver   : nvidia-driver-535-server-open - distro non-free
driver   : nvidia-driver-570-open - distro non-free
driver   : nvidia-driver-575-server-open - distro non-free
driver   : nvidia-driver-535-open - distro non-free
driver   : nvidia-driver-550 - distro non-free
driver   : nvidia-driver-535-server - distro non-free
driver   : nvidia-driver-570-server - distro non-free
driver   : nvidia-driver-580 - third-party non-free recommended
driver   : nvidia-driver-570 - distro non-free
driver   : nvidia-driver-575-server - distro non-free
driver   : nvidia-driver-570-server-open - distro non-free
driver   : nvidia-driver-550-open - distro non-free
driver   : nvidia-driver-575 - distro non-free
driver   : nvidia-driver-535 - distro non-free
driver   : nvidia-driver-575-open - distro non-free
driver   : nvidia-driver-580-open - third-party non-free
driver   : xserver-xorg-video-nouveau - distro free builtin
```

Check drivers
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

## References  
https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html  
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_local    
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local   
https://askubuntu.com/questions/882385/dev-sda1-clean-this-message-appears-after-i-startup-my-laptop-then-it-w
Install NVIDIA drivers and CUDA for Ubuntu 18.04 LTS  [https://gist.github.com/jmrf/4e2d57a2e5f58e103593fb608de14852]


## Uninstall
```
bash uninstall.bash
```

