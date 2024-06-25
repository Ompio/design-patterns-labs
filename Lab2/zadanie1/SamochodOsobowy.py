from Lab2.zadanie1.Samochod import Samochod


class SamochodOsobowy(Samochod):
    def zatankuj(self):
        print(f"{self} Tankowanie samochodu osobowego")

    def sprawdz_plyny(self):
        print(f"{self} Sprawdzanie płynów samochodu osobowego")

    def test(self):
        print(f"Samochód osobowy {self} gotowy")