from Lab1.Makaron import Makaron
from Lab1.Marchewka import Marchewka


class Zupa:
    def __init__(self):
        self.skladniki = []
        self.nazwa: str

    def przygotuj(self):
        print(f'Przygotowanie zupy ze skladnikow: {self.skladniki}')
        print('Nalewam wode od garnka')
        print('Wrzucam kostke rosolowa')
        self.nazwa = 'rosol'
        for skladnik in self.skladniki:
            if isinstance(skladnik, Marchewka):
                skladnik.obierz()
                skladnik.pokroj()
            if isinstance(skladnik, Makaron):
                skladnik.gotuj()

    def podaj(self):
        print('Podanie obiadu')
        print(f'Podaj {self.nazwa} do stolu')

    def wyslij(self, adres: str):
        print(f'Dostarczam obiad pod adres: {adres}')
