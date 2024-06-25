from Lab2.zadanie1.FabrykaSamochodow import FabrykaSamochodow


class Serwis:
    def __init__(self):
        self.fabryka = FabrykaSamochodow()
    def przygotuj_samochod(self, typ):
        car = self.fabryka.przygotuj_samochod(typ)
        car.sprawdz_plyny()
        car.zatankuj()
        return car