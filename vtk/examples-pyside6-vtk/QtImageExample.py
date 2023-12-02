# coding=utf-8
"""
Example of displaying an image with VTK/Qt/Python.

Original author: David Gobbi

This example does not include proper image orientation or interaction.
"""

import sys
import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication

from vtk import vtkImageSlice, vtkImageSliceMapper, vtkImageProperty
from vtk import vtkRenderer, vtkRenderWindow, vtkRenderWindowInteractor
from vtk import vtkInteractorStyleImage
from vtk import vtkNIFTIImageReader
from vtk import vtkImageHistogramStatistics

#from QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

def QVTKRenderWidgetImageExample(argv):
    """A simple example that uses the QVTKRenderWindowInteractor class."""

    if len(argv) < 2:
        sys.stderr.write(
            "This program needs a nifti file as its first argument\n")
        sys.exit(1)

    filename = argv[1]

    # make sure image is readable before doing anything else
    reader = vtkNIFTIImageReader()
    reader.SetFileName(filename)
    reader.Update()
    image = reader.GetOutput()

    # prefer the nifti "qform", use "sform" as a backup
    matrix = reader.GetQFormMatrix()
    if matrix is None:
        matrix = reader.GetSFormMatrix()

    # find a robust min, max range from the histogram
    histinfo = vtkImageHistogramStatistics()
    histinfo.SetInputData(image)
    histinfo.Update()
    minval, maxval = histinfo.GetAutoRange()
    print("Image range: [%g, %g]" % (minval, maxval))

    # every QT app needs an app object
    app = QApplication(['QVTKRenderWindowInteractor'])

    # create the widget
    widget = QVTKRenderWindowInteractor()
    widget.Initialize()
    widget.Start()

    # if you don't want the 'q' key to exit, comment this out
    widget.AddObserver("ExitEvent", lambda o, e, a=app: a.quit())

    # attach renderer to the display
    renderer = vtkRenderer()
    widget.GetRenderWindow().AddRenderer(renderer)

    # the mapper
    mapper = vtkImageSliceMapper()
    mapper.SetInputData(image)
    mapper.SliceAtFocalPointOn()

    # the actor
    actor = vtkImageSlice()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColorWindow(maxval - minval)
    actor.GetProperty().SetColorLevel(0.5*(minval + maxval))
    renderer.AddActor(actor)

    # set up the camera
    camera = renderer.GetActiveCamera()
    bounds = image.GetBounds()
    xc = 0.5*(bounds[0] + bounds[1])
    yc = 0.5*(bounds[2] + bounds[3])
    zc = 0.5*(bounds[4] + bounds[5])
    camera.SetFocalPoint(xc, yc, zc)
    camera.SetPosition(xc, yc, bounds[5] + 1.0)
    camera.SetViewUp(0.0, -1.0, 0.0)
    camera.ParallelProjectionOn()
    camera.SetParallelScale(0.5*(bounds[3]-bounds[2]))

    # show the widget
    widget.show()
    # start event processing
    app.exec()

if __name__ == "__main__":
    QVTKRenderWidgetImageExample(sys.argv)
