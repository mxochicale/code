# LOG
## Fri 18 Aug 15:28:49 BST 2023
* version
```
code --version

1.81.1
6c3e3dba23e8fadc360aed75ce363ba185c49794
x64
```



## Sun 19 Mar 10:01:27 GMT 2023
* version
```
code --version
1.76.2
ee2b180d582a7f601fa6ecfdad8d9fd269ab1884
x64

```
* log
```

bash install.bash 
[sudo] password for mxochicale: 
Hit:1 http://gb.archive.ubuntu.com/ubuntu focal InRelease
Hit:2 http://gb.archive.ubuntu.com/ubuntu focal-updates InRelease                         
Hit:3 http://security.ubuntu.com/ubuntu focal-security InRelease                          
Hit:4 http://gb.archive.ubuntu.com/ubuntu focal-backports InRelease
Hit:5 https://repo.skype.com/deb stable InRelease            
Reading package lists... Done                                
Building dependency tree       
Reading state information... Done
187 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree       
Reading state information... Done
apt-transport-https is already the newest version (2.0.9).
The following packages were automatically installed and are no longer required:
  evince-common gir1.2-goa-1.0 libevdocument3-4 libevview3-3 libkpathsea6 libspectre1 libsynctex2
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  distro-info python3-software-properties software-properties-gtk ubuntu-advantage-desktop-daemon ubuntu-advantage-tools
Suggested packages:
  shunit2
The following NEW packages will be installed
  distro-info ubuntu-advantage-desktop-daemon
The following packages will be upgraded:
  python3-software-properties software-properties-common software-properties-gtk ubuntu-advantage-tools wget
5 to upgrade, 2 to newly install, 0 to remove and 182 not to upgrade.
Need to get 663 kB of archives.
After this operation, 906 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://gb.archive.ubuntu.com/ubuntu focal/main amd64 distro-info amd64 0.23ubuntu1 [17.1 kB]
Get:2 http://gb.archive.ubuntu.com/ubuntu focal-updates/main amd64 ubuntu-advantage-tools amd64 27.13.6~20.04.1 [173 kB]
Get:3 http://gb.archive.ubuntu.com/ubuntu focal-updates/main amd64 wget amd64 1.20.3-1ubuntu2 [348 kB]
Get:4 http://gb.archive.ubuntu.com/ubuntu focal-updates/main amd64 software-properties-common all 0.99.9.11 [10.4 kB]
Get:5 http://gb.archive.ubuntu.com/ubuntu focal-updates/main amd64 ubuntu-advantage-desktop-daemon amd64 1.10~20.04.1 [23.5 kB]
Get:6 http://gb.archive.ubuntu.com/ubuntu focal-updates/main amd64 software-properties-gtk all 0.99.9.11 [69.1 kB]
Get:7 http://gb.archive.ubuntu.com/ubuntu focal-updates/main amd64 python3-software-properties all 0.99.9.11 [21.6 kB]
Fetched 663 kB in 0s (4,180 kB/s)                      
debconf: Unable to initialise frontend: Dialog
debconf: (Dialogue frontend requires a screen at least 13 lines tall and 31 columns wide.)
debconf: falling back to frontend: Readline
Preconfiguring packages ...
Selecting previously unselected package distro-info.
(Reading database ... 275082 files and directories currently installed.)
Preparing to unpack .../0-distro-info_0.23ubuntu1_amd64.deb ...
Unpacking distro-info (0.23ubuntu1) ...
Preparing to unpack .../1-ubuntu-advantage-tools_27.13.6~20.04.1_amd64.deb ...
Unpacking ubuntu-advantage-tools (27.13.6~20.04.1) over (20.3) ...
Preparing to unpack .../2-wget_1.20.3-1ubuntu2_amd64.deb ...
Unpacking wget (1.20.3-1ubuntu2) over (1.20.3-1ubuntu1) ...
Preparing to unpack .../3-software-properties-common_0.99.9.11_all.deb ...
Unpacking software-properties-common (0.99.9.11) over (0.98.9.5) ...
Selecting previously unselected package ubuntu-advantage-desktop-daemon.
Preparing to unpack .../4-ubuntu-advantage-desktop-daemon_1.10~20.04.1_amd64.deb ...
Unpacking ubuntu-advantage-desktop-daemon (1.10~20.04.1) ...
Preparing to unpack .../5-software-properties-gtk_0.99.9.11_all.deb ...
Unpacking software-properties-gtk (0.99.9.11) over (0.98.9.5) ...
Preparing to unpack .../6-python3-software-properties_0.99.9.11_all.deb ...
Unpacking python3-software-properties (0.99.9.11) over (0.98.9.5) ...
Setting up distro-info (0.23ubuntu1) ...
Setting up wget (1.20.3-1ubuntu2) ...
Setting up python3-software-properties (0.99.9.11) ...
Setting up ubuntu-advantage-tools (27.13.6~20.04.1) ...
Installing new version of config file /etc/logrotate.d/ubuntu-advantage-tools ...
Installing new version of config file /etc/ubuntu-advantage/uaclient.conf ...
debconf: Unable to initialise frontend: Dialog
debconf: (Dialogue frontend requires a screen at least 13 lines tall and 31 columns wide.)
debconf: falling back to frontend: Readline
Created symlink /etc/systemd/system/multi-user.target.wants/ua-reboot-cmds.service → /lib/systemd/system/ua-reboot-cmds.service.
Created symlink /etc/systemd/system/timers.target.wants/ua-timer.timer → /lib/systemd/system/ua-timer.timer.
Created symlink /etc/systemd/system/multi-user.target.wants/ubuntu-advantage.service → /lib/systemd/system/ubuntu-advantage.service.
Setting up ubuntu-advantage-desktop-daemon (1.10~20.04.1) ...
ubuntu-advantage-desktop-daemon.service is a disabled or a static unit, not starting it.
Setting up software-properties-common (0.99.9.11) ...
Setting up software-properties-gtk (0.99.9.11) ...
Processing triggers for dbus (1.12.16-2ubuntu2.3) ...
Processing triggers for shared-mime-info (1.15-1) ...
Processing triggers for install-info (6.7.0.dfsg.2-5) ...
Processing triggers for desktop-file-utils (0.24-1ubuntu3) ...
Processing triggers for mime-support (3.64ubuntu1) ...
Processing triggers for hicolor-icon-theme (0.17-2) ...
Processing triggers for gnome-menus (3.36.0-1ubuntu1) ...
Processing triggers for libglib2.0-0:amd64 (2.64.6-1~ubuntu20.04.3) ...
Processing triggers for man-db (2.9.1-1) ...
OK
Hit:1 http://gb.archive.ubuntu.com/ubuntu focal InRelease
Hit:2 http://gb.archive.ubuntu.com/ubuntu focal-updates InRelease                                                                                  
Hit:3 http://gb.archive.ubuntu.com/ubuntu focal-backports InRelease                                                                                
Hit:4 https://repo.skype.com/deb stable InRelease                                                                                                  
Get:5 https://packages.microsoft.com/repos/vscode stable InRelease [1,867 B]                                                                       
Hit:6 http://security.ubuntu.com/ubuntu focal-security InRelease                                                
Get:7 https://packages.microsoft.com/repos/vscode stable/main amd64 Packages [162 kB]
Fetched 164 kB in 1s (184 kB/s)   
Reading package lists... Done
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  evince-common gir1.2-goa-1.0 libevdocument3-4 libevview3-3 libkpathsea6 libspectre1 libsynctex2
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed
  code
0 to upgrade, 1 to newly install, 0 to remove and 182 not to upgrade.
Need to get 94.8 MB of archives.
After this operation, 394 MB of additional disk space will be used.
Get:1 https://packages.microsoft.com/repos/vscode stable/main amd64 code amd64 1.76.2-1678817801 [94.8 MB]
Fetched 94.8 MB in 14s (6,580 kB/s)                                                                                                                
Selecting previously unselected package code.
(Reading database ... 275222 files and directories currently installed.)
Preparing to unpack .../code_1.76.2-1678817801_amd64.deb ...
Unpacking code (1.76.2-1678817801) ...
Setting up code (1.76.2-1678817801) ...
Error in file "/usr/share/applications/org.kde.kdeconnect_open.desktop": "*/*" is an invalid MIME type ("*" is an unregistered media type)
Processing triggers for mime-support (3.64ubuntu1) ...
Processing triggers for gnome-menus (3.36.0-1ubuntu1) ...
Processing triggers for shared-mime-info (1.15-1) ...
Processing triggers for desktop-file-utils (0.24-1ubuntu3) ...

```


