from Lab2.zadanie1.SamochodCiezarowy import SamochodCiezarowy
from Lab2.zadanie1.SamochodOsobowy import SamochodOsobowy


class FabrykaSamochodow:
    def przygotuj_samochod(self,typ):
        if typ == "osobowy":
            return SamochodOsobowy()
        elif typ == "ciężarowy":
            return SamochodCiezarowy()
        else:
            raise ValueError("Nieznany typ samochodu")