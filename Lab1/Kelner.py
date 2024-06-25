from Lab1.IKelner import IKelner
from Lab1.Zupa import Zupa


class Kelner(IKelner):
    def wyslij(self, adres: str):
        print(f'Dostarczam obiad pod adres: {adres}')

    def podaj(self, zupka: Zupa):
        print('Podanie obiadu')
        print(f'Podaj {zupka.nazwa} do stolu')

    def nakryjStol(self):
        print('Nakrycie stolu')

    def zbierzNaczynia(self):
        print('Zebranie naczyn')