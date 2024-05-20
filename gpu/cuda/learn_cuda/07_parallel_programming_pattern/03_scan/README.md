
## make

```

/usr/local/cuda/bin/nvcc -ccbin g++ -I/usr/local/cuda/samples/common/inc -std=c++11 -m64 --resource-usage -lineinfo -I/usr/local/cuda/samples/common/inc -L/usr/local/cuda/lib -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -o scan_v1.o -c scan_v1.cu
ptxas info    : 0 bytes gmem
ptxas info    : Compiling entry function '_Z14scan_v1_kernelPfS_i' for 'sm_52'
ptxas info    : Function properties for _Z14scan_v1_kernelPfS_i
    0 bytes stack frame, 0 bytes spill stores, 0 bytes spill loads
ptxas info    : Used 14 registers, 340 bytes cmem[0]
ptxas info    : 0 bytes gmem
ptxas info    : Compiling entry function '_Z14scan_v1_kernelPfS_i' for 'sm_60'
ptxas info    : Function properties for _Z14scan_v1_kernelPfS_i
    0 bytes stack frame, 0 bytes spill stores, 0 bytes spill loads
ptxas info    : Used 14 registers, 340 bytes cmem[0]
ptxas info    : 0 bytes gmem
ptxas info    : Compiling entry function '_Z14scan_v1_kernelPfS_i' for 'sm_61'
ptxas info    : Function properties for _Z14scan_v1_kernelPfS_i
    0 bytes stack frame, 0 bytes spill stores, 0 bytes spill loads
ptxas info    : Used 14 registers, 340 bytes cmem[0]
ptxas info    : 0 bytes gmem
ptxas info    : Compiling entry function '_Z14scan_v1_kernelPfS_i' for 'sm_70'
ptxas info    : Function properties for _Z14scan_v1_kernelPfS_i
    0 bytes stack frame, 0 bytes spill stores, 0 bytes spill loads
ptxas info    : Used 18 registers, 372 bytes cmem[0]
ptxas info    : 0 bytes gmem
ptxas info    : Compiling entry function '_Z14scan_v1_kernelPfS_i' for 'sm_75'
ptxas info    : Function properties for _Z14scan_v1_kernelPfS_i
    0 bytes stack frame, 0 bytes spill stores, 0 bytes spill loads
ptxas info    : Used 17 registers, 372 bytes cmem[0]
ptxas info    : 0 bytes gmem
ptxas info    : Compiling entry function '_Z14scan_v1_kernelPfS_i' for 'sm_80'
ptxas info    : Function properties for _Z14scan_v1_kernelPfS_i
    0 bytes stack frame, 0 bytes spill stores, 0 bytes spill loads
ptxas info    : Used 16 registers, 372 bytes cmem[0]
/usr/local/cuda/bin/nvcc -ccbin g++ -I/usr/local/cuda/samples/common/inc -std=c++11 -m64 --resource-usage -lineinfo -I/usr/local/cuda/samples/common/inc -L/usr/local/cuda/lib -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -o scan_v2.o -c scan_v2.cu
ptxas info    : 0 bytes gmem
ptxas info    : Compiling entry function '_Z14scan_v2_kernelPfS_i' for 'sm_52'
ptxas info    : Function properties for _Z14scan_v2_kernelPfS_i
    0 bytes stack frame, 0 bytes spill stores, 0 bytes spill loads
ptxas info    : Used 10 registers, 340 bytes cmem[0]
ptxas info    : 0 bytes gmem
ptxas info    : Compiling entry function '_Z14scan_v2_kernelPfS_i' for 'sm_60'
ptxas info    : Function properties for _Z14scan_v2_kernelPfS_i
    0 bytes stack frame, 0 bytes spill stores, 0 bytes spill loads
ptxas info    : Used 10 registers, 340 bytes cmem[0]
ptxas info    : 0 bytes gmem
ptxas info    : Compiling entry function '_Z14scan_v2_kernelPfS_i' for 'sm_61'
ptxas info    : Function properties for _Z14scan_v2_kernelPfS_i
    0 bytes stack frame, 0 bytes spill stores, 0 bytes spill loads
ptxas info    : Used 10 registers, 340 bytes cmem[0]
ptxas info    : 0 bytes gmem
ptxas info    : Compiling entry function '_Z14scan_v2_kernelPfS_i' for 'sm_70'
ptxas info    : Function properties for _Z14scan_v2_kernelPfS_i
    0 bytes stack frame, 0 bytes spill stores, 0 bytes spill loads
ptxas info    : Used 14 registers, 372 bytes cmem[0]
ptxas info    : 0 bytes gmem
ptxas info    : Compiling entry function '_Z14scan_v2_kernelPfS_i' for 'sm_75'
ptxas info    : Function properties for _Z14scan_v2_kernelPfS_i
    0 bytes stack frame, 0 bytes spill stores, 0 bytes spill loads
ptxas info    : Used 12 registers, 372 bytes cmem[0]
ptxas info    : 0 bytes gmem
ptxas info    : Compiling entry function '_Z14scan_v2_kernelPfS_i' for 'sm_80'
ptxas info    : Function properties for _Z14scan_v2_kernelPfS_i
    0 bytes stack frame, 0 bytes spill stores, 0 bytes spill loads
ptxas info    : Used 12 registers, 372 bytes cmem[0]
/usr/local/cuda/bin/nvcc -ccbin g++ -std=c++11 -m64 --resource-usage -lineinfo -I/usr/local/cuda/samples/common/inc -L/usr/local/cuda/lib -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -o scan scan.cu scan_v1.o scan_v2.o
ptxas info    : 0 bytes gmem
ptxas info    : 0 bytes gmem
ptxas info    : 0 bytes gmem
ptxas info    : 0 bytes gmem
ptxas info    : 0 bytes gmem
ptxas info    : 0 bytes gmem
```

## ./scan
```

input         ::	-0.4508	-0.0210	-0.4774	 0.2750	-0.2206	 0.3169	-0.1268	 0.1248	-0.2364	 0.4241	 0.0841	 0.3532	 0.2188	 0.0052	 0.0398	 0.4869	
result[cpu]   ::	-0.4508	-0.4718	-0.9492	-0.6742	-0.8948	-0.5779	-0.7047	-0.5798	-0.8162	-0.3922	-0.3081	 0.0452	 0.2640	 0.2693	 0.3091	 0.7960	
result[gpu_v1]::	-0.4508	-0.4718	-0.9492	-0.6742	-0.8948	-0.5779	-0.7047	-0.5798	-0.8162	-0.3922	-0.3081	 0.0452	 0.2640	 0.2693	 0.3091	 0.7960	
SUCCESS!!
result[cpu]   ::	-0.4508	-0.4718	-0.9492	-0.6742	-0.8948	-0.5779	-0.7047	-0.5798	-0.8162	-0.3922	-0.3081	 0.0452	 0.2640	 0.2693	 0.3091	 0.7960	
result[gpu_v2]::	-0.4508	-0.4718	-0.9492	-0.6742	-0.8948	-0.5779	-0.7047	-0.5798	-0.8162	-0.3922	-0.3081	 0.0452	 0.2640	 0.2693	 0.3091	 0.7960	
SUCCESS!!
```

