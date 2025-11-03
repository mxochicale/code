## Installation of RStudio in ubuntu
# https://posit.co/download/rstudio-desktop/


UBUNTU_version=jammy
RSTUDIO_deb=rstudio-2025.09.2-418-amd64.deb
#rstudio-2025.09.1-401-amd64.deb

sudo apt update -qq
sudo apt-get install gdebi-core
cd ~/Downloads
wget https://download1.rstudio.org/electron/${UBUNTU_version}/amd64/${RSTUDIO_deb} -O ${RSTUDIO_deb}
sudo gdebi ${RSTUDIO_deb}
rm -rf ${RSTUDIO_deb}
