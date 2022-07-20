
## make
```

/usr/local/cuda/bin/nvcc -ccbin g++ -std=c++11 -I/usr/local/cuda/samples/common/inc -L/usr/local/cuda/lib  -gencode arch=compute_52,code=sm_52 -gencode arch=compute_60,code=sm_60 -gencode arch=compute_61,code=sm_61 -gencode arch=compute_70,code=sm_70 -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -o pack_n_split pack_n_split.cu
```

## ./pack_n_slit

```

input    ::	-0.4508	-0.0210	-0.4774	 0.2750	-0.2206	 0.3169	-0.1268	 0.1248	-0.2364	 0.4241	 0.0841	 0.3532	 0.2188	 0.0052	 0.0398	 0.4869	
pack[cpu]::	 0.2750	 0.3169	 0.1248	 0.4241	 0.0841	 0.3532	 0.2188	 0.0052	 0.0398	 0.4869	 0.1572	 0.1815	 0.2814	 0.0988	 0.3957	 0.2958	
pack[gpu]::	 0.2750	 0.3169	 0.1248	 0.4241	 0.0841	 0.3532	 0.2188	 0.0052	 0.0398	 0.4869	 0.1572	 0.1815	 0.2814	 0.0988	 0.3957	 0.2958	
SUCCESS!!
split[gpu]	 0.0000	 0.0000	 0.0000	 0.2750	 0.0000	 0.3169	 0.0000	 0.1248	 0.0000	 0.4241	 0.0841	 0.3532	 0.2188	 0.0052	 0.0398	 0.4869	
SUCCESS!!
```
