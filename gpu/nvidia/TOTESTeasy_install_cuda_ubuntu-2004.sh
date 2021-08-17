
# 1. Explore http://developer.download.nvidia.com/compute/cuda/repos/ to find your OS and arquitecuter 
# 
cd ~/Downloads
CUDA_REPO_PKG=cuda-repo-ubuntu1804_10.2.89-1_amd64.deb
CUDA_URL=http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64
wget -O /tmp/${CUDA_REPO_PKG} ${CUDA_URL}/${CUDA_REPO_PKG} 
