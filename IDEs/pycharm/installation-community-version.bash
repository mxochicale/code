#!/bin/bash

# 1. Check the latest version from 
	# https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux&code=PC
# 2. Copy and paste in the new version link line:
# 3. Run the bash:
#    bash installation.bash

#https://download.jetbrains.com/python/pycharm-community-2020.3.1.tar.gz
#https://download.jetbrains.com/python/pycharm-community-2021.1.tar.gz ## updated on Thu  8 Apr 00:41:56 BST 2021
#VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2021.1.1.tar.gz #Tue  1 Jun 21:43:57 BST 2021
#VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2021.2.tar.gz #Fri  6 Aug 14:49:19 BST 2021
#VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2021.2.2.tar.gz #Mon 20 Sep 23:50:31 BST 2021
VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2021.3.tar.gz #Mon  6 Dec 08:52:40 GMT 2021

cd ~/Downloads
rm -rf  pycharm-community-202*
wget $VERSION_LINK
tar -xzf pycharm-community-20*
rm pycharm-community-20*.tar.gz
cd ~/Downloads/pycharm-community-20*/bin/
chmod u+x pycharm.sh
sh pycharm.sh

