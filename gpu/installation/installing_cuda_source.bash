#################################
### Adding cuda paths to bashrc file [https://sh-tsang.medium.com/tutorial-cuda-v10-2-cudnn-v7-6-5-installation-ubuntu-18-04-3d24c157473f] 
### You might need to check .bashrc to avoid duplication of cuda paths
{
echo ''
echo ''
echo '#============================================================'
echo '#'
echo '#  CUDA PATHS'
echo '#'
echo "export PATH=/usr/local/cuda/bin:${PATH}  "
echo "export LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH}  "
echo ''
echo ''
echo ''
} >> ~/.bashrc


