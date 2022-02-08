# Optimizing Model Parameters

## Script 
```
cd $HOME/repositories/code/pytorch/examples/optimisation_tutorial
conda activate pytorchVE
python optimization_tutorial.py
``` 

## Issues
``` 
/home/mx19/anaconda3/envs/pytorchVE/lib/python3.8/site-packages/torchvision/datasets/mnist.py:498: UserWarning: The given NumPy array is not writeable, and PyTorch does not support non-writeable tensors. This means you can write to the underlying (supposedly non-writeable) NumPy array using the tensor. You may want to copy the array to protect its data or make it writeable before converting it to a tensor. This type of warning will be suppressed for the rest of this program. (Triggered internally at  /tmp/pip-req-build-pma2oi4d/torch/csrc/utils/tensor_numpy.cpp:180.)
```

>Changing line 498 in torchvision/datasets/mnist.py from
return torch.from_numpy(parsed.astype(m[2], copy=False)).view(*s)
to
return torch.from_numpy(parsed.astype(m[2])).view(*s)
removes the error.
> https://github.com/pytorch/vision/issues/4183

## References
https://pytorch.org/tutorials/beginner/basics/optimization_tutorial.html 
https://github.com/pytorch/tutorials/blob/master/beginner_source/basics/optimization_tutorial.py   

