from Lab1.Makaron import Makaron
from Lab1.Marchewka import Marchewka
from Lab1.Ryz import Ryz
from Lab1.Zupa import Zupa


class ZupaPomidorowa(Zupa):
    def przygotuj(self):
        print(f'Przygotowanie zupy ze skladnikow: {self.skladniki}')
        print('Nalewam wode od garnka')
        print('Wrzucam koncentrat pomidorowy')
        self.nazwa = 'zupa pomidorowa'
        for skladnik in self.skladniki:
            if isinstance(skladnik, Marchewka):
                skladnik.obierz()
                skladnik.pokroj()
            if isinstance(skladnik, Makaron):
                skladnik.gotuj()
            if isinstance(skladnik, Ryz):
                skladnik.gotuj()

    def podaj(self):
        print('Podanie obiadu')
        print(f'Podaj {self.nazwa} do stolu')

    def wyslij(self, adres: str):
        print(f'Dostarczam obiad pod adres: {adres}')