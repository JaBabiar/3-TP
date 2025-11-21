import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        ## W przypadku użycia klasy PyQt zawsze trzeba wykorzystać
        ## super().__init__() by funkcja miała dostęp do metod
        super().__init__()

        # Zmiana tytułu na Lekcja 1
        self.setWindowTitle("Lekcja 1")
        # Dodanie przycisku Kliknij
        self.button = QPushButton("Kliknij")
        # Ustawienie stałego rozmiaru za pomocą
        # self.setFixedSize(QSize(400, 300))
        # Ustawienie min/max rozmiaru
        self.button.setMinimumSize(100,50)
        self.button.setMaximumSize(200,100)


        # Dodanie przycisku na środek QMainWindow (podstawowo rozszerza na 100%)
        self.setCentralWidget(self.button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()