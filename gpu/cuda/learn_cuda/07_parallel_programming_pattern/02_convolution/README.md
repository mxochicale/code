
## make
```
~/repositories/code/gpu/cuda/learn_cuda/07_parallel_programming_pattern/02_convolution$ make
/usr/local/cuda/bin/nvcc -ccbin g++ -m64 -g -std=c++11 -lineinfo --maxrregcount=48 --resource-usage -Xcompiler -rdynamic -Xcompiler -fopenmp -rdc=true -I/usr/local/cuda/samples/common/inc -L/usr/local/cuda/lib -lgomp -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -o convolution convolution.cu
nvlink info    : 144 bytes gmem, 65536 bytes cmem[3] (target: sm_52)
nvlink info    : Function properties for '_Z21convolution_kernel_v1PfS_S_iii': (target: sm_52)
nvlink info    : used 30 registers, 0 stack, 0 bytes smem, 356 bytes cmem[0], 0 bytes lmem (target: sm_52)
nvlink info    : Function properties for '_Z21convolution_kernel_v2PfS_S_iii': (target: sm_52)
nvlink info    : used 30 registers, 0 stack, 0 bytes smem, 356 bytes cmem[0], 0 bytes lmem (target: sm_52)
nvlink info    : Function properties for '_Z21convolution_kernel_v3PfS_S_iii': (target: sm_52)
nvlink info    : used 29 registers, 0 stack, 0 bytes smem, 356 bytes cmem[0], 0 bytes lmem (target: sm_52)
nvlink info    : 144 bytes gmem, 65536 bytes cmem[3] (target: sm_60)
nvlink info    : Function properties for '_Z21convolution_kernel_v1PfS_S_iii': (target: sm_60)
nvlink info    : used 30 registers, 0 stack, 0 bytes smem, 356 bytes cmem[0], 0 bytes lmem (target: sm_60)
nvlink info    : Function properties for '_Z21convolution_kernel_v2PfS_S_iii': (target: sm_60)
nvlink info    : used 30 registers, 0 stack, 0 bytes smem, 356 bytes cmem[0], 0 bytes lmem (target: sm_60)
nvlink info    : Function properties for '_Z21convolution_kernel_v3PfS_S_iii': (target: sm_60)
nvlink info    : used 29 registers, 0 stack, 0 bytes smem, 356 bytes cmem[0], 0 bytes lmem (target: sm_60)
nvlink info    : 144 bytes gmem, 65536 bytes cmem[3] (target: sm_61)
nvlink info    : Function properties for '_Z21convolution_kernel_v1PfS_S_iii': (target: sm_61)
nvlink info    : used 30 registers, 0 stack, 0 bytes smem, 356 bytes cmem[0], 0 bytes lmem (target: sm_61)
nvlink info    : Function properties for '_Z21convolution_kernel_v2PfS_S_iii': (target: sm_61)
nvlink info    : used 30 registers, 0 stack, 0 bytes smem, 356 bytes cmem[0], 0 bytes lmem (target: sm_61)
nvlink info    : Function properties for '_Z21convolution_kernel_v3PfS_S_iii': (target: sm_61)
nvlink info    : used 29 registers, 0 stack, 0 bytes smem, 356 bytes cmem[0], 0 bytes lmem (target: sm_61)
nvlink info    : 144 bytes gmem, 65536 bytes cmem[3] (target: sm_70)
nvlink info    : Function properties for '_Z21convolution_kernel_v1PfS_S_iii': (target: sm_70)
nvlink info    : used 32 registers, 0 stack, 0 bytes smem, 388 bytes cmem[0], 0 bytes lmem (target: sm_70)
nvlink info    : Function properties for '_Z21convolution_kernel_v2PfS_S_iii': (target: sm_70)
nvlink info    : used 32 registers, 0 stack, 0 bytes smem, 388 bytes cmem[0], 0 bytes lmem (target: sm_70)
nvlink info    : Function properties for '_Z21convolution_kernel_v3PfS_S_iii': (target: sm_70)
nvlink info    : used 37 registers, 0 stack, 0 bytes smem, 388 bytes cmem[0], 0 bytes lmem (target: sm_70)
nvlink info    : 144 bytes gmem, 65536 bytes cmem[3] (target: sm_75)
nvlink info    : Function properties for '_Z21convolution_kernel_v1PfS_S_iii': (target: sm_75)
nvlink info    : used 32 registers, 0 stack, 0 bytes smem, 388 bytes cmem[0], 0 bytes lmem (target: sm_75)
nvlink info    : Function properties for '_Z21convolution_kernel_v2PfS_S_iii': (target: sm_75)
nvlink info    : used 32 registers, 0 stack, 0 bytes smem, 388 bytes cmem[0], 0 bytes lmem (target: sm_75)
nvlink info    : Function properties for '_Z21convolution_kernel_v3PfS_S_iii': (target: sm_75)
nvlink info    : used 38 registers, 0 stack, 0 bytes smem, 388 bytes cmem[0], 0 bytes lmem (target: sm_75)
nvlink info    : 144 bytes gmem, 65536 bytes cmem[3] (target: sm_80)
nvlink info    : Function properties for '_Z21convolution_kernel_v1PfS_S_iii': (target: sm_80)
nvlink info    : used 32 registers, 0 stack, 0 bytes smem, 388 bytes cmem[0], 0 bytes lmem (target: sm_80)
nvlink info    : Function properties for '_Z21convolution_kernel_v2PfS_S_iii': (target: sm_80)
nvlink info    : used 32 registers, 0 stack, 0 bytes smem, 388 bytes cmem[0], 0 bytes lmem (target: sm_80)
nvlink info    : Function properties for '_Z21convolution_kernel_v3PfS_S_iii': (target: sm_80)
nvlink info    : used 37 registers, 0 stack, 0 bytes smem, 388 bytes cmem[0], 0 bytes lmem (target: sm_80)

```


## $ ./convolution 

```
$ ./convolution 
Processing Time (1) -> GPU: 0.55 ms
Processing Time (2) -> GPU: 0.50 ms
Processing Time (3) -> GPU: 0.32 ms
Processing Time -> Host: 3764.15 ms
SUCCESS!!
```
