from Lab1.Skladnik import Skladnik


class Ryz(Skladnik):
    def __repr__(self):
        return 'Ryz'

    @staticmethod
    def gotuj():
        print('Gotowanie ryzu')
