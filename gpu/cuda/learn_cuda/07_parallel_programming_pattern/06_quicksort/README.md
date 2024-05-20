
## make

```
/usr/local/cuda/bin/nvcc -ccbin g++ -rdc=true -m64 -lineinfo  -I/usr/local/cuda/samples/common/inc -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -o quick_sort quick_sort.cu 
```

## ./quick_sort

```
Running quicksort on 2048 elements
Launching kernel on the GPU
Validating results: OK
```
