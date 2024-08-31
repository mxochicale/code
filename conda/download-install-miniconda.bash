## USAGE
## Open terminal and type: 
## bash download-install-miniconda.bash ##70-ish MB of space

## 00 Welcome
echo "Hi $USER"
echo "This is a bash script to install miniconda in your LINUX/GNU machine"
echo "USAGE:"
echo "bash download-installation-miniconda.bash"
echo " "

## 00 Remove old version
rm -rf home/$USER/miniconda3
rm .condarc

## 01 Dependencies? not sure if still need it but will keep it
#sudo apt install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6


## 02 Download 
cd ~/Downloads
## Check latest version: 
## https://repo.anaconda.com/miniconda/
MINICONDA_VERSION="Miniconda3-latest-Linux-x86_64.sh" 

##LOGS
#71.0M	2023-02-07 21:27:22	32d73e1bc33fda089d7cd9ef4c1be542616bd8e437d1f77afeeaf7afdb019787
#62.7M	2019-01-02 10:05:14	f387eded3fa4ddc3104b7775e62d59065b30205c2758a8b86b4c27144adafcc4 on Sun 31 Mar 06:05:42 BST 2024
#143M Aug 22 17:47 Miniconda3-latest-Linux-x86_64.sh 
#33442cd3813df33dcbb4a932b938ee95398be98344dff4c30f7e757cd2110e4f  Miniconda3-latest-Linux-x86_64.sh


LINK=https://repo.anaconda.com/miniconda/$MINICONDA_VERSION
echo downloading $LINK
wget -N $LINK

### 03 Verify hash 
sha256sum $MINICONDA_VERSION
## Make sure the hash printed from the command above matches the one available at the Anaconda with Python 3 on 64-bit Linux page for your appropriate Anaconda version.
## https://docs.anaconda.com/anaconda/install/hashes/Anaconda3-2020.11-Linux-x86_64.sh-hash
## cf2ff493f11eaad5d09ce2b4feaa5ea90db5174303d5b3fe030e16d29aeef7de

## 04 Install
bash $MINICONDA_VERSION
#01. press Enter (and keep pressing until you read licences)
#02. Yes to `Do you accept the license terms? [yes|no]`
#03. Enter to default location: $HOME/miniconda3
#04. Yes to `Do you wish the installer to initialize Anaconda3 by running conda init? [yes|no]

#05 Source PATH: 
source ~/.bashrc

#06. type: 
conda config --set auto_activate_base false

## Remove Download
cd ~/Downloads
rm $MINICONDA_VERSION

## References 
# https://varhowto.com/install-miniconda-ubuntu-20-04/
