from Lab2.zadanie1.Serwis import Serwis


class Klient:
    def __init__(self):
        serwis = Serwis()
        moj_samochod = serwis.przygotuj_samochod("osobowy")
        moj_samochod.test()
        moj_samochod2 = serwis.przygotuj_samochod("ciężarowy")
        moj_samochod2.test()


Klient()
