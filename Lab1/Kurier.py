from Lab1.IKelner import IKelner
from Lab1.Zupa import Zupa


class Kurier(IKelner):
    def __init__(self):
        self.adres: str

    def podaj(self, zupka: Zupa):
        print(f'Dostarczam {zupka} na adres: {self.adres}')

    def set_adres(self, adres):
        self.adres = adres
