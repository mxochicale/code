#chmod +x *.sh

# references 
#https://www.rosehosting.com/blog/how-to-install-python-3-6-on-ubuntu-16-04/

#Check the latest version here: https://www.python.org/ftp/python
#dependencies

sudo apt-get -y install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev zlib1g-dev


version=3.7.0
cd ~/Downloads/
wget https://www.python.org/ftp/python/$version/Python-$version.tgz
sudo tar -xvf Python-$version.tgz
cd Python-$version
sudo ./configure --enable-optimizations
sudo make install #Use sudo make install and not altinstall to set it as default python version


cd ..
sudo rm -rf  Python-$version
rm Python-$version.tgz


##install numpy
#sudo apt-get -y install python3-pip
#pip3 install numpy
##REF https://linuxconfig.org/install-numpy-on-ubuntu-18-04-bionic-beaver-linux


#cd ~/Downloads/
#wget https://bootstrap.pypa.io/get-pip.py
#sudo python get-pip.py
#sudo -H pip3 install numpy

##REF https://stackoverflow.com/questions/41328451/ssl-module-in-python-is-not-available-when-installing-package-with-pip3

