# https://doc.qt.io/qtforpython/quickstart.html
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.text)

        self.button.clicked.connect(self.random_choice_of_hello_string)

    @QtCore.Slot()
    def random_choice_of_hello_string(self):
        self.text.setText(random.choice(self.hello))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 200)
    widget.show()

    sys.exit(app.exec())
