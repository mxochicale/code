sudo apt-get clean
sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoremove
sudo apt-get purge nvidia*
sudo apt-get remove --purge '^nvidia-.*'
sudo apt-get install ubuntu-desktop # 2. If the ubuntu-desktop package is removed, reinstall it
sudo ubuntu-drivers autoinstall
#reboot

