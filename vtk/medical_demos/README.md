# Medical demos
https://examples.vtk.org/site/Python/#medical

## Download files
* FullHead.mhd references FullHead.raw.gz

```
wget https://gitlab.kitware.com/vtk/vtk-examples/-/raw/master/src/Testing/Data/FullHead.mhd
wget https://gitlab.kitware.com/vtk/vtk-examples/-/raw/master/src/Testing/Data/FullHead.raw.gz

wget https://gitlab.kitware.com/vtk/vtk-examples/-/raw/master/src/Python/Medical/TissueLens.py
wget https://gitlab.kitware.com/vtk/vtk-examples/-/raw/master/src/Python/Medical/MedicalDemo1.py
wget https://gitlab.kitware.com/vtk/vtk-examples/-/raw/master/src/Python/Medical/MedicalDemo2.py
wget https://gitlab.kitware.com/vtk/vtk-examples/-/raw/master/src/Python/Medical/MedicalDemo3.py
wget https://gitlab.kitware.com/vtk/vtk-examples/-/raw/master/src/Python/Medical/MedicalDemo4.py
```

## Running app
```
python MedicalDemo1.py FullHead.mhd #Create a skin surface from volume data.
python MedicalDemo2.py FullHead.mhd #Create a skin and bone surface from volume data.
python MedicalDemo3.py FullHead.mhd #Create skin, bone and slices from volume data.
python MedicalDemo4.py FullHead.mhd #Create a volume rendering.
python TissueLens.py FullHead.mhd   #Cut a volume with a sphere.
```




