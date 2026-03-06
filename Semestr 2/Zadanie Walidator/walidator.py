def sprawdz_alt(tekst):
    if len(tekst) > 255:
        return "Błąd: Za długi"
    if len(tekst) < 125:
        return "Błąd: za krótki"

    if tekst.startswith("zdjęcie"):
        return "Błąd: Zbędny Przedrostek"

    return "Poprawny ALT"