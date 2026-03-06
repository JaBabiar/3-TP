import unittest
from walidator import sprawdz_alt

class TestWalidatora(unittest.TestCase):
    def test_poprawny_opis(self):
        self.assertEqual(sprawdz_alt("Czerwony samochód zaparkowany na trawie"), "Poprawny ALT")

    def test_za_krotki(self):
        # Minimum 5 znaków
        self.assertEqual(sprawdz_alt("Kot"), "Błąd: Za długi")

    def test_za_dlugi(self):
        # Maks 128 znakow
        dlugi_tekst = "AB" * 60
        self.assertEqual(sprawdz_alt(dlugi_tekst), "Błąd: za krótki")

    def test_zbedny_przedrostek(self):
        #Czytniki automatycznie mówią nam że to opis zdjęcia
        self.assertEqual(sprawdz_alt("zdjęcie Psa"), "Błąd: Zbędny Przedrostek")
        self.assertEqual(sprawdz_alt("Zdjęcie Kota"), "Błąd: Zbędny Przedrostek")

    def test_zly_typ_danych(self):
        with self.assertRaises(TypeError):
            sprawdz_alt(123)

