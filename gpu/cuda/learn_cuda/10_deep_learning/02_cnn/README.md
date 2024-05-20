# CNN

## Compiling
```
bash download_mnist.sh
make
./train
```

## errors
```
train: src/mnist.cpp:37: void cudl::MNIST::load_data(std::string&): Assertion `(magic_number & 0xFFF) == 0x803' failed.
```

