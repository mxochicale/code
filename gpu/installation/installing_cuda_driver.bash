
#Step 1: Thoroughly Remove Old NVIDIA Drivers
sudo apt-get remove --purge nvidia-* cuda-drivers* -y
sudo apt-get autoremove -y


#Step 2: Add the Official NVIDIA Repository
# Add the GPG key
sudo mkdir -p /usr/share/keyrings
curl -fsSL https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/3bf863cc.pub | sudo gpg --dearmor -o /usr/share/keyrings/cuda-archive-keyring.gpg

# Add the repository source
echo "deb [signed-by=/usr/share/keyrings/cuda-archive-keyring.gpg] https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/ /" | sudo tee /etc/apt/sources.list.d/cuda-ubuntu2404-x86_64.list

#Step 3: Update and Install the Correct Driver
sudo apt update


# List nvidia drivers
ubuntu-drivers list

# Install the open-source driver version
#sudo apt install -y nvidia-driver-550 #errors
sudo apt install -y nvidia-driver-580 #no errors

#Step 4: Reboot and Verify
#sudo reboot
#nvidia-smi


#nvidia-smi (before rebooting)
#Failed to initialize NVML: Driver/library version mismatch
#NVML library version: 580.173 



