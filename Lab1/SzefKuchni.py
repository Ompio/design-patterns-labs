from Lab1.IKucharz import IKucharz
from Lab1.Zupa import Zupa


class SzefKuchni(IKucharz):
    @staticmethod
    def przygotuj(zupa: Zupa):
        print(f'Przygotowanie {zupa.nazwa} ze skladnikow: {zupa.skladniki}')
        for skladnik in zupa.skladniki:
            skladnik.przygotuj_skladnik()

    def przygotujMenu(self):
        print('Przygowowanie menu na nestepny okres pracy')