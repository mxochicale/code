#!/bin/bash
#
# 1. Check the latest version from 
	# https://www.jetbrains.com/dataspell/
# 2. Copy and paste in the new version link line:
# 3. Run the bash:
#    bash installation.bash

VERSION_LINK=https://download.jetbrains.com/python/dataspell-2021.3.2.tar.gz #Wed  9 Mar 13:32:15 GMT 2022

cd ~/Downloads
wget $VERSION_LINK
tar -xzf dataspell-202*
rm dataspell-202*.tar.gz
cd ~/Downloads/dataspell-202*/bin/
chmod u+x dataspell.sh
sh dataspell.sh
