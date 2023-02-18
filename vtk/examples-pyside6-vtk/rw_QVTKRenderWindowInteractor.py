# https://stackoverflow.com/questions/69200800/pyqt5-and-vtk-object-integration
# https://github.com/KhronosGroup/glTF-Sample-Models/blob/master/2.0/Fox/glTF-Binary/Fox.glb

# TO EXPLORE
#https://stackoverflow.com/questions/64094386/can-i-add-paraviews-renderer-or-interactor-to-my-pyqt5-application
##https://python.hotexamples.com/examples/vtk.qt4.QVTKRenderWindowInteractor/QVTKRenderWindowInteractor/-/python-qvtkrenderwindowinteractor-class-examples.html


import sys
import vtk
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QMainWindow
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(190, 300, 300, 200)
        self.setWindowTitle("Simple menu")

        self.container = QWidget()
        vl = QVBoxLayout(self.container)
        self.setCentralWidget(self.container)
        self.resize(640, 480)

        importer = vtk.vtkGLTFImporter()
        importer.SetFileName('Fox.glb')
        importer.Read()
        renderer = importer.GetRenderer()
        render_window = importer.GetRenderWindow()

        vtk_widget = QVTKRenderWindowInteractor(rw=render_window)
        vtk_widget.AddObserver("ExitEvent", lambda o, e, a=app: a.quit())
        vl.addWidget(vtk_widget)
        vtk_widget.Initialize()
        vtk_widget.Start()

        colors = vtk.vtkNamedColors()
        renderer.SetBackground(colors.GetColor3d("White"))

        renderer.ResetCamera()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Menu()
    ex.show()
    sys.exit(app.exec())
