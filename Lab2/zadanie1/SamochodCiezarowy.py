from Lab2.zadanie1.Samochod import Samochod


class SamochodCiezarowy(Samochod):
    def zatankuj(self):
        print(f"{self} Tankowanie ciężarówki")

    def sprawdz_plyny(self):
        print(f"{self} Sprawdzanie płynów ciężarówki")

    def test(self):
        print(f"Ciężarówka {self} gotowa")