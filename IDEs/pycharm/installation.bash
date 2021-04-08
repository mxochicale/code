#!/bin/bash

#VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2020.3.1.tar.gz
VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2021.1.tar.gz ## updated on Thu  8 Apr 00:41:56 BST 2021

cd ~/Downloads
wget $VERSION_LINK
tar -xzf pycharm-community-20*
rm pycharm-community-20*.tar.gz
cd ~/Downloads/pycharm-community-20*/bin/
chmod u+x pycharm.sh
sh pycharm.sh
