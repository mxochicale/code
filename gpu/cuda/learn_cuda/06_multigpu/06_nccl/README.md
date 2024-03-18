

## Errors

```
mx19@sie133-lap:~/repositories/code/gpu/cuda/learn_cuda/06_multigpu/06_nccl$ make
/usr/local/cuda/bin/nvcc -ccbin g++ -I/usr/local/cuda/samples/common/inc -m64 -lineinfo -lnccl  -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -o nccl nccl.cu 
nccl.cu:7:10: fatal error: nccl.h: No such file or directory
    7 | #include <nccl.h>
      |          ^~~~~~~~
compilation terminated.
make: *** [Makefile:21: nccl] Error 1

```
