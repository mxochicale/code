# ANN

## Compiling
```
bash download_mnist.sh
make
./train
make clean
```

## logs
```
== MNIST training with CUDNN ==
[TRAIN]
loading ./dataset/train-images-idx3-ubyte
loaded 60000 items..
.. model Configuration ..
CUDA: dense1
CUDA: relu
CUDA: dense2
CUDA: softmax
.. initialized dense1 layer ..
.. initialized dense2 layer ..
step:  200, loss: 0.660, accuracy: 79.289%
step:  400, loss: 0.559, accuracy: 90.316%
step:  600, loss: 0.537, accuracy: 90.506%
step:  800, loss: 0.530, accuracy: 90.494%
step: 1000, loss: 0.643, accuracy: 90.533%
step: 1200, loss: 0.584, accuracy: 90.551%
step: 1400, loss: 0.552, accuracy: 90.533%
step: 1600, loss: 0.534, accuracy: 90.535%
[INFERENCE]
loading ./dataset/t10k-images-idx3-ubyte
loaded 10000 items..
loss: 1.158, accuracy: 78.700%
Done.
```



## Reference
https://github.com/PacktPublishing/Learn-CUDA-Programming/tree/master/Chapter10/10_deep_learning/01_ann
