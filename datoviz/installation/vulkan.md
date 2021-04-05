# Vulkan

## Install the latest Lunarg Vulkan SDK (tarball SDK),


## download vulkan

```
mkdir ~/vulkan && cd ~/vulkan
```
download 
```
# vulkansdk-linux-x86_64-1.2.170.0.tar.gz (206MB)
1.2.170.0: 26-Feb-2021	
c1e4b6e624479273383c892a946f8ab7fcb888d4a8809d157276fb9448f01f0d
https://vulkan.lunarg.com/sdk/home#linux
wget https://vulkan.lunarg.com/sdk/home#sdk/downloadConfirm/1.2.170.0/linux/vulkansdk-linux-x86_64-1.2.170.0.tar.gz
```

## untar and install
```
tar -xf vulkansdk-linux-x86_64-1.2.170.0.tar.gz
cd 1.2.170.0/
```

## Source vulkan

```
source ~/vulkan/1.2.170.0/setup-env.sh
```
or add this onto the .bashrc
```
## source vulkna
source ~/vulkan/1.2.170.0/setup-env.sh
```
ref: https://vulkan.lunarg.com/doc/sdk/1.2.170.0/linux/getting_started.html

## test

* Vulkan Installation Analyzer (VIA) with the command:
~$ vkvia`
* Vulkan Info with the command:
`~$ vulkaninfo`
* Vulkan Cube with the command:
`~$ vkcube`




## Reference
https://vulkan.lunarg.com/sdk/home#linux

