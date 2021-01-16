Python Installation
---

# On Machine  Ubuntu 16.04.4 x64


```
sudo apt-get update
sudo apt-get upgrade
```

The machine gets this version of python
```
$ python2.7   
Python 2.7.12 (default, Nov 19 2016, 06:48:10)   
[GCC 5.4.0 20160609] on linux2  
```


## 2.7.15

delete previous version
```
sudo rm -rf /usr/lib/python2* && sudo rm -rf  /usr/local/lib/python2*
```

[4](https://github.com/docker-library/python/issues/114)



Some dependencies
```
sudo apt-get update
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
```

```
version=2.7.15
cd ~/Downloads/
wget https://www.python.org/ftp/python/$version/Python-$version.tgz
sudo tar -xvf Python-$version.tgz
cd Python-$version
sudo ./configure --enable-optimizations

sudo make install #Use sudo make install and not altinstall to set it as default python version

cd ..
rm -rf  Python-$version
rm Python-$version.tgz
```

[2](https://tecadmin.net/install-python-2-7-on-ubuntu-and-linuxmint/)
[3](https://askubuntu.com/questions/101591/how-do-i-install-the-latest-python-2-7-x-or-3-x-on-ubuntu)





## install pip

```
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
sudo python get-pip.py
```







## Upgrate Python 2.7 to Python-2.7.13

This move might hurt a bit for your machine since some frameworks like ROS might
have issues with the workable versions of python. Proceed with precaution and do it
just for experimentation in your experimental machine.

```
sudo apt-get install build-essential checkinstall  
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev  
```


```
cd /usr/src
sudo su
wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz
tar xzf Python-2.7.13.tgz
rm -rf Python-2.7.13.tgz
cd Python-2.7.13
./configure
#make altinstall #make altinstall is used to prevent replacing the default python binary file /usr/bin/python.
make install
```

```
# python2.7 -V
Python 2.7.13
```
[REF](https://tecadmin.net/install-python-2-7-on-centos-rhel/)
