# VTKHDF files
https://www.kitware.com/how-to-write-time-dependent-data-in-vtkhdf-files/
>  October 27, 2023; Lucas Givord and Julien Fausty
> It can be read into VTK or ParaView master at the moment and will be available in the next release of both : VTK 9.3.0 and ParaView 5.12.0.

## Application
python vtkpython.py 

## issues
* python=3.10 with vtk>=9.3.0 in bareVE.yaml; 
* python=3.11 with vtk>=9.3.0 in bareVE.yaml; 
* python=3.9 with vtk>=9.3.0 in bareVE.yaml; 
* python=3.9 with  - vtk>=9.2.5 in bareVE.yaml; 
* python=3.9 with  - vtk>=9.2.0 in bareVE.yaml; 
* python=3.8 with  - vtk>=9.2.0 in bareVE.yaml; 


```
Traceback (most recent call last):
  File "/home/mxochicale/repositories/mxochicale/code/vtk/vtkhdf/vtkpython.py", line 3, in <module>
    from vtkmodules.vtkFiltersGeneral import (vtkGroupDataSetsFilter,
ImportError: cannot import name 'vtkSpatioTemporalHarmonicsAttribute' from 'vtkmodules.vtkFiltersGeneral' (/home/mxochicale/mambaforge/envs/bareVE/lib/python3.10/site-packages/vtkmodules/vtkFiltersGeneral.cpython-310-x86_64-linux-gnu.so)
ImportError: cannot import name 'vtkSpatioTemporalHarmonicsAttribute' from 'vtkmodules.vtkFiltersGeneral' (/home/mxochicale/mambaforge/envs/bareVE/lib/python3.9/site-packages/vtkmodules/vtkFiltersGeneral.cpython-39-x86_64-linux-gnu.so)
ImportError: cannot import name 'vtkSpatioTemporalHarmonicsAttribute' from 'vtkmodules.vtkFiltersGeneral' (/home/mxochicale/mambaforge/envs/bareVE/lib/python3.9/site-packages/vtkmodules/vtkFiltersGeneral.cpython-39-x86_64-linux-gnu.so)
ImportError: cannot import name 'vtkSpatioTemporalHarmonicsAttribute' from 'vtkmodules.vtkFiltersGeneral' (/home/mxochicale/mambaforge/envs/bareVE/lib/python3.11/site-packages/vtkmodules/vtkFiltersGeneral.cpython-311-x86_64-linux-gnu.so)
```