## Tue 29 Nov 00:44:40 GMT 2022
* version
```
code --version
1.73.1
6261075646f055b99068d3688932416f2346dd3b
x64


```

* logs
```
$ bash install.bash 
[sudo] password for mxochicale: 
Get:1 file:/var/cuda-repo-ubuntu2204-11-8-local  InRelease [1,575 B]
Get:1 file:/var/cuda-repo-ubuntu2204-11-8-local  InRelease [1,575 B]
Hit:2 http://gb.archive.ubuntu.com/ubuntu jammy InRelease
Get:3 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]                             
Get:4 http://gb.archive.ubuntu.com/ubuntu jammy-updates InRelease [114 kB]                                      
Get:5 https://dl.google.com/linux/chrome/deb stable InRelease [1,811 B]                                                    
Get:6 http://gb.archive.ubuntu.com/ubuntu jammy-backports InRelease [99.8 kB]             
Get:7 https://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,127 B]
Get:8 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [497 kB]
Get:9 http://gb.archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [731 kB]
Get:10 http://security.ubuntu.com/ubuntu jammy-security/main i386 Packages [214 kB]
Get:11 http://security.ubuntu.com/ubuntu jammy-security/main Translation-en [108 kB]     
Get:12 http://security.ubuntu.com/ubuntu jammy-security/main amd64 DEP-11 Metadata [20.1 kB]     
Get:13 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 Packages [409 kB]                
Get:14 http://gb.archive.ubuntu.com/ubuntu jammy-updates/main i386 Packages [382 kB]              
Get:15 http://security.ubuntu.com/ubuntu jammy-security/restricted Translation-en [62.3 kB]
Get:16 http://security.ubuntu.com/ubuntu jammy-security/universe i386 Packages [480 kB]            
Get:17 http://gb.archive.ubuntu.com/ubuntu jammy-updates/main Translation-en [164 kB]             
Get:18 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [618 kB]         
Get:19 http://gb.archive.ubuntu.com/ubuntu jammy-updates/main amd64 DEP-11 Metadata [94.9 kB]    
Get:20 http://gb.archive.ubuntu.com/ubuntu jammy-updates/universe i386 Packages [554 kB]                    
Get:21 http://security.ubuntu.com/ubuntu jammy-security/universe Translation-en [81.0 kB]                   
Get:22 http://gb.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [757 kB]         
Get:23 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 DEP-11 Metadata [13.3 kB]   
Get:24 http://gb.archive.ubuntu.com/ubuntu jammy-updates/universe Translation-en [126 kB]            
Get:25 http://gb.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 DEP-11 Metadata [257 kB]
Get:26 http://gb.archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 DEP-11 Metadata [940 B]
Get:27 http://gb.archive.ubuntu.com/ubuntu jammy-backports/universe amd64 DEP-11 Metadata [11.6 kB]
Fetched 5,909 kB in 2s (2,808 kB/s)                                           
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
29 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
wget is already the newest version (1.21.2-2ubuntu1).
wget set to manually installed.
software-properties-common is already the newest version (0.99.22.3).
software-properties-common set to manually installed.
The following packages were automatically installed and are no longer required:
  libflashrom1 libftdi1-2
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed
  apt-transport-https
0 to upgrade, 1 to newly install, 0 to remove and 29 not to upgrade.
Need to get 1,506 B of archives.
After this operation, 169 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://gb.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 apt-transport-https all 2.4.8 [1,506 B]
Fetched 1,506 B in 0s (25.5 kB/s)               
Selecting previously unselected package apt-transport-https.
(Reading database ... 193245 files and directories currently installed.)
Preparing to unpack .../apt-transport-https_2.4.8_all.deb ...
Unpacking apt-transport-https (2.4.8) ...
Setting up apt-transport-https (2.4.8) ...
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
OK
Repository: 'deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main'
Description:
Archive for codename: stable components: main
More info: https://packages.microsoft.com/repos/vscode
Adding repository.
Press [ENTER] to continue or Ctrl-c to cancel.
Adding deb entry to /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.list
Adding disabled deb-src entry to /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.list
Get:1 file:/var/cuda-repo-ubuntu2204-11-8-local  InRelease [1,575 B]
Get:1 file:/var/cuda-repo-ubuntu2204-11-8-local  InRelease [1,575 B]
Hit:2 http://gb.archive.ubuntu.com/ubuntu jammy InRelease                   
Hit:3 http://security.ubuntu.com/ubuntu jammy-security InRelease                                                       
Hit:4 http://gb.archive.ubuntu.com/ubuntu jammy-updates InRelease                                                      
Hit:5 http://gb.archive.ubuntu.com/ubuntu jammy-backports InRelease                                                    
Hit:6 https://dl.google.com/linux/chrome/deb stable InRelease                                                    
Get:7 https://packages.microsoft.com/repos/vscode stable InRelease [3,959 B]  
Get:8 https://packages.microsoft.com/repos/vscode stable/main amd64 Packages [336 kB]
Fetched 340 kB in 1s (398 kB/s)   
Reading package lists... Done
W: https://packages.microsoft.com/repos/vscode/dists/stable/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libflashrom1 libftdi1-2
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed
  code
0 to upgrade, 1 to newly install, 0 to remove and 29 not to upgrade.
Need to get 96.7 MB of archives.
After this operation, 397 MB of additional disk space will be used.
Get:1 https://packages.microsoft.com/repos/vscode stable/main amd64 code amd64 1.73.1-1667967334 [96.7 MB]
Fetched 96.7 MB in 18s (5,524 kB/s)                                                                                                                                                                       
Selecting previously unselected package code.
(Reading database ... 193249 files and directories currently installed.)
Preparing to unpack .../code_1.73.1-1667967334_amd64.deb ...
Unpacking code (1.73.1-1667967334) ...
Setting up code (1.73.1-1667967334) ...
Processing triggers for gnome-menus (3.36.0-1ubuntu3) ...
Processing triggers for shared-mime-info (2.1-2) ...
Processing triggers for mailcap (3.70+nmu1ubuntu1) ...
Processing triggers for desktop-file-utils (0.26-1ubuntu3) ...

```

