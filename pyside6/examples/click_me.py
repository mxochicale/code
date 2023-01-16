# https://doc.qt.io/qtforpython/tutorials/basictutorial/clickablebutton.html
import sys
import PySide6.QtCore

# Prints PySide6 version
print(PySide6.__version__)

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__)

from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot


@Slot()
def say_hello():
	print("Button clicked, Hello!")
                                            
if __name__ == "__main__":
	# Create the Qt Application
	app = QApplication(sys.argv)

	# Create a button, connect it and show it
	button = QPushButton("Click me")
	button.clicked.connect(say_hello)
	button.show()
	
	# Run the main Qt loop
	app.exec()

