from Lab1.Skladnik import Skladnik


class Woda(Skladnik):
    def __repr__(self):
        return 'Woda'

    def przygotuj_skladnik(self):
        self.nalej()

    @staticmethod
    def nalej():
        print('Nalewam wode od garnka')
