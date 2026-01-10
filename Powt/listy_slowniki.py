# CZĘŚĆ 1: LISTY
# 1. Utwórz listę zawierającą pięć dowolnych imion.
nazwaListy = ["imie1", "imie2", "imie3", "imie4", "imie5", "Marian"]
# 2. Wyświetl trzeci element tej listy (pamiętaj o indeksowaniu od zera!).
print(nazwaListy[2])
# 3. Dodaj na koniec listy swoje imię.
nazwaListy.append("Michał")
# 4. Usuń drugi element z listy.
nazwaListy.pop(1)# alt. del nazwaListy[1]
# 5. Odwróć kolejność elementów w liście i wyświetl wynik.
nazwaListy.reverse()
# 6. Utwórz nową listę zawierającą tylko imiona zaczynające się na literę "A" (lub inną wybraną).
naLitere = [imie for imie in nazwaListy if imie.startswith("i")]
print(naLitere)
naLitere = []
for imie in nazwaListy:
    if imie.startswith("M"):
        naLitere.append(imie)
print(naLitere)

# 7. Połącz dwie listy: jedną z imionami, a drugą z nazwiskami – tak aby powstała lista par (np. ["Jan", "Kowalski"]).
imiona = ["Anna", "Piotr", "Kasia", "Marek", "Julia"]
nazwiska = ["Kowalski", "Nowak", "Wiśniewski", "Wójcik", "Kamińska"]
imieNazwisko = []
for para in zip(imiona, nazwiska):
    imieNazwisko.append(list(para))
print(imieNazwisko)


# CZĘŚĆ 2: SŁOWNIKI
# 1. Utwórz słownik reprezentujący ucznia: klucze to "imię", "nazwisko", "klasa", a wartości – przykładowe dane.
nazwaSlownika = {
    "imie": "jakiesImie",
    "nazwisko": "jakiesNazwisko",
    "klasa": "3tp"
}
# 2. Dodaj do słownika nowy klucz "oceny" z wartością będącą listą liczb (np. [5, 4, 6, 3]).
nazwaSlownika["oceny"] = [5, 4, 6, 3]
print(nazwaSlownika)

nazwaSlownika.update({"oceny": [1,2,3,4], "srednia": 4.3})
print(nazwaSlownika)
# 3. Wyświetl tylko listę ocen ucznia.
print(nazwaSlownika["oceny"])
# 4. Oblicz i wyświetl średnią ocen ucznia.
print(sum(nazwaSlownika["oceny"])/len(nazwaSlownika["oceny"]))
# 5. Utwórz słownik klas, w którym każda klasa (np. "3A", "3B") ma swój własny słownik z danymi uczniów:
#    np. {"3A": {"uczniowie": [{"imię": "Ziutek", "oceny": [5, 6]}, ...], "wychowawca": "Pan Nowak"}}
# 6. Dodaj nowego ucznia do jednej z klas.
# 7. Znajdź ucznia z najwyższą średnią ocen w danej klasie i wyświetl jego imię.


