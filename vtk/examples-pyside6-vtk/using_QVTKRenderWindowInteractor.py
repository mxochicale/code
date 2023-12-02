# https://gitlab.kitware.com/vtk/vtk/-/blob/master/Wrapping/Python/vtkmodules/qt/QVTKRenderWindowInteractor.py

#import vtk
import vtkmodules.vtkRenderingOpenGL2
from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
from vtkmodules.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    #vtkRenderWindow,
    #vtkRenderWindowInteractor,
    vtkRenderer
)


def QVTKRenderWidgetConeExample():
    """A simple example that uses the QVTKRenderWindowInteractor class."""

    # every QT app needs an app
    app = QApplication(['QVTKRenderWindowInteractor'])
    #window = QWidget()
    #window = QMainWindow()

    # create the widget
    widget = QVTKRenderWindowInteractor()
    #widget = QVTKRenderWindowInteractor(window)
    #window.setCentralWidget(widget)

    # To color actors
    colors = vtkNamedColors()

    cone = vtkConeSource()
    cone.SetResolution(100)

    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(colors.GetColor3d("Tomato"))
    coneActor.RotateZ(60.0)

    ren = vtkRenderer()
    widget.GetRenderWindow().AddRenderer(ren)
    ##if you dont want the 'q' key to exit comment this.
    widget.AddObserver("ExitEvent", lambda o, e, a=app: a.quit())


    # Add the actors to the renderer
    ren.AddActor(coneActor)

    # show the widget
    widget.show()

    # This allows the interactor to initalize itself. It has to be
    # called before an event loop.
    widget.Initialize()
    # Start the event loop.
    widget.Start()


    # start event processing
    # Source: https://doc.qt.io/qtforpython/porting_from2.html
    # 'exec_' is deprecated and will be removed in the future.
    # Use 'exec' instead.
    try:
        app.exec()
    except AttributeError:
        app.exec()


if __name__ == "__main__":
    QVTKRenderWidgetConeExample()
