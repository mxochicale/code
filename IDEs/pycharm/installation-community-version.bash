#!/bin/bash
#PyCharm Community Edition
#Free, built on open source

# 1. Check the latest version from 
    # https://www.jetbrains.com/pycharm/download/?section=linux
    # Click download to see version, for example 2023.3.5.tar.gz
# 2. Copy and paste in the new version link line:
# 3. Run the bash:
#    bash installation-community-version.bash

#https://download.jetbrains.com/python/pycharm-community-2020.3.1.tar.gz
#https://download.jetbrains.com/python/pycharm-community-2021.1.tar.gz ## updated on Thu  8 Apr 00:41:56 BST 2021
#VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2021.1.1.tar.gz #Tue  1 Jun 21:43:57 BST 2021
#VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2021.2.tar.gz #Fri  6 Aug 14:49:19 BST 2021
#VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2021.2.2.tar.gz #Mon 20 Sep 23:50:31 BST 2021
#VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2021.3.tar.gz #Mon  6 Dec 08:52:40 GMT 2021
#VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2022.2.3.tar.gz #Mon 17 Oct 10:28:46 BST 2022
#VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2022.3.2.tar.gz 	#Wed  1 Mar 13:02:39 GMT 2023   
											# Build #PC-223.8617.48, built on January 24, 2023

#VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2023.1.1.tar.gz 	#Mon  1 May 01:36:15 BST 2023
    #Version: 2023.1.1
    #Build: 231.8770.66
    #28 April 2023

#VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2023.2.tar.gz 	#Wed 16 Aug 02:26:14 BST 2023
	#Version: 2023.2
	#Build #PC-232.8660.197, built on July 26, 2023
	#Runtime version: 17.0.7+7-b1000.6 amd64
	#VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o.
	#Linux 6.2.0-26-generic
	#GC: G1 Young Generation, G1 Old Generation
	#Memory: 2048M
	#Cores: 20
	#Current Desktop: ubuntu:GNOME

VERSION_LINK=https://download.jetbrains.com/python/pycharm-community-2023.3.5.tar.gz # Sun 24 Mar 16:54:30 GMT 2024
    ## Pycharm>Help>About
    #Build #PC-233.15026.15, built on March 21, 2024
    #Runtime version: 17.0.10+1-b1087.23 amd64
    #VM: OpenJDK 64-Bit Server VM by JetBrains s.r.o

#VERSION_LINK=? #:r !date
		#copy build version from the app

cd ~/Downloads
rm -rf  pycharm-community-202*
wget $VERSION_LINK
tar -xzf pycharm-community-20*
rm pycharm-community-20*.tar.gz
cd ~/Downloads/pycharm-community-20*/bin/
chmod u+x pycharm.sh
sh pycharm.sh

