# CNN

## Compiling
```
bash download_mnist.sh
make
./train
make clean
```

## Logs
```

== MNIST training with CUDNN ==
[TRAIN]
loading ./dataset/train-images-idx3-ubyte
loaded 60000 items..
.. model Configuration ..
CUDA: conv1
CUDA: relu
CUDA: pool
CUDA: conv2
CUDA: relu
CUDA: pool
CUDA: dense1
CUDA: relu
CUDA: dense2
CUDA: softmax
.. initialized conv1 layer ..
.. initialized conv2 layer ..
.. initialized dense1 layer ..
.. initialized dense2 layer ..
step:  200, loss: 0.355, accuracy: 69.025%
step:  400, loss: 0.223, accuracy: 93.570%
step:  600, loss: 0.207, accuracy: 94.215%
step:  800, loss: 0.263, accuracy: 94.299%
step: 1000, loss: 0.314, accuracy: 94.320%
step: 1200, loss: 0.272, accuracy: 94.314%
step: 1400, loss: 0.228, accuracy: 94.291%
step: 1600, loss: 0.209, accuracy: 94.295%
.. store weights to the storage ..
.. saving conv1 parameter .. done ..
.. saving relu parameter .. done ..
.. saving pool parameter .. done ..
.. saving conv2 parameter .. done ..
.. saving relu parameter .. done ..
.. saving pool parameter .. done ..
.. saving dense1 parameter .. done ..
.. saving relu parameter .. done ..
.. saving dense2 parameter .. done ..
.. saving softmax parameter .. done ..
[INFERENCE]
loading ./dataset/t10k-images-idx3-ubyte
loaded 10000 items..
loss: 0.641, accuracy: 85.300%
Done.

```


## Erros
* SORTED: Error: libcublasLt.so.12
```
Could not load library libcublasLt.so.12. Error: libcublasLt.so.12: cannot open shared object file: No such file or directory
Invalid handle. Cannot load symbol cublasLtCreate
#sudo find / -name "libcublasLt.so.12"
Resolved by installing 
cuDNN_version=9.1.1
CUDA_VERSION_dots=12.5.0

```

## Reference
https://github.com/PacktPublishing/Learn-CUDA-Programming/tree/master/Chapter10/10_deep_learning/02_cnn


