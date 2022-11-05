## Instructions
### 1. Explore http://developer.download.nvidia.com/compute/cuda/repos/ to find your OS and arquitecuter 
### 2. Manually update version variables 
### 3. Run it: bash installing_cuda.bash

cd ~/Downloads

## CUDA 
CUDA_URL=https://developer.download.nvidia.com/compute/cuda
CUDA_VERSION=11.8.0

## REPO with UBUNTU VERSION
#CUDA_REPO_PKG=cuda-repo-ubuntu1804_10.2.89-1_amd64.deb
#CUDA_REPO_PKG=cuda-repo-ubuntu2004-11-4-local_11.4.2-470.57.02-1_amd64.deb
CUDA_REPO_PKG=cuda-repo-ubuntu2204-11-8-local_$CUDA_VERSION-520.61.05-1_amd64.deb

wget $CUDA_URL/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget $CUDA_URL/$CUDA_VERSION/local_installers/$CUDA_REPO_PKG
sudo dpkg -i $CUDA_REPO_PKG  
#sudo apt-key add /var/cuda-repo-ubuntu2004-11-4-local/7fa2af80.pub
sudo cp /var/cuda-repo-ubuntu2204-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings
sudo apt-get update
sudo apt-get -y install cuda

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


## REBOOT MACHINE00

### Installs all CUDA Toolkit packages required to develop CUDA applications. Does not include the driver.
#sudo apt install nvidia-cuda-toolkit


## Remove package
rm $CUDA_REPO_PKG
