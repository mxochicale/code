# Replicating PyTorch [Vision] — Binary Image Classification

## Conda environment 
Current [ve.yml](../../conda-virtual-environment/ve.yml) was migrated to [codeVE.yml](../../../conda/create-virtual-environments/codeVE.yml)

## Datasets
https://www.kaggle.com/dansbecker/hot-dog-not-hot-dog 
```
cd $HOME/datasets/hot-dog-not-hot-dog
tree -d
.
├── seefood
│   ├── test
│   │   ├── hot_dog
│   │   └── not_hot_dog
│   └── train
│       ├── hot_dog
│       └── not_hot_dog
├── test
│   ├── hot_dog
│   └── not_hot_dog
└── train
    ├── hot_dog
    └── not_hot_dog
```

## Script 
```
cd $HOME/repositories/code/pytorch/examples/binary_image_classification
conda activate codeVE
jupyter notebook
```

## Issues

## References
https://towardsdatascience.com/pytorch-vision-binary-image-classification-d9a227705cf9 
