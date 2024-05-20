from Lab1.Skladnik import Skladnik


class Ryz(Skladnik):
    def __repr__(self):
        return 'Ryz'

    def przygotuj_skladnik(self):
        self.gotuj()

    @staticmethod
    def gotuj():
        print('Gotowanie ryzu')
