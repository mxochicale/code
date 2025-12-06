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
#docker images
#docker rmi --force <ID> #ubuntu:latest
#docker system prune -f --volumes
```

2. Reboot device

3. Remove package
```bash
~/Desktop/$CUDA_REPO_PKG
```

4. Check versions and add them to logs
* nvidia-smi
```bash
nvidia-smi
nvcc -V
```
* nvcc -V
```bash
nvcc -V
```

* ubuntu-drivers devices
```bash
ubuntu-drivers devices
```

* dpkg -l | grep nvidia  # For Ubuntu/Debian
```bash
dpkg -l | grep nvidia  # For Ubuntu/Debian
```

6. Logs
* See [logs.md](logs.md)

5. cuDNN Installation
```bash
bash installation_cudNN.bash
```


## Notes
* "nvidia-smi shows the highest version of CUDA supported by your driver.
nvcc -V shows the version of the current CUDA installation.
As long as your driver-supported version is higher than your installed version, it's fine.
You can even have several versions of CUDA installed at the same time." [ https://stackoverflow.com/questions/53422407 ]

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

## Known errors

```
cuda-toolkit-13-0 is already the newest version (13.0.2-1).
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 libnvidia-gl-580 : Depends: libnvidia-egl-gbm1 (>= 1.1.2.1) but it is not going to be installed
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).


sudo apt --fix-broken install

The following additional packages will be installed:
  libnvidia-egl-gbm1
The following NEW packages will be installed:
  libnvidia-egl-gbm1



Error! Installation aborted.

Autoinstall on 6.14.0-36-generic failed for module(s) nvidia(6).

Error! One or more modules failed to install during autoinstall.
Refer to previous errors for more information.
run-parts: /etc/kernel/postinst.d/dkms exited with return code 1
dpkg: error processing package linux-image-6.14.0-36-generic (--configure):
 installed linux-image-6.14.0-36-generic package post-installation script subprocess returned error exit status 1
Errors were encountered while processing:
 nvidia-dkms-580-open
 nvidia-driver-580-open
 linux-image-6.14.0-36-generic
E: Sub-process /usr/bin/dpkg returned an error code (1)
W: Operation was interrupted before it could finish



```
