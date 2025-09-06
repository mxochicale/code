# Installation of CUDA Toolkit and cuDNN

1. Run bash in a terminal 

```
bash installing_cuda.bash
```

2. Reboot device

N. Remove package
```
~/Desktop/$CUDA_REPO_PKG
```

3. Check versions
```
nvidia-smi
nvcc -V
```

3. cuDNN Installation
```
bash installation_cudNN.bash
```

4. Logs
* See [logs.md](logs.md)


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

