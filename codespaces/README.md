# Codespaces



## Creating for the first time

### Create codespaces  
1. Select branch
2. Go to Code> create codespace on `branch-name` 
3. `New with options`


## predefined dev container configuration

1. Access the Visual Studio Code Command Palette (Shift+Command+P / Ctrl+Shift+P), then start typing "add dev". 
Click Codespaces: Add Dev Container Configuration Files.
2. Create a new config file
3. Select container conf template: Miniconda (Python3)
4. Select additional feature `Nothing`


Creates:  solid guacamole  https://github.com/codespaces/solid-guacamole-5gqwv79vg77274jg
In the terminal: 
```
conda info
conda env list
```

## Running demo scripts 
* Activate solid guacamole  https://github.com/codespaces/solid-guacamole-5gqwv79vg77274jg
* Select Kernel
* `Install enable suggested extensions Python + Jupyter`
* Python environment 
* demo (Python VERSION) /opt/conda/envs/demo/bin/python
* Run notebook


## References
https://www.sckaiser.com/blog/2023/01/30/conda-codespaces.html  
https://github.com/crazy4pi314/conda-devcontainer-demo  
https://blog.shibayan.jp/entry/20220309/1646754054  
https://www.youtube.com/watch?v=RIchFX_gYb0  
https://github.com/microsoft/AI-For-Beginners/blob/main/.devcontainer/Dockerfile   
* Prebuild configuration: https://github.com/mxochicale/code/settings/codespaces
* https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers#using-a-predefined-dev-container-configuration

