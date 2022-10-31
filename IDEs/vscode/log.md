# LOG


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
