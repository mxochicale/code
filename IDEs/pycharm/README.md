# PyCharm
> PyCharm is an integrated development environment (IDE) used in computer programming, specifically for the Python language. It is developed by the Czech company JetBrains. [:books:](https://en.wikipedia.org/wiki/PyCharm)

## Installation (and tested) on Ubuntu 18.04,20.04 
### Option One[easy]
```
sudo snap install pycharm-community --classic
```

### Option Two [intermediate level]
```
bash installation.bash
```
which roughfly cotains:
```
cd ~/Downloads
#wget https://download.jetbrains.com/python/pycharm-community-2020.3.1.tar.gz
#wget https://download.jetbrains.com/python/pycharm-community-2021.1.tar.gz ## updated on Thu  8 Apr 00:41:56 BST 2021
tar -xzf pycharm-community-20*
rm pycharm-community-20*
cd ~/Downloads/pycharm-community-20*/bin/
chmod u+x pycharm.sh
sh pycharm.sh
```
https://itsfoss.com/install-pycharm-ubuntu/

* Create Desktop app launch

```
    Start PyCharm.
    From the Tools menu, select "Create Desktop Entry..."
    Tick the corresponding box if you want the launcher for all users.
    If you selected "Create entry for all users", you will be asked for your password.
    A green message bubble should appear informing you that it was successful.
    You should then be able to find PyCharm in the Unity Dash or pin it to the launcher.

Note: You may need a system restart before it appears.
```
https://askubuntu.com/questions/391439/how-can-i-set-up-pycharm-to-launch-from-the-launcher


## Customisation 
### Integration with Github 
* [Clone Git repositories using SSH](https://medium.com/@akshay.sinha/pycharm-integration-with-github-876510c6ca1f)


## References
* https://tecadmin.net/how-to-install-pycharm-on-ubuntu-20-04/  
* https://www.jetbrains.com/pycharm/download/#section=linux  
* https://itsfoss.com/install-pycharm-ubuntu  
* https://linuxhint.com/install_pycharm_ubuntu_2004/   
