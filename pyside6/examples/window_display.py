from PySide6.QtWidgets import QApplication, QWidget, QMainWindow
 
if __name__ == '__main__':
    app = QApplication(['Adding title of the window!!!'])
    window = QMainWindow()
    widget = QWidget()
    window.show()

    app.exec()
    print("Finalizing")
    