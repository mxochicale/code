# Installation of CUDA Toolkit and cuDNN

1. Run bash in a terminal 

```bash
bash installing_cuda.bash
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

