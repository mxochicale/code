# Froggie and the Joy of Open Source Community
https://www.kitware.com/froggie-and-the-joy-of-open-source-community/

> The code uses a general way of specifying transformations that can permute image and other geometric data in order to maintain proper orientation regardless of the acquisition order. See the class SliceOrder.

> The dataset was prepared at the Lawrence Berkeley National Laboratories. It is included with their permission. The data was acquired by physically slicing the frog and photographing the slices. The original segmented data is in the form of tissue masks with one file per tissue. There are 136 slices per tissue and 15 different tissues. Each slice is 470 by 500 pixels.


## Running example 
* Run example
```
python FroggieSurface.py Frog_mhd.json
python FroggieView.py Frog_vtk.json
```
* Download data
wget https://gitlab.kitware.com/vtk/vtk-examples/-/archive/master/vtk-examples-master.zip?path=src/Testing/Data/Frog -O frog
* Tree 
```.
├── Frog
│   ├── blood.vtk
│   ├── brainbin.vtk
│   ├── brain.vtk
│   ├── duodenum.vtk
│   ├── eye_retna.vtk
│   ├── eye_white.vtk
│   ├── frog.mhd
│   ├── frogtissue.mhd
│   ├── frogtissue.zraw
│   ├── frog.zraw
│   ├── heart.vtk
│   ├── ileum.vtk
│   ├── kidney.vtk
│   ├── l_intestine.vtk
│   ├── liver.vtk
│   ├── lung.vtk
│   ├── nerve.vtk
│   ├── skeleton.vtk
│   ├── skin.vtk
│   ├── spleen.vtk
│   ├── stomach.vtk
│   └── vtk-examples-master-src-Testing-Data-Frog.zip
├── FroggieSurface.py
├── FroggieView.py
├── Frog_mhd.json
├── Frog_vtk.json
└── README.md

1 directory, 27 files
```


