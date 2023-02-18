# https://gitlab.kitware.com/vtk/vtk/-/blob/master/Wrapping/Python/vtkmodules/qt/QVTKRenderWindowInteractor.py

import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkFiltersSources import vtkConeSource
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)


def VTKRenderWidgetConeExample():
    """A simple example that uses the VTKRenderWindowInteractor class."""

    colors = vtkNamedColors()

    cone = vtkConeSource()
    cone.SetResolution(100)

    coneMapper = vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    coneActor = vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.GetProperty().SetColor(colors.GetColor3d("Tomato"))
    coneActor.RotateZ(60.0)

    # Create the graphics structure. The renderer renders into the render
    # window. The render window interactor captures mouse events and will
    # perform appropriate camera or actor manipulation depending on the
    # nature of the events. 
    ren = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Add the actors to the renderer, set the background and size
    ren.AddActor(coneActor)
    renWin.SetSize(500, 500)
    renWin.SetWindowName('CylinderExample')


    # This allows the interactor to initalize itself. It has to be
    # called before an event loop.
    iren.Initialize()

    # Start the event loop.
    iren.Start()


if __name__ == "__main__":
    VTKRenderWidgetConeExample()
