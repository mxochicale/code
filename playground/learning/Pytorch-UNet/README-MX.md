# UNet: semantic segmentation with PyTorch

## Clone repository
```
git clone git@github.com:milesial/Pytorch-UNet.git
cd Pytorch-UNet/
rm -rf .git
``` 

## Setting up virtual environment
* [README](../../setting-virtual-environment/README.md)


## Download data in kaggle
Once register in kaggle, you can download data which is ~`24.43 GB`.
https://www.kaggle.com/c/carvana-image-masking-challenge/data  

## Set data paths
In train.py set `imgs_dir` `masks_dir`

You just have to make sure the path to your directories is correct, and it should end on "/" e.g.:
``` 
imgs_dir="../data/carvana-image-masking-challenge/train/"
masks_dir="../data/carvana-image-masking-challenge/train_masks/"
```
https://github.com/milesial/Pytorch-UNet/issues/155#issuecomment-693024341


## Issues
* `AssertionError: Either no mask or multiple masks found for the ID 90fdd8932877_06: []` sol:https://github.com/milesial/Pytorch-UNet/issues/242
```
    train_loader = DataLoader(train, batch_size=batch_size, shuffle=True, num_workers=1, pin_memory=False)
    val_loader = DataLoader(val, batch_size=batch_size, shuffle=False, num_workers=1, pin_memory=False, drop_last=True)
```