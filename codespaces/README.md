# Codespaces

## New to codespaces?
* [Start here](https://docs.github.com/en/codespaces). Learn the core concepts and how to get started.
* [Quickstart for GitHub Codespaces](https://docs.github.com/en/codespaces/getting-started/quickstart).

## Create codespaces  
1. Open your repository and go to `Code`>`Codespaces`
2. Select branch
3. Create codespace on `branch-name`. #This will take 3-ish minutes to prebuild container

The creation of codespace make use of 
  * [Dockerfile](../.devcontainer/Dockerfile) 
  * [devcontainer.json](../.devcontainer/devcontainer.json)
  * [demoVE.yaml](demoVE.yml)
  * [noop.txt](noop.txt)


## (First time) Predefined dev container configuration
1. Access the Visual Studio Code Command Palette (Shift+Command+P / Ctrl+Shift+P), then start typing "add dev". 
Click Codespaces: Add Dev Container Configuration Files.
2. Create a new config file
3. Select container conf template: Miniconda (Python3)
4. Select additional feature `Nothing`

Creates: `docker_funny_name_ID`  https://github.com/codespaces/`docker_funny_name_ID`
You can check in the terminal these commands: `conda info` and `conda env list`

## (Already created) Running demo scripts 
* Activate `docker_funny_name_ID`  https://github.com/codespaces/`docker_funny_name_ID`
* Open notebook 
* Select Kernel (top right icon)
  * `Install enable suggested extensions Python + Jupyter`
  * Python environment 
  * demoVE (Python VERSION) /opt/conda/envs/demoVE/bin/python
* Run notebook
* Stop running container (bottom left menu)
* Maybe go https://github.com/codespaces/ to delete it


## References
https://www.sckaiser.com/blog/2023/01/30/conda-codespaces.html  
https://github.com/crazy4pi314/conda-devcontainer-demo  
https://blog.shibayan.jp/entry/20220309/1646754054  
https://www.youtube.com/watch?v=RIchFX_gYb0  
https://github.com/microsoft/AI-For-Beginners/blob/main/.devcontainer/Dockerfile   
* Prebuild configuration: https://github.com/mxochicale/code/settings/codespaces
* https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers#using-a-predefined-dev-container-configuration

