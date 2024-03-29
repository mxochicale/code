# PyCharm
> PyCharm is an integrated development environment (IDE) used in computer programming, specifically for the Python language. 
> It is developed by the Czech company JetBrains. [:books:](https://en.wikipedia.org/wiki/PyCharm)  

The following are instructions of the use of PyCharm under GNU/Linux with distributions of Ubuntu 18.04x64, 20.04x64, 22.04x64.
NOTE. No need to create a new branch and PR, just add #45 in the commit message with the version, e.g.: 
```
git add .
git commit -m 'pycharm-community-2023.3.5. #45'
git push origin main
```

## 1. pycharm-community Installation 

### Option One [intermediate level]

* 1.1 Check the latest version from 
 https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=linux&code=PC
* 1.2 Copy and paste in the new version link in [installation-community-version.bash](installation-community-version.bash)

* 1.3 Installation
```
cd $HOME/repositories/mxochicale/code/IDEs/pycharm
bash installation-community-version.bash
```
* 1.4 Usage
  * Confirm that you have read and accept the terms of this User Agreement
  * DATA SHARING: Don't send 
  * Import a project
  * Reference https://itsfoss.com/install-pycharm-ubuntu/

* 1.5 Create Desktop app launch
```
    * Start PyCharm.
    * Go to Tools menu, 
    * Select "Create Desktop Entry..." and click OKAY.
    	#You can create a desktop entry for easier starting PyCharm from a system menu
	#and better desktop integration
	# [X] Create the entry for all users (require user privilages)
 	
	# TICKING THE CORRESPONDING BOX IS OPTIONAL
    	# Tick the corresponding box if you want the launcher for all users.
    	# If you selected "Create entry for all users", you will be asked for your password.
    	# A green message bubble should appear informing you that it was successful.
    	# You should then be able to find PyCharm in the Unity Dash or pin it to the launcher.
    	# **Note: You may need a system restart before it appears.**

```
Reference https://askubuntu.com/questions/391439/how-can-i-set-up-pycharm-to-launch-from-the-launcher

* 1.6 Remove installation
```
cd $HOME/Downloads
rm -rf pycharm-community-* 
```

### Option Two for installation [easy]
```
sudo snap install pycharm-community --classic
```

## 2. Customisation 
### Opening multiple projects
Open a project, while another one is already opened.
Then, depending on the option selected in the Project Opening section of the System Settings page of the Settings dialog (Ctrl+Alt+S), 
PyCharm can ask you for the following alternatives:
If the New Window option is selected, the new project silently opens in a new window.
![fig](figures/multiple-projects.png)

See more: https://www.jetbrains.com/help/pycharm/open-projects.html#multiple


### Setting conda environments
Open File>Settings (or Ctrl+Alt+S) to set up conda virtual environment
![fig](figures/setting-up-conda-env.png)

### Integration with Github 
* [Clone Git repositories using SSH](https://medium.com/@akshay.sinha/pycharm-integration-with-github-876510c6ca1f)


### Spell Checker Spanish Dictionary
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

## 4 DataSpell 
> The IDE for Professional Data Scientists [:link:](https://www.jetbrains.com/dataspell/)
* Download
```
bash installation-dataspell.bash
#575M Jan 28 08:18  dataspell-2021.3.2.tar.gz
``` 

* Launch  
``` 
cd $HOME/Downloads/dataspell-2021.3.2/bin
sh dataspell.sh
```

* Make use of default env
Check list of env `conda env list`
``` 
TYPE: conda
CONDA_INSTALLATION: $HOME/anaconda3/bin/conda
CONDA_ENVIRONMENT: $HOME/anaconda3/envs/$ENV_NAME/bin/python
``` 

* remove settings and projects
```
rm -rf  $HOME/.config/JetBrains/DataSpell2021.3/
rm -rf $HOME/.config/JetBrains/DataSpell2021.3/projects
```


## The Python IDE for Professional Developers using academic credentials 

2.1. Request education licences as a student of teacher at [JetBrains Products for Learning](https://www.jetbrains.com/shop/eform/students). You need your academic email.  
2.2. Download and install it via terminal.  
``` 
cd $HOME/repositories/code/IDEs/pycharm
bash installation-professional-version-with-student-licence.bash 
```
2.3. Activate licences  
![figs](figures/licenses-pycharm-professional-v2021-3-2.png)  

See more: https://www.jetbrains.com/community/education/#students


## Uninstalling
Remove the following directories:

Syntax
```
    ~/.config/JetBrains/<product><version>
    ~/.cache/JetBrains/<product><version>
    ~/.local/share/JetBrains/<product><version>
```

## References
* https://tecadmin.net/how-to-install-pycharm-on-ubuntu-20-04/  
* https://www.jetbrains.com/pycharm/download/#section=linux  
* https://itsfoss.com/install-pycharm-ubuntu  
* https://linuxhint.com/install_pycharm_ubuntu_2004/   
