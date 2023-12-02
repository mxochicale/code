import numpy as np
import h5py as h5

from vtkmodules.vtkCommonDataModel import (vtkDataObject,
                                            vtkPartitionedDataSet,
                                            vtkPolyData)
from vtkmodules.vtkFiltersGeneral import vtkGroupDataSetsFilter
from vtkmodules.vtkFiltersGeneral import vtkWarpScalar

from vtkmodules.vtkFiltersGeneral import vtkSpatioTemporalHarmonicsAttribute
#https://gitlab.kitware.com/vtk/vtk/-/blob/master/Filters/General/vtkSpatioTemporalHarmonicsAttribute.h

from vtkmodules.vtkFiltersHybrid import vtkGenerateTimeSteps
from vtkmodules.vtkFiltersSources import vtkSphereSource
from vtkmodules.util.numpy_support import vtk_to_numpy



sphere0 = vtkSphereSource()
sphere0.SetPhiResolution(30)
sphere0.SetThetaResolution(30)
sphere0.SetRadius(10)

sphere1 = vtkSphereSource()
sphere1.SetPhiResolution(30)
sphere1.SetThetaResolution(30)
sphere1.SetRadius(10)
sphere1.SetCenter(15, 15, 15)

# store the spheres in a single partitioned data set
groupDataSets = vtkGroupDataSetsFilter()
groupDataSets.AddInputConnection(sphere0.GetOutputPort())
groupDataSets.AddInputConnection(sphere1.GetOutputPort())
groupDataSets.SetOutputTypeToPartitionedDataSet()

# generate time steps
timeSteps = vtkGenerateTimeSteps()
timeSteps.SetInputConnection(groupDataSets.GetOutputPort())
timeValues = np.linspace(0.0, 2*np.pi, 100, endpoint=False)
timeSteps.SetTimeStepValues(100, timeValues)

# generate fields
addFields = vtkSpatioTemporalHarmonicsAttribute()
harmonics = np.array([
 	[1.0, 1.0, 0.6283, 0.6283, 0.6283, 0.0],
 	[3.0, 1.0, 0.6283, 0.0, 0.0, 1.5708],
 	[2.0, 2.0, 0.0, 0.6283, 0.0, 3.1416],
 	[1.0, 3.0, 0.0, 0.0, 0.6283, 4.7124]
 	])
for iH in range(harmonics.shape[0]):
	addFields.AddHarmonic(harmonics[iH, 0],
                      	harmonics[iH, 1],
                      	harmonics[iH, 2],
                      	harmonics[iH, 3],
                      	harmonics[iH, 4],
                      	harmonics[iH, 5])

addFields.SetInputConnection(timeSteps.GetOutputPort())

# warp spheres
warp = vtkWarpScalar()
warp.SetInputConnection(addFields.GetOutputPort())
warp.SetInputArrayToProcess(0, 0, 0,
                        	vtkDataObject.FIELD_ASSOCIATION_POINTS,
                        	'SpatioTemporalHarmonics')

# update the entire thing
warp.Update()
