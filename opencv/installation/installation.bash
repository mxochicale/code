## Dependencies 20.04, 22.04
sudo apt update && sudo apt install -y cmake gcc g++ unzip libgtk2.0-dev libgtk-3-dev wget 

############################
# Build core modules with opencv_contrib
#
# Download and unpack sources
rm -rf ~/opencv_build
mkdir -p ~/opencv_build && cd ~/opencv_build
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.x.zip
unzip opencv.zip
unzip opencv_contrib.zip
# Create build directory and switch into it
mkdir -p build && cd build
# Configure
cmake -DOPENCV_EXTRA_MODULES_PATH=../opencv_contrib-4.x/modules ../opencv-4.x -DWITH_FFMPEG=ON -DOPENCV_GENERATE_PKGCONFIG=ON

### leaving the folling lines for reference
#cmake -D CMAKE_BUILD_TYPE=RELEASE \
#    -D CMAKE_INSTALL_PREFIX=/usr/local \
#    -D INSTALL_C_EXAMPLES=ON \
#    -D INSTALL_PYTHON_EXAMPLES=ON \
#    -D OPENCV_GENERATE_PKGCONFIG=ON \
#    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_build/opencv_contrib/modules \
#    -D BUILD_EXAMPLES=ON ..

# Build
cmake --build .


#Build - run actual compilation process:
make -j8

#Since /usr/local is owned by the root user, the installation should be performed with elevated privileges (sudo):
sudo make install


# verify
#DONT FORGET TO ADD  -D OPENCV_GENERATE_PKGCONFIG=ON \
pkg-config --modversion opencv4


