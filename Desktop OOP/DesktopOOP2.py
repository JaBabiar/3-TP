import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle("Lekcja 2")

        self.button = QPushButton("Kliknij")
        # Ustawiamy tryb checkbox na przycisku
        self.button.setCheckable(True)
        # Nadajemy funkcję która ma się wykonać podczas kliknięcia (Można nadać wiele funkcji do jednej akcji
        self.button.clicked.connect(self.btn_clicked)
        self.button.clicked.connect(self.btn_check)
        # Gdy przycisk jest odciśnięty
        self.button.released.connect(self.btn_rel)
        # Ustawiamy zmienną
        self.button.setChecked(self.button_is_checked)
        self.setCentralWidget(self.button)

    def btn_clicked(self):
        print("Klik")
    def btn_check(self, checked):
        print(checked)
    def btn_rel(self):
        self.button_is_checked = self.button.isChecked()

        print(self.button_is_checked)

### Koniec Klasy
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()