from Lab1.IKucharz import IKucharz
from Lab1.Zupa import Zupa


class Kucharz(IKucharz):
    @staticmethod
    def przygotuj(zupa: Zupa):
        print(f'Przygotowanie {zupa.nazwa} ze skladnikow: {zupa.skladniki}')
        for skladnik in zupa.skladniki:
            skladnik.przygotuj_skladnik()
