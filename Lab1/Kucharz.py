from Lab1.Zupa import Zupa


class Kucharz:
    @staticmethod
    def przygotuj(zupa: Zupa):
        print(f'Przygotowanie {zupa.nazwa} ze skladnikow: {zupa.skladniki}')
        for skladnik in zupa.skladniki:
            skladnik.przygotuj_skladnik()
