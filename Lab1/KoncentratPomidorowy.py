from Lab1.Skladnik import Skladnik


class KoncentratPomidorowy(Skladnik):
    def __repr__(self):
        return 'Koncentrat pomidorowy'

    def przygotuj_skladnik(self):
        self.wrzuc()

    @staticmethod
    def wrzuc():
        print('Wrzucam koncentrat pomidorowy')
