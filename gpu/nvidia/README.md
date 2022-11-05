## Manual installation

### CUDA Toolkit
1. Run bash in a terminal 

```
bash installing_cuda.bash
```

2. Check versions
```
nvidia-smi
nvcc -V
```

3. Logs
* size of deb package
```
2.4G Aug 30 22:13 cuda-repo-ubuntu2004-11-4-local_11.4.2-470.57.02-1_amd64.deb
```
* Other [logs.md](logs.md)


4. References  
https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html  
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=20.04&target_type=deb_local    
https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local   


### GPU dependencies 
Ubuntu users working with GPU dependencies should pay attention to nvidia drivers of their machines as these should match with the conda version. 

For instance, I use this:
```
## Install NVIDIA drivers and CUDA for Ubuntu 18.04 LTS  [https://gist.github.com/jmrf/4e2d57a2e5f58e103593fb608de14852]
wget http://us.download.nvidia.com/XFree86/Linux-x86_64/440.100/NVIDIA-Linux-x86_64-440.100.run
sudo chmod +x NVIDIA-Linux-x86_64-440.100.run
```


After installation
```
## Add the following to the end of file [https://sh-tsang.medium.com/tutorial-cuda-v10-2-cudnn-v7-6-5-installation-ubuntu-18-04-3d24c157473f] 
export PATH=/usr/local/cuda/bin:$PATH  
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```

Run the ~/.bashrc again: `source /.bashrc`
Still not sure if cudnn are required by xononav but installed them


```
### download and copy cudnn depencies of cudnn-10.2-linux-x64-v8.1.0.77.tgz from [https://developer.nvidia.com/rdp/cudnn-download] [https://gist.github.com/Mahedi-61/2a2f1579d4271717d421065168ce6a73]
sudo cp cuda/include/cudnn*.h /usr/local/cuda/include 
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda/lib64 
sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*
```


## In case you need to install the  default drivers
```
sudo apt-get clean
sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoremove
sudo apt-get purge nvidia*
sudo apt-get remove --purge '^nvidia-.*'
sudo apt-get install ubuntu-desktop # 2. If the ubuntu-desktop package is removed, reinstall it
sudo ubuntu-drivers autoinstall
reboot
```

https://askubuntu.com/questions/882385/dev-sda1-clean-this-message-appears-after-i-startup-my-laptop-then-it-w




