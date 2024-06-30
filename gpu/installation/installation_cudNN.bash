

# 1. CHECK VERSIONhttps://developer.nvidia.com/cudnn-downloads
	#OTHER VERSIONS https://developer.nvidia.com/rdp/cudnn-archive

cd ~/Downloads
cuDNN_version=9.1.1
DEB_PACKAGE=cudnn-local-repo-ubuntu2204-${cuDNN_version}_1.0-1_amd64.deb #Length: 1750279558 (1.6G) [application/x-deb]

wget https://developer.download.nvidia.com/compute/cudnn/${cuDNN_version}/local_installers/$DEB_PACKAGE -O $DEB_PACKAGE

# Installing using deb package
sudo dpkg -i $DEB_PACKAGE
sudo cp /var/cudnn-local-repo-ubuntu2204-${cuDNN_version}/cudnn-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cudnn

##To install for CUDA 12, perform the above configuration but install the CUDA 12 specific package:
sudo apt-get -y install cudnn-cuda-12

# copy the following files into the cuda toolkit directory.
sudo cp -P include/* /usr/local/cuda/include
sudo cp -P lib/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/lib64/libcudnn* 


rm $DEB_PACKAGE

#EXAMPLES
#sudo cp -P cuda/include/cudnn.h /usr/local/cuda-11.7/include
#sudo cp -P include/* /usr/local/cuda/include/
#sudo cp -P cuda/lib/libcudnn* /usr/local/cuda-11.7/lib64/
#sudo cp -P lib64/* /usr/local/cuda/lib64/
#sudo chmod a+r /usr/local/cuda-11.7/lib64/libcudnn*


### download and copy cudnn depencies of cudnn-10.2-linux-x64-v8.1.0.77.tgz from [https://developer.nvidia.com/rdp/cudnn-download] [https://gist.github.com/Mahedi-61/2a2f1579d4271717d421065168ce6a73]
#sudo cp cuda/include/cudnn*.h /usr/local/cuda/include 
#sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda/lib64 
#sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*




## REFERNCES
#https://medium.com/geekculture/install-cuda-and-cudnn-on-windows-linux-52d1501a8805#68ce


