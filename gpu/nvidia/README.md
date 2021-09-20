## default drivers
```
sudo apt-get clean
sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoremove
sudo apt-get purge nvidia*
sudo ubuntu-drivers autoinstall
reboot
```

https://askubuntu.com/questions/882385/dev-sda1-clean-this-message-appears-after-i-startup-my-laptop-then-it-w




## Using conda 

```
mx19@sie085-lap:~$ nvidia-smi
Thu Apr  8 00:23:34 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.39       Driver Version: 460.39       CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce RTX 2070    Off  | 00000000:01:00.0  On |                  N/A |
| N/A   46C    P8     7W /  N/A |    259MiB /  7973MiB |      1%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1065      G   /usr/lib/xorg/Xorg                 18MiB |
|    0   N/A  N/A      1120      G   /usr/bin/gnome-shell               69MiB |
|    0   N/A  N/A      1523      G   /usr/lib/xorg/Xorg                124MiB |
|    0   N/A  N/A      1684      G   /usr/bin/gnome-shell               40MiB |
|    0   N/A  N/A      4205      G   /usr/lib/firefox/firefox            1MiB |
+-----------------------------------------------------------------------------+
mx19@sie085-lap:~$ nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Wed_Oct_23_19:24:38_PDT_2019
Cuda compilation tools, release 10.2, V10.2.89

```



### Manual installation

#### GPU dependencies 
Ubuntu users working with GPU dependencies should pay attention to nvidia drivers of their machines as these should match with the conda version. 

For instance, I use this:
```
## Install NVIDIA drivers and CUDA for Ubuntu 18.04 LTS  [https://gist.github.com/jmrf/4e2d57a2e5f58e103593fb608de14852]
wget http://us.download.nvidia.com/XFree86/Linux-x86_64/440.100/NVIDIA-Linux-x86_64-440.100.run
sudo chmod +x NVIDIA-Linux-x86_64-440.100.run
```


After installation
```
## Add the following to the end of file [https://sh-tsang.medium.com/tutorial-cuda-v10-2-cudnn-v7-6-5-installation-ubuntu-18-04-3d24c157473f] 
export PATH=/usr/local/cuda/bin:$PATH  
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```

Run the ~/.bashrc again: `source /.bashrc`
Still not sure if cudnn are required by xononav but installed them


```
### download and copy cudnn depencies of cudnn-10.2-linux-x64-v8.1.0.77.tgz from [https://developer.nvidia.com/rdp/cudnn-download] [https://gist.github.com/Mahedi-61/2a2f1579d4271717d421065168ce6a73]
sudo cp cuda/include/cudnn*.h /usr/local/cuda/include 
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda/lib64 
sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*
```


* Check versions
```
mx19@sie085-lap:~$ nvidia-smi
Mon Feb  8 22:42:28 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 440.100      Driver Version: 440.100      CUDA Version: 10.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce RTX 207...  Off  | 00000000:01:00.0  On |                  N/A |
| N/A   48C    P8     6W /  N/A |    246MiB /  7973MiB |      6%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      1357      G   /usr/lib/xorg/Xorg                            18MiB |
|    0      1417      G   /usr/bin/gnome-shell                          49MiB |
|    0      1811      G   /usr/lib/xorg/Xorg                            96MiB |
|    0      1968      G   /usr/bin/gnome-shell                          77MiB |
+-----------------------------------------------------------------------------+
mx19@sie085-lap:~$ nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2019 NVIDIA Corporation
Built on Wed_Oct_23_19:24:38_PDT_2019
Cuda compilation tools, release 10.2, V10.2.89
```








### Virtual environment with python3.8
Due to the  wxPython-4.1.0-cp38-cp38-linux_x86_64.whl dependnecies #787, python3.8 was used to create the virtual environment (ve) for xononav. Further comments will be added re conda ve. 

### Creation of ve with python3.8
```
python3.8 -m venv test38
source test38/bin/activate
```
* you can source ve by adding the following lines to bashrc 
```
#load virtual environment
source $HOME/ve-p38c102/bin/activate
```

### Dependencies installation
```
cd ~/Xononav
source ve-p38c102/bin/activate
git pull
git checkout master 
pip install -U pip #to avoid HTTPError: 404 Client Error: Not Found for url: https://pypi.org/simple/numpy-stubs/
pip install -e .[dev]
pip install torch torchvision  # https://pytorch.org/
```



## Virtual environment with python3.7 
### creation
```
python3.7 -m venv xonodev-py37conda102
```
* source ve using bashrc 
```
echo '#load virtual environment' >> ~/.bashrc 
echo 'source $HOME/xonodev-py37conda102/bin/activate' >> ~/.bashrc 
source  ~/.bashrc 
```

### Dependencies installation
```
cd ~/Xononav
git pull
git checkout master 
pip install -U pip #to avoid HTTPError: 404 Client Error: Not Found for url: https://pypi.org/simple/numpy-stubs/
```
due to a different python version one needs to amend  https://github.com/gift-surg/XonoNav/blob/master/setup.py manually
```
        #return f"wxPython @ https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-18.04/wxPython-{WXPYTHON_VERSION}-cp38-cp38-linux_x86_64.whl"
        return f"wxPython @ https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-18.04/wxPython-{WXPYTHON_VERSION}-cp37-cp37m-linux_x86_64.whl"
        #all versions of wxpython https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-18.04/
```
then 
```
pip install -e .[dev]
pip install torch torchvision  # https://pytorch.org/
```



## In case you need to install the  default drivers
```
sudo apt-get clean
sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoremove
sudo apt-get purge nvidia*
sudo ubuntu-drivers autoinstall
reboot
```

https://askubuntu.com/questions/882385/dev-sda1-clean-this-message-appears-after-i-startup-my-laptop-then-it-w




