# Visual Studio Code [#47](https://github.com/mxochicale/code/issues/47)
> Visual Studio Code is a free source-code editor made by Microsoft for Windows, Linux and macOS [:books:](https://en.wikipedia.org/wiki/Visual_Studio_Code).

GitHub: https://github.com/microsoft/vscode
Versions: https://code.visualstudio.com/updates/

## Installation in Ubuntu 20.04x64/22.04x64
* Run [install.sh](install.sh). See [logs](logs.md).
```
cd $HOME/repositories/mxochicale/code/IDEs/vscode
bash install.bash
#Add Microsoft apt repository for Visual Studio Code? <Yes>
```

## Commit changes
```
export V=$(code --version | awk '{printf "%s ", $1}')
echo $V
sed -i "/\<LOG\>/ s/$/ \n\n# $(date) \ncode --version: $V/" log.md #insert date and version
git add .
git commit -m 'code --version: $V #47'
```

## Extensions 
* GitHub.copilot
Open vscode and search for `GitHub.copilot` at Menu: View/Extensions. 
See more [here](../../copilot/)

* markdownlint 
Go to `View>Extensions` and search for markdownlint. 
Alternatively, you might also like to do this from the terminal.
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
