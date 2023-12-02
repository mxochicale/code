# https://stackoverflow.com/questions/56883979/qwidgets-grab-method-doesnt-work-on-a-qvtkrenderwindowinteractor-object

#import vtk
import vtkmodules.vtkRenderingOpenGL2
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6 import QtCore

from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkFiltersSources import vtkCylinderSource
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    #vtkRenderWindow,
    #vtkRenderWindowInteractor,
    vtkRenderer
)


def QVTKRenderWidgetExample():
	"""A simple example that uses the QVTKRenderWindowInteractor class."""
	
	# every QT app needs an app
	app = QApplication(['QVTKRenderWindowInteractor'])
	window = QWidget()
	window.show()
	layout = QVBoxLayout()
	window.setLayout(layout)


	cylinder = vtkCylinderSource()
	cylinder.SetResolution(6)
	
	cylinderMapper = vtkPolyDataMapper()
	cylinderMapper.SetInputConnection(cylinder.GetOutputPort())
	
	cylinderActor = vtkActor()
	cylinderActor.SetMapper(cylinderMapper)

	
	# Create renderer and populate the vtk widget
	ren = vtkRenderer()
	ren.AddActor(cylinderActor)

	w_vtk = QVTKRenderWindowInteractor()
	w_vtk.AddObserver("ExitEvent", lambda o, e, a=app: a.quit())
	layout.addWidget(w_vtk)
	w_vtk.Initialize()
	w_vtk.Start()
	w_vtk.GetRenderWindow().AddRenderer(ren)
	
	# Add print screen button
	button = QPushButton("Print")
	text = QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)
	layout.addWidget(button)
	layout.addWidget(text)

	
	# start event processing
	# Source: https://doc.qt.io/qtforpython/porting_from2.html
	# 'exec_' is deprecated and will be removed in the future.
	# Use 'exec' instead.
	try:
		app.exec()
	except AttributeError:
		app.exec()

if __name__ == "__main__":
    QVTKRenderWidgetExample()
