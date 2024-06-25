from Lab2.zadanie2.Faktura import Faktura
from Lab2.zadanie2.Pozycja import Pozycja

if __name__ == "__main__":
    faktura = Faktura()
    faktura.kontrahent = "Krzaczek Sp. z o.o."
    faktura.pozycje.append(Pozycja("komputer", 1, 1000))
    faktura.pozycje.append(Pozycja("drukarka", 2, 300, 23))
    faktura.pozycje.append(Pozycja("myszka", 2, 23, 23, ""))
    faktura.pozycje.append(Pozycja("montaz", 1, 300, 7, "234"))
    pozycja = Pozycja.Builder("drukarka", 2).cena(300).vat(23).build()