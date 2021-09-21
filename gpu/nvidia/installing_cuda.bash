# 1. Explore http://developer.download.nvidia.com/compute/cuda/repos/ to find your OS and arquitecuter 
# 
cd ~/Downloads

## CUDA URL
CUDA_URL=http://developer.download.nvidia.com/compute/cuda

## REPO with UBUNTU VERSION
#CUDA_REPO_PKG=cuda-repo-ubuntu1804_10.2.89-1_amd64.deb
CUDA_REPO_PKG=cuda-repo-ubuntu2004-11-4-local_11.4.2-470.57.02-1_amd64.deb

wget $CUDA_URL/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget $CUDA_URL/11.4.2/local_installers/$CUDA_REPO_PKG
sudo dpkg -i $CUDA_REPO_PKG  
sudo apt-key add /var/cuda-repo-ubuntu2004-11-4-local/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda

## Installs all CUDA Toolkit packages required to develop CUDA applications. Does not include the driver.
sudo apt install nvidia-cuda-toolkit


## Remove package
rm $CUDA_REPO_PKG
