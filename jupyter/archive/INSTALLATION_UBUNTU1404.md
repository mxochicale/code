# Ubuntu 14.04  64


## Installing the latest version of python


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



### issues

* `make: *** [libinstall] Error 1 while installing python`

```
*  I fix it removing /usr/lib/python2.x and /usr/local/lib/python2.x
* sudo rm -rf /usr/lib/python2* && sudo rm -rf  /usr/local/lib/python2*

```

[4](https://github.com/docker-library/python/issues/114)




## install pip

```
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
sudo python get-pip.py
```




## Installing jupyter



```
sudo apt-get update
sudo apt-get -y install python-pip python-dev
sudo -H pip install --upgrade pip
sudo apt-get -y install ipython ipython-notebook
sudo -H pip install jupyter
```


### issues

```
ImportError: Tornado requires an up-to-date SSL module. This means Python 2.7.9+ or 3.4+ (although some distributions have backported the necessary changes to older versions).
```
Then, it was installed the latest version of Python

For other version of ubuntu, refer to 
[ [100] ](https://askubuntu.com/questions/847263/install-jupyter-for-python-2-7-in-ubuntu-14-04)




## References

[ [100] https://askubuntu.com/questions/847263/install-jupyter-for-python-2-7-in-ubuntu-14-04 ](https://askubuntu.com/questions/847263/install-jupyter-for-python-2-7-in-ubuntu-14-04)



## Test

Execute the following command

```
jupyter notebook
```



