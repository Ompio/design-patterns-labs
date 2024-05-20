from Lab1.Skladnik import Skladnik


class Marchewka(Skladnik):
    def __repr__(self):
        return 'marchewka'

    @staticmethod
    def pokroj():
        print('Krojenie marchewki')

    def obierz(self):
        print('Obieranie marchewki')