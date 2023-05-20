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
#ANACONDA_VERSION="Anaconda3-5.3.1-Linux-x86_64.sh"
#ANACONDA_VERSION="Anaconda3-2022.05-Linux-x86_64.sh" # 658.8M 	2022-05-10 13:22:00 	a01150aff48fcb6fcd6472381652de04
#ANACONDA_VERSION="Anaconda3-5.3.1-Linux-x86_64.sh" 	#637.0M 	2018-11-19 13:38:46 	334b43d5e8468507f123dbfe7437078f
#ANACONDA_VERSION="Anaconda3-2022.05-Linux-x86_64.sh" #658.8M 	2022-05-10 13:22:00 	a7c0afe862f6ea19a596801fc138bde0463abcbce1b753e8d5c474b506a2db2d
#ANACONDA_VERSION="Anaconda3-2022.10-Linux-x86_64.sh" # 	737.6M 	2022-10-17 16:15:39 	e7ecbccbc197ebd7e1f211c59df2e37bc6959d081f2235d387e08c9026666acd


ANACONDA_VERSION="Anaconda3-2023.03-1-Linux-x86_64.sh" 
#860.6M	2023-04-24 12:41:05	95102d7c732411f1458a20bdf47e4c1b0b6c8a21a2edfe4052ca370aaae57bab
#on Sat 20 May 07:22:22 BST 2023

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
