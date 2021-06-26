# Python3 Installation

## python 38 on Ubuntu 18.04
```
sudo apt install python3.8
```
https://askubuntu.com/questions/1197683/how-do-i-install-python-3-8-in-lubuntu-18-04



## python 3.7.9 on Machine  Ubuntu 14.04.4 x64

Check the latest version here: https://www.python.org/ftp/python

dependencies
```
sudo apt-get install zlib1g-dev
```

```
version=3.7.0
cd ~/Downloads/
wget https://www.python.org/ftp/python/$version/Python-$version.tgz
sudo tar -xvf Python-$version.tgz
cd Python-$version
sudo ./configure --enable-optimizations

sudo make install #Use sudo make install and not altinstall to set it as default python version
# see output in footnote1


cd ..
sudo rm -rf  Python-$version
rm Python-$version.tgz

```

# references 
https://www.rosehosting.com/blog/how-to-install-python-3-6-on-ubuntu-16-04/


# footnote

footnote1. output:
```
(cd /usr/local/share/man/man1; ln -s python3.7.1 python3.1)
if test "xupgrade" != "xno"  ; then \
		case upgrade in \
			upgrade) ensurepip="--upgrade" ;; \
			install|*) ensurepip="" ;; \
		esac; \
		 ./python -E -m ensurepip \
			$ensurepip --root=/ ; \
	fi
The directory '/home/map479-admin/.cache/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/home/map479-admin/.cache/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Looking in links: /tmp/tmptcm2jw9l
Collecting setuptools
Collecting pip
Installing collected packages: setuptools, pip
Successfully installed pip-10.0.1 setuptools-39.0.1

```


