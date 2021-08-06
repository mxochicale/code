# PyCharm
> PyCharm is an integrated development environment (IDE) used in computer programming, specifically for the Python language. It is developed by the Czech company JetBrains. [:books:](https://en.wikipedia.org/wiki/PyCharm)

## Installation (and tested) on Ubuntu 18.04,20.04 
### Option One[easy]
```
sudo snap install pycharm-community --classic
```

### Option Two [intermediate level]
1. Run bash
```
bash installation.bash
```
2. Import pycharm settings 
it opens a window with `/home/username/.PycharmC2019.3/config` and click OK

* `bash installation.bash` which roughfly cotains:
```
cd ~/Downloads
wget https://download.jetbrains.com/python/pycharm-community-2020.3.1.tar.gz
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


## Spell Checker Spanish Dictionary
```
Agregando el diccionario de español:
    Descarga los archivos aquí.
    Descomprime el zip.
    Dentro de la carpeta descomprimida en src/dict hay un archivo que dice spanish.0 y contiene muchas palabras en español, cambia su extensión a .dic.
    En PyCharm adentro de Settings/Editor/Spelling, en donde dice "Custom Dictionaries", agrega el archivo spanish.dic mencionado antes.
    Da click en "Apply" y listo, ahora PyCharm revisará también tu ortografía en español.
```
https://es.stackoverflow.com/questions/226011/    
https://plugins.jetbrains.com/plugin/7851-spell-checker-spanish-dictionary    


## Uninstalling 

Remove the following directories:

Syntax
    ~/.config/JetBrains/<product><version>
    ~/.cache/JetBrains/<product><version>
    ~/.local/share/JetBrains/<product><version>


## References
* https://tecadmin.net/how-to-install-pycharm-on-ubuntu-20-04/  
* https://www.jetbrains.com/pycharm/download/#section=linux  
* https://itsfoss.com/install-pycharm-ubuntu  
* https://linuxhint.com/install_pycharm_ubuntu_2004/   
