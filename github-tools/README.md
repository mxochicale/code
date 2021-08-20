# Github tools

 
## GitKraken in Ubuntu 2021
```
cd ~/Downloads
mkdir -p gitkraken && cd gitkraken/

wget https://release.axocdn.com/linux/gitkraken-amd64.deb
# Extract the original deb package
dpkg-deb -R gitkraken-amd64.deb gitkraken-amd64/

# Replace "python" to "python | python2" in dependency list
sed -i -E -e 's/, python,/, python \| python2,/g' gitkraken-amd64/DEBIAN/control

# Package the modifications back into a new deb
dpkg-deb -b gitkraken-amd64/ gitkraken-amd64.focal.deb

# Install as usual
# sudo apt install gdebi-core
sudo gdebi -nq gitkraken-amd64.focal.deb 
```

## Reference  
* https://gist.github.com/ivan-aksamentov/9e59de334c1e1b95f692f222db411f5a

