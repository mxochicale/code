# https://gist.github.com/ianliu/3e281d6fc523f9235b26c8d0674bc01e

import vtkmodules.vtkRenderingOpenGL2
#import vtk

from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

#import vtkmodules.qt 
#vtkmodules.qt.PyQtImpl = 'PySide6'
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkFiltersSources import vtkCylinderSource
from vtkmodules.vtkRenderingAnnotation import vtkCubeAxesActor
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
	vtkActor,
    	vtkPolyDataMapper,
	vtkRenderer
)


# every QT app needs an app
app = QApplication(['qt_ex'])
window = QWidget()
window.show()
#layout = QVBoxLayout()
#window.setLayout(layout)

cylinder = vtkCylinderSource()
cylinder.SetResolution(30)

cylinderMapper = vtkPolyDataMapper()
cylinderMapper.SetInputConnection(cylinder.GetOutputPort())


cylinderActor = vtkActor()
cylinderActor.SetMapper(cylinderMapper)


#axes = vtkCubeAxesActor()

ren = vtkRenderer()

#axes.SetBounds(-.1, .1, -.1, .1, -.1, .1)
#axes.SetCamera(ren.GetActiveCamera())
#axes.SetFlyModeToStaticTriad()

ren.AddActor(cylinderActor)
#ren.AddActor(axes)


widget = QVTKRenderWindowInteractor()
widget.AddObserver("ExitEvent", lambda o, e, a=app: a.quit())
#layout.addWidget(widget)

#renderer = vtkRenderer()
#widget.SetInteractorStyle(vtkInteractorStyleTrackballCamera())


# show the widget
#widget.show()
widget.Initialize()
widget.Start()
widget.GetRenderWindow().AddRenderer(ren)


# start event processing
app.exec()


