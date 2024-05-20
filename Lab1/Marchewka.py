from Lab1.Skladnik import Skladnik


class Marchewka(Skladnik):
    def __repr__(self):
        return 'marchewka'

    def przygotuj_skladnik(self):
        self.obierz()
        self.pokroj()

    @staticmethod
    def pokroj():
        print('Krojenie marchewki')

    def obierz(self):
        print('Obieranie marchewki')