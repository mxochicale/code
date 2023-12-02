#https://gist.github.com/ianliu/3e281d6fc523f9235b26c8d0674bc01e
import vtk

renderer = vtk.vtkRenderer()
axes = vtk.vtkCubeAxesActor()
axes.SetBounds(-.1, .1, -.1, .1, -.1, .1)
axes.SetCamera(renderer.GetActiveCamera())
axes.SetFlyModeToStaticTriad()
renderer.AddActor(axes)

rw = vtk.vtkRenderWindow()
rw.AddRenderer(renderer)

iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(rw)
iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())

rw.Render()
iren.Start()
