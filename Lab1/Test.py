from Lab1.Kelner import Kelner
from Lab1.KoncentratPomidorowy import KoncentratPomidorowy
from Lab1.KostkaRosolowa import KostkaRosolowa
from Lab1.Kucharz import Kucharz
from Lab1.Makaron import Makaron
from Lab1.Marchewka import Marchewka
from Lab1.Ryz import Ryz
from Lab1.Woda import Woda
from Lab1.Zupa import Zupa
from ZupaPomidorowa import ZupaPomidorowa


class Test:
    def __init__(self):
        self.kucharz = Kucharz()
        self.kelner = Kelner()
        self.przygotujZupe()
        self.przygotujZupePomidorowaZRyzemNaWynos()
        self.przygotujZupePomidorowaZMakaronem()

    # def przygotuj(self, kucharz: IKucharz, kelner: IKelner):

    def przygotujZupe(self):
        zupka = Zupa('rosol')
        woda = Woda()
        zupka.skladniki.append(woda)
        kostka_rosolowa = KostkaRosolowa()
        zupka.skladniki.append(kostka_rosolowa)
        marchew = Marchewka()
        zupka.skladniki.append(marchew)
        makaron = Makaron()
        zupka.skladniki.append(makaron)
        self.kucharz.przygotuj(zupka)
        self.kelner.podaj(zupka)

    def przygotujZupePomidorowaZRyzemNaWynos(self):
        zupka = Zupa('pomidorowa z ryzem')
        woda = Woda()
        zupka.skladniki.append(woda)
        koncentrat_pomidorowy = KoncentratPomidorowy()
        zupka.skladniki.append(koncentrat_pomidorowy)
        marchew = Marchewka()
        zupka.skladniki.append(marchew)
        makaron = Ryz()
        zupka.skladniki.append(makaron)
        self.kucharz.przygotuj(zupka)
        self.kelner.wyslij('Ligota 1D')

    def przygotujZupePomidorowaZMakaronem(self):
        zupka = Zupa('pomidorowa z makaronem')
        woda = Woda()
        zupka.skladniki.append(woda)
        koncentrat_pomidorowy = KoncentratPomidorowy()
        zupka.skladniki.append(koncentrat_pomidorowy)
        marchew = Marchewka()
        zupka.skladniki.append(marchew)
        makaron = Makaron()
        zupka.skladniki.append(makaron)
        self.kucharz.przygotuj(zupka)
        self.kelner.podaj(zupka)


t = Test()