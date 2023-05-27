
# https://www.xingyulei.com/post/qt-threading/index.html

import time
import sys

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLineEdit, QGridLayout
)


class Window(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        # ui setup: please ignore
        widget = QWidget()
        layout = QGridLayout()

        button = QPushButton('run task!')
        button.clicked.connect(self.run_long_task)
        edit = QLineEdit()

        layout.addWidget(edit, 0, 0)
        layout.addWidget(button, 1, 0)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def run_long_task(self):
        time.sleep(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
Here
