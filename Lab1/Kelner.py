from Lab1.Zupa import Zupa


class Kelner:
    def wyslij(self, adres: str):
        print(f'Dostarczam obiad pod adres: {adres}')

    def podaj(self, zupka: Zupa):
        print('Podanie obiadu')
        print(f'Podaj {zupka.nazwa} do stolu')