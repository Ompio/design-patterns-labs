from Lab1.Skladnik import Skladnik


class Makaron(Skladnik):
    def __repr__(self):
        return 'makaron'

    def przygotuj_skladnik(self):
        self.gotuj()

    @staticmethod
    def gotuj():
        print('Gotowanie makaronu')