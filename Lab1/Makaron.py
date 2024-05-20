from Lab1.Skladnik import Skladnik


class Makaron(Skladnik):
    def __repr__(self):
        return 'makaron'

    @staticmethod
    def gotuj():
        print('Gotowanie makaronu')