from Lab1.Makaron import Makaron
from Lab1.Marchewka import Marchewka
from Lab1.Ryz import Ryz
from Lab1.Zupa import Zupa
from ZupaPomidorowa import ZupaPomidorowa


class Test:
    def __init__(self):
        self.przygotujZupe()

    def przygotujZupe(self):
        zupka = Zupa()
        marchew = Marchewka()
        zupka.skladniki.append(marchew)
        makaron = Makaron()
        zupka.skladniki.append(makaron)
        zupka.przygotuj()
        zupka.podaj()

    def przygotujZupePomidorowaZRyzemNaWynos(self):
        zupka = ZupaPomidorowa()
        marchew = Marchewka()
        zupka.skladniki.append(marchew)
        makaron = Ryz()
        zupka.skladniki.append(makaron)
        zupka.przygotuj()
        zupka.wyslij('Ligota 1D')
    def przygotujZupePomidorowaZMakaronem(self):
        zupka = ZupaPomidorowa()
        marchew = Marchewka()
        zupka.skladniki.append(marchew)
        makaron = Makaron()
        zupka.skladniki.append(makaron)
        zupka.przygotuj()
        zupka.podaj()


t = Test()