## Mon 31 Oct 15:52:01 GMT 2022
* Version
```
$ code --version
1.72.2
d045a5eda657f4d7b676dedbfa7aab8207f8a075
x64

```

* logs

```
$ sudo bash install.bash 
Hit:1 http://gb.archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://gb.archive.ubuntu.com/ubuntu jammy-updates InRelease [114 kB]                                        
Get:3 http://gb.archive.ubuntu.com/ubuntu jammy-backports InRelease [99.8 kB]                                                                     
Get:4 https://dl.google.com/linux/chrome/deb stable InRelease [1,811 B]         
Get:5 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]                    
Get:6 http://gb.archive.ubuntu.com/ubuntu jammy-updates/main i386 Packages [371 kB]
Get:7 https://dl.google.com/linux/chrome/deb stable/main amd64 Packages [1,118 B]
Get:8 http://gb.archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [695 kB]
Get:9 http://gb.archive.ubuntu.com/ubuntu jammy-updates/main amd64 DEP-11 Metadata [95.1 kB]
Get:10 http://gb.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [743 kB]         
Get:11 http://security.ubuntu.com/ubuntu jammy-security/main amd64 DEP-11 Metadata [20.0 kB]
Get:12 http://gb.archive.ubuntu.com/ubuntu jammy-updates/universe i386 Packages [546 kB]
Get:13 http://gb.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 DEP-11 Metadata [254 kB]
Get:14 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 DEP-11 Metadata [13.2 kB]
Get:15 http://gb.archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 DEP-11 Metadata [940 B]            
Get:16 http://gb.archive.ubuntu.com/ubuntu jammy-backports/universe amd64 DEP-11 Metadata [12.6 kB]
Fetched 3,078 kB in 1s (3,271 kB/s)                                          
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
11 packages can be upgraded. Run 'apt list --upgradable' to see them.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
wget is already the newest version (1.21.2-2ubuntu1).
wget set to manually installed.
software-properties-common is already the newest version (0.99.22.3).
software-properties-common set to manually installed.
The following packages were automatically installed and are no longer required:
  libflashrom1 libftdi1-2
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed
  apt-transport-https
0 to upgrade, 1 to newly install, 0 to remove and 11 not to upgrade.
Need to get 1,506 B of archives.
After this operation, 169 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://gb.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 apt-transport-https all 2.4.8 [1,506 B]
Fetched 1,506 B in 0s (28.5 kB/s)               
Selecting previously unselected package apt-transport-https.
(Reading database ... 176938 files and directories currently installed.)
Preparing to unpack .../apt-transport-https_2.4.8_all.deb ...
Unpacking apt-transport-https (2.4.8) ...
Setting up apt-transport-https (2.4.8) ...
Warning: apt-key is deprecated. Manage keyring files in trusted.gpg.d instead (see apt-key(8)).
OK
Repository: 'deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main'
Description:
Archive for codename: stable components: main
More info: https://packages.microsoft.com/repos/vscode
Adding repository.
Press [ENTER] to continue or Ctrl-c to cancel.
Adding deb entry to /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.list
Adding disabled deb-src entry to /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.list
Hit:1 http://gb.archive.ubuntu.com/ubuntu jammy InRelease
Hit:2 http://gb.archive.ubuntu.com/ubuntu jammy-updates InRelease                                
Hit:3 http://gb.archive.ubuntu.com/ubuntu jammy-backports InRelease                              
Get:4 https://packages.microsoft.com/repos/vscode stable InRelease [3,959 B]                                    
Hit:5 http://security.ubuntu.com/ubuntu jammy-security InRelease                                      
Hit:6 https://dl.google.com/linux/chrome/deb stable InRelease                   
Get:7 https://packages.microsoft.com/repos/vscode stable/main amd64 Packages [331 kB]
Fetched 335 kB in 1s (510 kB/s)   
Reading package lists... Done
W: https://packages.microsoft.com/repos/vscode/dists/stable/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libflashrom1 libftdi1-2
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed
  code
0 to upgrade, 1 to newly install, 0 to remove and 11 not to upgrade.
Need to get 88.1 MB of archives.
After this operation, 369 MB of additional disk space will be used.
Get:1 https://packages.microsoft.com/repos/vscode stable/main amd64 code amd64 1.72.2-1665614327 [88.1 MB]
Fetched 88.1 MB in 16s (5,654 kB/s)                                                                                                                                                                               
Selecting previously unselected package code.
(Reading database ... 176942 files and directories currently installed.)
Preparing to unpack .../code_1.72.2-1665614327_amd64.deb ...
Unpacking code (1.72.2-1665614327) ...
Setting up code (1.72.2-1665614327) ...
Processing triggers for gnome-menus (3.36.0-1ubuntu3) ...
Processing triggers for shared-mime-info (2.1-2) ...
Processing triggers for mailcap (3.70+nmu1ubuntu1) ...
Processing triggers for desktop-file-utils (0.26-1ubuntu3) ...

~/repositories/mxochicale/code/IDEs/vscode$ sudo rm /etc/apt/sources.list.d/vscode.list


```


## Thu 17 Feb 16:06:15 GMT 2022
```
$ code --version
1.64.2
f80445acd5a3dadef24aa209168452a3d97cc326
x64
```


## Fri 29 Oct 20:20:06 BST 2021
```
$ code --version
1.61.2
6cba118ac49a1b88332f312a8f67186f7f3c1643
x64
```
