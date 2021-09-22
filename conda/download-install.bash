## 00 Welcome
echo "Hi $USER"
echo "This is a bash script to install conda in your LINUX/GNU machine"
echo "USAGE:"
echo "bash download-installation.bash"
echo " "

## 01 Dependencies
sudo apt install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

## 02 Download 
cd ~/Downloads
# Check latest version: https://repo.anaconda.com/archive/
#ANACONDA_VERSION = Anaconda3-2020.11-Linux-x86_64.sh
ANACONDA_VERSION="Anaconda3-5.3.1-Linux-x86_64.sh"
LINK=https://repo.anaconda.com/archive/$ANACONDA_VERSION
wget $LINK

### 03 Verify hash 
sha256sum $ANACONDA_VERSION
## Make sure the hash printed from the command above matches the one available at the Anaconda with Python 3 on 64-bit Linux page for your appropriate Anaconda version.
## https://docs.anaconda.com/anaconda/install/hashes/Anaconda3-2020.11-Linux-x86_64.sh-hash
## cf2ff493f11eaad5d09ce2b4feaa5ea90db5174303d5b3fe030e16d29aeef7de

## 04 Install
bash $ANACONDA_VERSION

## 05 Source PATH 
source ~/.bashrc

## Remove Download
cd ~/Downloads
rm $ANACONDA_VERSION

## References 
# https://linuxize.com/post/how-to-install-anaconda-on-ubuntu-20-04/
