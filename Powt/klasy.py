# Stwórz klase pytanie która zawiera wartości
# - tresc / odpowiedzi / odpowiedz poprawna
# oraz metody
# odpowiedz
# Quiz który zawiera wartości
# Punkty / Lista Pytan / Imie I nazwisko /Wynik

class QuizClass:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.punkty = 0
        self.max = 0
        self.pytania = []
        self.curr_pytanie = 0

    def addQ(self, pytanie):
        self.pytania.append(pytanie)


class PytanieClass:
    def __init__(self, tresc, odpowiedzi, poprawna):
        self.tresc = tresc
        self.odpowiedzi = odpowiedzi
        self.poprawna = poprawna


def main():
    quiz = QuizClass("szpont")
    quiz.addQ(PytanieClass("Jaki mamy dzień", ["Piątek", "Czwartek", "Dobry"], 2))
    quiz.addQ(PytanieClass("Który mamy rok", ["2025", "2016", "2026"], 1))
    quiz.addQ(PytanieClass("Peak", ["Death Stranding", "Hideo Kojima", "Touge Battle w FH6", "Wszystkie"], 4))

    for pyt in quiz.pytania:
        print(pyt.tresc)
        print(pyt.odpowiedzi)
        print("Podaj Indeks Odpowiedzi: ")
        odp = int(input())
        if odp == pyt.poprawna:
            print("Wszystko Okej")


main()

### Rozwinięcie zadania, Dodaj klase Uczeń która posiada imie i nazwisko,
# Quiz w którym oraz Jego zapis tak aby
# końcowa wiadomość po odpowiedziach wyglądała w następujący sposób:
### [imie i nazwisko] otrzymał wynik [punkty zdobyte] [punkty maksymalne za quiz]