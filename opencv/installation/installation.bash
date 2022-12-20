# References
# https://linuxize.com/post/how-to-install-opencv-on-ubuntu-20-04/
# https://linuxtus.com/uninstall-install-opencv-ubuntu-22-04/

#># Dependencies 20.04
#>sudo apt install build-essential cmake git pkg-config libgtk-3-dev \
#>    libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
#>    libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev \
#>    gfortran openexr libatlas-base-dev python3-dev python3-numpy \
#>    libtbb2 libtbb-dev libdc1394-22-dev libopenexr-dev \
#>    libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev

## Dependencies 22.04
sudo apt-get install cmake gcc g++ libgtk2.0-dev libgtk-3-dev
#>#NO_USED  python3-dev python3-numpy \
#>#NO_USED    libavcodec-dev libavformat-dev libswscale-dev libgstreamer-plugins-base1.0-dev \
#>#NO_USED    libgstreamer1.0-dev

cd ~/Downloads
VERSION=4.6.0 #4.5.5 #See other tags https://github.com/opencv/opencv/tags
mkdir -p ~/opencv_build && cd ~/opencv_build
git clone https://github.com/opencv/opencv.git
cd opencv && git checkout $VERSION && cd ..
git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib && git checkout $VERSION && cd ..

cd ~/opencv_build/opencv
mkdir -p build && cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_build/opencv_contrib/modules \
    -D BUILD_EXAMPLES=ON ..

make -j8

sudo make install

## verify
pkg-config --modversion opencv4
