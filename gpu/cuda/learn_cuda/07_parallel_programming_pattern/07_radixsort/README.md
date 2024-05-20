
## make

```

/usr/local/cuda/bin/nvcc -ccbin g++ -rdc=true -m64 -lineinfo  -I/usr/local/cuda/samples/common/inc -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -o radix_warp_sort radix_warp_sort.cu 
/usr/local/cuda/bin/nvcc -ccbin g++ -rdc=true -m64 -lineinfo  -I/usr/local/cuda/samples/common/inc -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -o thrust_radix_sort thrust_radix_sort.cu 
```

## ./

```

 ./radix_warp_sort 
Sorting Successful!

./thrust_radix_sort 
sorting integers
 79 78 62 78 94 40 86 57 40 16 28 54 77 87 93 98
 16 28 40 40 54 57 62 77 78 78 79 86 87 93 94 98

sorting integers (descending)
 79 78 62 78 94 40 86 57 40 16 28 54 77 87 93 98
 98 94 93 87 86 79 78 78 77 62 57 54 40 40 28 16
```
