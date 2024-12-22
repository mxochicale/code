# Examples 

## compile hello.cu
```
nvcc -o hello hello.cu
make 
make clean
```
output: 
```
./hello 
Hello World from GPU! (kernel launch <<M_thread_blocks, T_parallel_threads>>)
Max error: 0.000000
```

## References
https://linuxconfig.org/how-to-install-cuda-on-ubuntu-20-04-focal-fossa-linux   
https://cuda-tutorial.readthedocs.io/en/latest/   
