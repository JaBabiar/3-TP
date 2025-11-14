import sys
import this
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self, windw_name):
        super().__init__()
        self.setWindowTitle(windw_name)
        button = QPushButton("Press Me!")

        button.clicked.connect(lambda: self.open_settings(windw_name))

        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)

    def open_settings(self, name):
        window2 = MainWindow(f"{name} Settings")
        window2.show()


app = QApplication(sys.argv)

window = MainWindow("Steam")

window.show()

app.exec()