# Replicating VGG16.ipynb

## Conda environment 
Current [ve.yml](../../conda-virtual-environment/ve.yml) was migrated to [codeVE.yml](../../../conda/create-virtual-environments/codeVE.yml)

## Datasets
https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz

## Script 
```
cd $HOME/repositories/code/playground/fundamentals-of-ai/neural-network-classification-algorithms/vgg
conda activate codeVE
jupyter notebook
```

## Notes

### EPOCHS = 50 executed in 4h 23m 36s, finished 23:15:14 2022-02-28
``` 
Loss in epoch 0 :::: 1.822487028503418
Got 4458 / 10000 with accuracy 44.58
Loss in epoch 1 :::: 1.3144953930854797
...
Loss in epoch 49 :::: 0.022338543514224877
Got 7881 / 10000 with accuracy 78.81
```

Saved model: `513M Mar  1 04:57 vgg16_cifar.pt`

### `for batch_idx, (data,targets) in enumerate(test_dl):` executed in 9m 11s, finished 10:48:24 2022-03-02 [CPU]; executed in 23.9s, finished 11:06:07 2022-03-02 [GPU]

```
Got 7906 / 10000 with accuracy 79.06 [CPU]
Got 7920 / 10000 with accuracy 79.20 [GPU]
```


### EPOCHS = 1 executed in 5m 17s, finished 09:00:56 2022-03-03
``` 

Loss in epoch 0 :::: 1.7990044103622436
Got 4655 / 10000 with accuracy 46.55

Saved model `513M Mar  3 09:02 vgg16_cifar_TMP.pt`
```



## Issues

## References

https://github.com/Ti-Oluwanimi/Neural-Network-Classification-Algorithms/blob/main/VGG16.ipynb

https://debuggercafe.com/implementing-vgg11-from-scratch-using-pytorch/  

https://medium.com/@tioluwaniaremu/vgg-16-a-simple-implementation-using-pytorch-7850be4d14a1  
> Also, since VGG16 is a much deeper model and has 138 million parameters, 
> it is worthy to say that you will be needing 
> 14 cups of coffee while training the model from scratch.


https://medium.com/analytics-vidhya/alexnet-a-simple-implementation-using-pytorch-30c14e8b6db2 

https://towardsdatascience.com/the-w3h-of-alexnet-vggnet-resnet-and-inception-7baaaecccc96
> AlexNet and ResNet-152, both have about 60M parameters but there is about a 10% difference in their top-5 accuracy. 
> But training a ResNet-152 requires a lot of computations (about 10 times more than that of AlexNet) which means 
> more training time and energy required.

> VGGNet not only has a higher number of parameters and FLOP as compared to ResNet-152 
> but also has a decreased accuracy. It takes more time to train a VGGNet with reduced accuracy.

> Training an AlexNet takes about the same time as training Inception. 
> The memory requirements are 10 times less with improved accuracy (about 9%)


https://sofiadutta.github.io/datascience-ipynbs/pytorch/Image-Classification-using-PyTorch.html

https://www.stefanfiott.com/machine-learning/cifar-10-classifier-using-cnn-in-pytorch/
