


```
$  mpicc -showme 
gcc -I/usr/lib/x86_64-linux-gnu/openmpi/include/openmpi -I/usr/lib/x86_64-linux-gnu/openmpi/include -pthread -L/usr/lib/x86_64-linux-gnu/openmpi/lib -lmpi
```


```
mpicc -g -I/usr/lib/x86_64-linux-gnu/openmpi/include -o helloWorldMPI helloWorldMPI.c -lm
```
