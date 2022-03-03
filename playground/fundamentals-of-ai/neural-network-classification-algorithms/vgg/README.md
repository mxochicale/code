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
Got 5730 / 10000 with accuracy 57.30
Loss in epoch 2 :::: 0.9707437125682831
Got 6896 / 10000 with accuracy 68.96
Loss in epoch 3 :::: 0.756159718132019
Got 7264 / 10000 with accuracy 72.64
Loss in epoch 4 :::: 0.6058241069316864
Got 7383 / 10000 with accuracy 73.83
Loss in epoch 5 :::: 0.47915516843795775
Got 7692 / 10000 with accuracy 76.92
Loss in epoch 6 :::: 0.37425202519893647
Got 7803 / 10000 with accuracy 78.03
Loss in epoch 7 :::: 0.2807335279405117
Got 7740 / 10000 with accuracy 77.40
Loss in epoch 8 :::: 0.22346274626255036
Got 7844 / 10000 with accuracy 78.44
Loss in epoch 9 :::: 0.17847996798157692
Got 7848 / 10000 with accuracy 78.48
Loss in epoch 10 :::: 0.14781020445227622
Got 7872 / 10000 with accuracy 78.72
Loss in epoch 11 :::: 0.12325876159518957
Got 7940 / 10000 with accuracy 79.40
Loss in epoch 12 :::: 0.10356270266547798
Got 7933 / 10000 with accuracy 79.33
Loss in epoch 13 :::: 0.09814273201748729
Got 7923 / 10000 with accuracy 79.23
Loss in epoch 14 :::: 0.08814270719140768
Got 7910 / 10000 with accuracy 79.10
Loss in epoch 15 :::: 0.07574469480589033
Got 7857 / 10000 with accuracy 78.57
Loss in epoch 16 :::: 0.06981589934211224
Got 7871 / 10000 with accuracy 78.71
Loss in epoch 17 :::: 0.06362842797357589
Got 7967 / 10000 with accuracy 79.67
Loss in epoch 18 :::: 0.06208857551068068
Got 7821 / 10000 with accuracy 78.21
Loss in epoch 19 :::: 0.058485132415592674
Got 7953 / 10000 with accuracy 79.53
Loss in epoch 20 :::: 0.050276186327822506
Got 7964 / 10000 with accuracy 79.64
Loss in epoch 21 :::: 0.04976917912792415
Got 8009 / 10000 with accuracy 80.09
Loss in epoch 22 :::: 0.04382371689006686
Got 7958 / 10000 with accuracy 79.58
Loss in epoch 23 :::: 0.04912403560187668
Got 7913 / 10000 with accuracy 79.13
Loss in epoch 24 :::: 0.04194094930868596
Got 7951 / 10000 with accuracy 79.51
Loss in epoch 25 :::: 0.0421104849240277
Got 7971 / 10000 with accuracy 79.71
Loss in epoch 26 :::: 0.0378722396737081
Got 7925 / 10000 with accuracy 79.25
Loss in epoch 27 :::: 0.035903563880547884
Got 7943 / 10000 with accuracy 79.43
Loss in epoch 28 :::: 0.036991838415525856
Got 7897 / 10000 with accuracy 78.97
Loss in epoch 29 :::: 0.03549494900521822
Got 7953 / 10000 with accuracy 79.53
Loss in epoch 30 :::: 0.03304938904424198
Got 7946 / 10000 with accuracy 79.46
Loss in epoch 31 :::: 0.03349702634196729
Got 7939 / 10000 with accuracy 79.39
Loss in epoch 32 :::: 0.03107016664966941
Got 7900 / 10000 with accuracy 79.00
Loss in epoch 33 :::: 0.032933122889185325
Got 8014 / 10000 with accuracy 80.14
Loss in epoch 34 :::: 0.030072895263740792
Got 8038 / 10000 with accuracy 80.38
Loss in epoch 35 :::: 0.028162019508471713
Got 7974 / 10000 with accuracy 79.74
Loss in epoch 36 :::: 0.02891350651467219
Got 7913 / 10000 with accuracy 79.13
Loss in epoch 37 :::: 0.026545191328576766
Got 7926 / 10000 with accuracy 79.26
Loss in epoch 38 :::: 0.023882066421443596
Got 7909 / 10000 with accuracy 79.09
Loss in epoch 39 :::: 0.02651701272971113
Got 7982 / 10000 with accuracy 79.82
Loss in epoch 40 :::: 0.026040794279472902
Got 7952 / 10000 with accuracy 79.52
Loss in epoch 41 :::: 0.024371529390104115
Got 8000 / 10000 with accuracy 80.00
Loss in epoch 42 :::: 0.025139389837905764
Got 7974 / 10000 with accuracy 79.74
Loss in epoch 43 :::: 0.024507477929710877
Got 7940 / 10000 with accuracy 79.40
Loss in epoch 44 :::: 0.023659181051084305
Got 7944 / 10000 with accuracy 79.44
Loss in epoch 45 :::: 0.02191463044389384
Got 7958 / 10000 with accuracy 79.58
Loss in epoch 46 :::: 0.02567893305339385
Got 7986 / 10000 with accuracy 79.86
Loss in epoch 47 :::: 0.02088426975227485
Got 7993 / 10000 with accuracy 79.93
Loss in epoch 48 :::: 0.023486072013291413
Got 7913 / 10000 with accuracy 79.13
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

