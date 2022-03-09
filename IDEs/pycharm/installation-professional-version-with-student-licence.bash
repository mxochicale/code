#!/bin/bash

# 1. Check the latest version from 
	# https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux
# 2. Copy and paste in the new version link line:
# 3. Run the bash:
#    bash installation.bash

VERSION_LINK=https://download.jetbrains.com/python/pycharm-professional-2021.3.2.tar.gz #Wed  9 Mar 12:15:22 GMT 2022
cd ~/Downloads
rm -rf  pycharm-professional-202*
wget $VERSION_LINK
tar -xzf pycharm-professional-202*
rm pycharm-professional-202*.tar.gz
cd ~/Downloads/pycharm-202*/bin/
chmod u+x pycharm.sh
sh pycharm.sh
