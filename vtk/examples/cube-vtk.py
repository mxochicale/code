## References 
### PAGE15 https://mt4sd.ulpgc.es/slicer-int/images/7/71/VTK.pdf
### step5.py https://kitware.github.io/vtk-examples/site/Python/#tutorial

import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkFiltersSources import vtkCubeSource
from vtkmodules.vtkInteractionStyle import vtkInteractorStyleTrackballCamera
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)

def main():
    ##SOURCE/READER
    # Create an interactor
    cube = vtkCubeSource()
    polyData = cube.GetOutput()
    #print(polyData)

    ##MAPPER
    cubeMapper = vtkPolyDataMapper()
    cubeMapper.SetInputConnection(cube.GetOutputPort())

    ##ACTOR
    cubeActor = vtkActor()
    cubeActor.SetMapper(cubeMapper)
    cubeActor.GetProperty().SetColor(1.0, 0.0, 0.0) # make the cube red

    ##RENDERER
    ### Create a renderer and add the cube actor to it
    renderer = vtkRenderer()
    renderer.AddActor(cubeActor)
    renderer.SetBackground(0.0, 0.0, 0.0)  # make the background black

    ##Render window
    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer) 
    renderWindow.SetSize(500, 500)
    renderWindow.SetWindowName('Tutorial_Step1')

    # The vtkRenderWindowInteractor class watches for events (e.g., keypress,
    # mouse) in the vtkRenderWindow. These events are translated into
    # event invocations that VTK understands (see VTK/Common/vtkCommand.h
    # for all events that VTK processes). Then observers of these VTK
    # events can process them as appropriate.
    iterator_renderer = vtkRenderWindowInteractor()
    iterator_renderer.SetRenderWindow(renderWindow)

    # By default the vtkRenderWindowInteractor instantiates an instance
    # of vtkInteractorStyle. vtkInteractorStyle translates a set of events
    # it observes into operations on the camera, actors, and/or properties
    # in the vtkRenderWindow associated with the vtkRenderWinodwInteractor.
    # Here we specify a particular interactor style.
    style = vtkInteractorStyleTrackballCamera()
    iterator_renderer.SetInteractorStyle(style)


    # The user can use the mouse
    # and keyboard to perform the operations on the scene according to the
    # current interaction style. When the user presses the 'e' key, by default
    # an ExitEvent is invoked by the vtkRenderWindowInteractor which is caught
    # and drops out of the event loop (triggered by the Start() method that
    # follows.
    # You can also use
    # q to quit
    # w to show lines
    # 3 to swap colours 
    iterator_renderer.Initialize()
    iterator_renderer.Start()


if __name__ == '__main__':
    main()
