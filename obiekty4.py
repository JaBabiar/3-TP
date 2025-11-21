import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QLabel, QVBoxLayout, QLineEdit, QMainWindow
)
from PyQt6.QtCore import Qt


class AplikacjaGreeter(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

        self.polaczSygnaly()

    def initUI(self):
        """Metoda pomocnicza do budowania interfejsu."""
        self.setWindowTitle("Sygnały i Sloty")

        # Tworzymy komponenty (atrybuty 'self')
        self.etykieta_instrukcji = QLabel("Wpisz swoje imię:")
        self.pole_tekstowe = QLineEdit()
        self.przycisk_przywitaj = QPushButton("Przywitaj!")
        self.etykieta_wyniku = QLabel("...")

        # Ustawiamy czcionkę dla wyniku, żeby był większy
        font = self.etykieta_wyniku.font()
        font.setPointSize(16)
        self.etykieta_wyniku.setFont(font)
        self.etykieta_wyniku.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Wyśrodkuj

        # Ustawiamy layout
        layout = QVBoxLayout()
        layout.addWidget(self.etykieta_instrukcji)
        layout.addWidget(self.pole_tekstowe)
        layout.addWidget(self.przycisk_przywitaj)
        layout.addWidget(self.etykieta_wyniku)

        self.setLayout(layout)

    def polaczSygnaly(self):
        """Metoda pomocnicza do łączenia akcji."""
        self.przycisk_przywitaj.clicked.connect(self.przywitaj_uzytkownika)

    # --- Nasz SLOT ---
    def przywitaj_uzytkownika(self):
        print("Slot został wywołany!")  # Dobre do debugowania

        # 1. Pobierz dane z innego widżetu (dlatego jest 'self'!)
        imie = self.pole_tekstowe.text()

        # Sprawdzenie, czy imię nie jest puste
        if not imie:
            imie = "Bezimienny"

        # 2. Ustaw dane w innym widżecie
        self.etykieta_wyniku.setText(f"Witaj, {imie}!")

        # 3. Możemy też modyfikować inne komponenty
        self.pole_tekstowe.clear()


# --- Blok uruchomieniowy ---
def main():
    app = QApplication(sys.argv)
    window = AplikacjaGreeter()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()