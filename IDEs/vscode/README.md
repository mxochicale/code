# Visual Studio Code 
> Visual Studio Code is a free source-code editor made by Microsoft for Windows, Linux and macOS [:books:](https://en.wikipedia.org/wiki/Visual_Studio_Code).

## Installation in Ubuntu 20.04x64
Run [install.sh](install.sh)
```
cd $HOME/repositories/code/IDEs/vscode
sudo echo
bash install.bash
#REMOVE apt repository
sudo rm /etc/apt/sources.list.d/vscode.list

```
## Customisation
Adding plugings from the terminal
```
code --install-extension DavidAnson.vscode-markdownlint
```
## Remove vscode
```
apt-key list
sudo apt-key del rsa2048
sudo rm /etc/apt/sources.list.d/vscode.list
sudo apt remove code
sudo apt update # should succeed now
```

## Reference
* https://websiteforstudents.com/how-to-install-visual-studio-code-on-ubuntu-20-04-18-04/
* https://github.com/microsoft/vscode
* https://linuxize.com/post/how-to-install-visual-studio-code-on-ubuntu-20-04/ 

