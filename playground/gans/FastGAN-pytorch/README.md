# A Fast and Stable GAN for Small and High Resolution Imagesets - pytorch
The official pytorch implementation of the paper "Towards Faster and Stabilized GAN Training for High-fidelity Few-shot Image Synthesis", the paper can be found [here](https://arxiv.org/abs/2101.04775).

## Clone repository
```
git clone git@github.com:odegeasslbc/FastGAN-pytorch.git
```

## -1. Setting up Virtual Environment
See [README.md](../00-setting-virtual-environments/README.md)


## 0. Data
The datasets used in the paper can be found at [link](https://drive.google.com/file/d/1aAJCZbXNHyraJ6Mi13dSbe7pTyfPXha0/view?usp=sharing).  
After testing on over 20 datasets with each has less than 100 images, this GAN converges on 80% of them.
I still cannot summarize an obvious pattern of the "good properties" for a dataset which this GAN can converge on, please feel free to try with your own datasets.


## 1. Description
The code is structured as follows:
* models.py: all the models' structure definition.

* operation.py: the helper functions and data loading methods during training.

* train.py: the main entry of the code, execute this file to train the model, the intermediate results and checkpoints will be automatically saved periodically into a folder "train_results".

* eval.py: generates images from a trained generator into a folder, which can be used to calculate FID score.

* benchmarking: the functions we used to compute FID are located here, it automatically downloads the pytorch official inception model. 

* lpips: this folder contains the code to compute the LPIPS score, the inception model is also automatically download from official location.

* scripts: this folder contains many scripts you can use to play around the trained model. Including: 
    1. style_mix.py: style-mixing as introduced in the paper;
    2. generate_video.py: generating a continuous video from the interpolation of generated images;
    3. find_nearest_neighbor.py: given a generated image, find the closest real-image from the training set;
    4. train_backtracking_one.py: given a real-image, find the latent vector of this image from a trained Generator.

    

## 2. How to run

### 2.1 Tweaking code
####  not support compare_ssim in skimage 0.18.2 #22 
* Changing the file lpips/init.py as follows
```
change default to: from skimage import measure (line 7)
change default to: return (1 - measure.compare_ssim(p0, p1, data_range=range, multichannel=True)) / 2. (line 53)
``` 
Reference: https://github.com/odegeasslbc/FastGAN-pytorch/issues/22


* Place all your training images in a folder, and simply call
```
python train.py --path /path/to/RGB-image-folder
```
* You can also see all the training options by:
```
python train.py --help
```

* Example on my machine 
```
conda activate pytorchVE 
cd playground\gans\FastGAN-pytorch
python train.py --help
```
Terminal output
```

(pytorchVE) mx19@sie085-lap:~/xfiles/code/playground/gans/FastGAN-pytorch$ python train.py --help
Setting up Perceptual loss...
Downloading: "https://download.pytorch.org/models/vgg16-397923af.pth" to /home/mx19/.cache/torch/checkpoints/vgg16-397923af.pth
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 528M/528M [01:04<00:00, 8.63MB/s]
Loading model from: /home/mx19/xfiles/code/playground/gans/FastGAN-pytorch/lpips/weights/v0.1/vgg.pth
...[net-lin [vgg]] initialized
...Done
usage: train.py [-h] [--path PATH] [--cuda CUDA] [--name NAME] [--iter ITER] [--start_iter START_ITER] [--batch_size BATCH_SIZE] [--im_size IM_SIZE] [--ckpt CKPT]

region gan
                          
``` 


* Example 
``` 
conda activate pytorchVE
cd playground\gans\FastGAN-pytorch
python train.py --cuda 1 --iter 1000 --batch_size 5 --path /home/mx19/datasets/few-shot-images/100-shot-grumpy_cat

 
Setting up Perceptual loss...
Loading model from: /home/mx19/xfiles/code/playground/gans/FastGAN-pytorch/lpips/weights/v0.1/vgg.pth
...[net-lin [vgg]] initialized
...Done
Namespace(batch_size=5, ckpt='None', cuda=1, im_size=1024, iter=1000, name='test1', path='/home/mx19/datasets/few-shot-images/100-shot-grumpy_cat', start_iter=0)
  0%|                                                                                                                                                                | 0/1001 [00:00<?, ?it/s]
 iteration: 0
GAN: loss d: 0.04283    loss g: -0.41895
  0%|▏                                                                                                                                                       | 1/1001 [00:01<30:02,  1.80s/it]
 iteration: 1
  0%|▎                                                                                                                                                       | 2/1001 [00:02<20:31,  1.23s/it]
 iteration: 2
  0%|▍                                                                                                                                                       | 3/1001 [00:03<17:03,  1.03s/it]



...


: 994
 99%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ | 995/1001 [16:34<00:06,  1.02s/it]
 iteration: 995
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▎| 996/1001 [16:35<00:05,  1.02s/it]
 iteration: 996
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▍| 997/1001 [16:36<00:04,  1.03s/it]
 iteration: 997
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▌| 998/1001 [16:37<00:03,  1.03s/it]
 iteration: 998
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▋| 999/1001 [16:38<00:02,  1.04s/it]
 iteration: 999
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████▊| 1000/1001 [16:39<00:01,  1.03s/it]
 iteration: 1000
GAN: loss d: 0.49730    loss g: -1.67313
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1001/1001 [16:41<00:00,  1.00s/it]
(pytorchVE) mx19@sie085-lap:~/xfiles/code/playground/gans/FastGAN-pytorch$ 


# OR


conda activate pytorchVE
cd playground\gans\FastGAN-pytorch
python train.py --cuda 1 --iter 9000 --batch_size 5 --path /home/mx19/datasets/few-shot-images/100-shot-grumpy_cat


Setting up Perceptual loss...
Loading model from: /home/mx19/xfiles/code/playground/gans/FastGAN-pytorch/lpips/weights/v0.1/vgg.pth
...[net-lin [vgg]] initialized
...Done
Namespace(batch_size=5, ckpt='None', cuda=1, im_size=1024, iter=9000, name='test1', path='/home/mx19/datasets/few-shot-images/100-shot-grumpy_cat', start_iter=0)
  0%|                                                                                                                                                                | 0/9001 [00:00<?, ?it/s]
 iteration: 0
GAN: loss d: 0.27591    loss g: -0.51711
  0%|                                                                                                                                                      | 1/9001 [00:01<3:54:12,  1.56s/it]
 iteration: 1
  0%|                                                                            

...


                                                           | 1646/9001 [26:22<1:56:44,  1.05it/s]
 iteration: 1646
 18%|██████████████████████████▉                                                                                                                        | 1647/9001 [26:23<1:57:03,  1.05it/s]
 iteration: 1647
 18%|██████████████████████████▉                                                                                                                        | 1648/9001 [26:24<1:56:28,  1.05it/s]
 iteration: 1648
 18%|██████████████████████████▉                                                                                                                        | 1649/9001 [26:25<1:56:06,  1.06it/s]
 iteration: 1649
 18%|██████████████████████████▉                                                                                                                        | 1650/9001 [26:26<1:52:19,  1.09it/s]
 iteration: 1650
 18%|██████████████████████████▉                                                                                                                        | 1651/9001 [26:27<1:53:43,  1.08it/s]
 iteration: 1651
 18%|██████████████████████████▉                                                                                                                        | 1652/9001 [26:27<1:55:08,  1.06it/s]
 iteration: 1652


... 


just cancell it 

```


The code will automatically create a new folder (you have to specify the name of the folder using --name option) to store the trained checkpoints and intermediate synthesis results.

Once finish training, you can generate 100 images (or as many as you want) by:
```
cd ./train_results/name_of_your_training/
python eval.py --n_sample 100 
```

* Modify `eval.py`
```
    for epoch in [10*i for i in range(args.start_iter, args.end_iter+1)]:
        ckpt = 'models/%d.pth'%(epoch)
        checkpoint = torch.load(ckpt, map_location=lambda a,b: a)
        net_ig.load_state_dict(checkpoint['g'])
        #load_params(net_ig, checkpoint['g_ema'])

```

* Example to run the evaluation 
```
conda activate pytorchVE
cd train_results/test1/

$ python eval.py --n_sample 1000 --start_iter 100 --end_iter 100
load checkpoint success, epoch 1000
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 62/62 [02:05<00:00,  2.02s/it]
  
```


* See generated images
``` 
cd playground/gans/FastGAN-pytorch/train_results/test1/eval_1000/img
eog *
```



## 3. Pre-trained models
The pre-trained models and the respective code of each model are shared [here](https://drive.google.com/drive/folders/1nCpr84nKkrs9-aVMET5h8gqFbUYJRPLR?usp=sharing).

You can also use FastGAN to generate images with a pre-packaged Docker image, hosted on the Replicate registry: https://beta.replicate.ai/odegeasslbc/FastGAN

## 4. Important notes
1. The provided code is for research use only.
2. Different model and training configurations are needed on different datasets. You may have to tune the hyper-parameters to get the best results on your own datasets. 

    2.1. The hyper-parameters includes: the augmentation options, the model depth (how many layers), the model width (channel numbers of each layer). To change these, you have to change the code in models.py and train.py directly. 
    
    2.2. Please check the code in the shared pre-trained models on how each of them are configured differently on different datasets. Especially, compare the models.py for ffhq and art datasets, you will get an idea on what chages could be made on different datasets.

## 5. Other notes
1. The provided scripts are not well organized, contributions are welcomed to clean them.
2.  An third-party implementation of this paper can be found [here](https://github.com/lucidrains/lightweight-gan), where some other techniques are included. I suggest you try both implementation if you find one of them does not work. 
