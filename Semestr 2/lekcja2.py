import sys
# Importujemy niezbędne klasy z modułu QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class MojePierwszeOkno(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 1. KONFIGURACJA GŁÓWNEGO OKNA
        self.setWindowTitle("Podstawy PyQt6 - Sygnały i Sloty")
        self.setFixedSize(350, 200) # Ustawiamy stały rozmiar okna (szerokość, wysokość)

        # 2. TWORZENIE ELEMENTÓW INTERFEJSU (WIDGETÓW)
        # Tworzymy etykietę tekstową
        self.etykieta = QLabel("Witaj! Kliknij przycisk poniżej.", self)
        
        # Tworzymy przycisk
        self.przycisk = QPushButton("Kliknij mnie", self)

        # 3. ŁĄCZENIE SYGNAŁÓW ZE SLOTAMI (AKCJAMI)
        # Kiedy przycisk zostanie kliknięty (sygnał), wywołaj metodę zmien_tekst (slot)
        self.przycisk.clicked.connect(self.zmien_tekst)

        # 4. UKŁADANIE ELEMENTÓW W OKNIE (LAYOUT)
        # Aby elementy ładnie się ułożyły, używamy pionowego układu (QVBoxLayout)
        uklad = QVBoxLayout()
        uklad.addWidget(self.etykieta)
        uklad.addWidget(self.przycisk)

        # Tworzymy główny, centralny widget i przypisujemy mu nasz układ
        centralny_widget = QWidget()
        centralny_widget.setLayout(uklad)
        self.setCentralWidget(centralny_widget)

    # 5. DEFINIOWANIE METOD (SLOTÓW)
    def zmien_tekst(self):
        """Ta metoda uruchamia się po kliknięciu przycisku."""
        self.etykieta.setText("Świetnie! Sygnał został odebrany.")
        self.przycisk.setText("Już kliknięto")
        self.przycisk.setEnabled(False) # Wyłącza przycisk po pierwszym kliknięciu


# === URUCHOMIENIE APLIKACJI ===
if __name__ == "__main__":
    # QApplication zarządza główną pętlą programu
    app = QApplication(sys.argv)
    
    # Tworzymy instancję naszego okna i wyświetlamy je
    okno = MojePierwszeOkno()
    okno.show()
    
    # Uruchamiamy pętlę zdarzeń (aplikacja działa dopóki jej nie zamkniemy)
    sys.exit(app.exec())


"""
Twoim zadaniem jest napisanie własnej, prostej aplikacji w PyQt6 
na podstawie powyższego przykładu.

Wymagania:
1. Utwórz okno o nazwie "Mój Panel Sterowania" i wymiarach 400x300.
2. Dodaj do okna jedną etykietę (QLabel) z tekstem "Wybierz akcję:".
3. Dodaj DWA przyciski (QPushButton) obok siebie lub jeden pod drugim:
   - Przycisk 1: Tekst "Powitanie"
   - Przycisk 2: Tekst "Pożegnanie"
4. Oprogramuj zachowanie przycisków:
   - Kliknięcie przycisku "Powitanie" powinno zmienić tekst 
     etykiety na "Witaj na lekcji programowania!".
   - Kliknięcie przycisku "Pożegnanie" powinno zmienić tekst 
     etykiety na "Do zobaczenia następnym razem!".

Zadanie do oddania na + z aktywności 
"""
