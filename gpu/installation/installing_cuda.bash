## Instructions
### 1. Explore https://developer.nvidia.com/cuda-downloads to find your OS and arquitecuter 
### 2. Manually update version variables 
### 3. Run it: bash installing_cuda.bash

## CHANGING PATHS
cd ~/Downloads

## SETTING VARIABLES
CUDA_URL=https://developer.download.nvidia.com/compute/cuda
CUDA_VERSION_dots=12.5.0  #CUDA_VERSION=11.8.0
CUDA_VERSION_dashes=12-5
UBUNTU_VERSION=ubuntu2204

## REPO with UBUNTU VERSION
#CUDA_REPO_PKG=cuda-repo-ubuntu1804_10.2.89-1_amd64.deb
#CUDA_REPO_PKG=cuda-repo-ubuntu2004-11-4-local_11.4.2-470.57.02-1_amd64.deb
#CUDA_REPO_PKG=cuda-repo-$UBUNTU_VERSION-11-8-local_$CUDA_VERSION_dots-520.61.05-1_amd64.deb
#CUDA_REPO_PKG=cuda-repo-$UBUNTU_VERSION-11-8-local_$CUDA_VERSION_dots-520.61.05-1_amd64.deb
CUDA_REPO_PKG=cuda-repo-$UBUNTU_VERSION-$CUDA_VERSION_dashes-local_$CUDA_VERSION_dots-555.42.02-1_amd64.deb #Length: 3302514250 (3.1G) 

wget $CUDA_URL/repos/ubuntu2204/x86_64/cuda-$UBUNTU_VERSION.pin -O cuda-$UBUNTU_VERSION.pin 
sudo mv cuda-$UBUNTU_VERSION.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget $CUDA_URL/$CUDA_VERSION_dots/local_installers/$CUDA_REPO_PKG -O $CUDA_REPO_PKG
sudo dpkg -i $CUDA_REPO_PKG  

sudo cp /var/cuda-repo-$UBUNTU_VERSION-$CUDA_VERSION_dashes-local/cuda-*-keyring.gpg /usr/share/keyrings
sudo apt-get update
sudo apt-get -y install cuda-toolkit-$CUDA_VERSION_dashes

#Configuring Secure Boot ├──────────────────────────────────────────────────────────────────────────────────────────┐
#                                  
# Your system has UEFI Secure Boot enabled
# UEFI Secure Boot requires additional configuration to work with third-party drivers.
# The system will assist you in configuring UEFI Secure Boot. To permit the use of third-party drivers, 
# a new Machine-Owner Key (MOK) has been generated. This key now needs to be enrolled in your system's firmware.
# To ensure that this change is being made by you as an authorized user, and not by an attacker, 
# you must choose a password now and then confirm the change after reboot using the same password, in both the
# "Enroll MOK" and "Change Secure Boot state" menus that will be presented to you when this system reboots.
# If you proceed but do not confirm the password upon reboot, Ubuntu will still be able to boot on your system 
# but any hardware that requires third-party drivers to work correctly may not be usable.

##################################
#### Adding cuda paths to bashrc file [https://sh-tsang.medium.com/tutorial-cuda-v10-2-cudnn-v7-6-5-installation-ubuntu-18-04-3d24c157473f] 
#### You might need to check .bashrc to avoid duplication of cuda paths
{
echo ''
echo ''
echo '#============================================================'
echo '#'
echo '#  CUDA PATHS'
echo '#'
echo "export PATH=/usr/local/cuda/bin:${PATH}  "
echo "export LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH}  "
echo ''
echo ''
echo ''
} >> ~/.bashrc


## REBOOT MACHINE00

## Remove package
rm $CUDA_REPO_PKG
