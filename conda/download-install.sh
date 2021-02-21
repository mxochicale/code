## 01 Dependencies
sudo apt install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

## 02 Download 
cd Downloads
wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh

## 03 Verify hash 
sha256sum Anaconda3-2020.11-Linux-x86_64.sh
# Make sure the hash printed from the command above matches the one available at the Anaconda with Python 3 on 64-bit Linux page for your appropriate Anaconda version.
# https://docs.anaconda.com/anaconda/install/hashes/Anaconda3-2020.11-Linux-x86_64.sh-hash
# cf2ff493f11eaad5d09ce2b4feaa5ea90db5174303d5b3fe030e16d29aeef7de

## 04 Install
bash Anaconda3-2020.11-Linux-x86_64.sh

## 05 Source PATH 
source ~/.bashrc

## 06 Conda update
conda update --all


## 07 remove Download
cd Downloads
rm Anaconda3-2020.11-Linux-x86_64.sh



### Uninstalling Anaconda 
### rm -rf ~/anaconda3 ~/.condarc ~/.conda ~/.continuum
#### Open the ~/.bashrc file and remove the Anaconda directory from the PATH environment variable:



## References 
# https://linuxize.com/post/how-to-install-anaconda-on-ubuntu-20-04/
