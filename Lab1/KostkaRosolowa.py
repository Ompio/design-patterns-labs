from Lab1.Skladnik import Skladnik


class KostkaRosolowa(Skladnik):
    def __repr__(self):
        return 'Kostka rosolowa'

    def przygotuj_skladnik(self):
        self.wrzuc()

    @staticmethod
    def wrzuc():
        print('Wrzucam kostke rosolowa')
