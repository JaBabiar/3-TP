import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QPushButton, QDoubleSpinBox)


class BMICalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalkulator BMI")

        # Główny layout (pionowy)
        main_layout = QVBoxLayout()

        # --- Sekcja Wagi ---
        weight_layout = QHBoxLayout()
        weight_label = QLabel("Waga (kg):")
        self.weight_input = QDoubleSpinBox()
        self.weight_input.setRange(0, 300)

        weight_layout.addWidget(weight_label)
        weight_layout.addWidget(self.weight_input)

        # --- Sekcja Przycisku ---
        self.btn = QPushButton("Oblicz")
        self.btn.clicked.connect(self.calculate_bmi)

        # --- Sekcja Wyniku ---
        self.result_label = QLabel("Wynik pojawi się tutaj")

        # Dodawanie do głównego layoutu
        main_layout.addLayout(weight_layout)
        # TU DODAJ LAYOUT DLA WZROSTU
        main_layout.addWidget(self.btn)
        main_layout.addWidget(self.result_label)

        # Finalizacja
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def calculate_bmi(self):
        # 1. Pobierz wagę
        waga = self.weight_input.value()
        # 2. Pobierz wzrost (pamiętaj o konwersji cm -> m)
        # 3. Oblicz: waga / (wzrost * wzrost)
        # 4. Ustaw tekst w self.result_label
        pass


app = QApplication(sys.argv)
window = BMICalculator()
window.show()
app.exec()