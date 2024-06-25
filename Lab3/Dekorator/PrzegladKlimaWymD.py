from Lab3.Dekorator.PrzegladKlimaD import PrzegladZKlima


class PrzegladKlimaWymD(PrzegladZKlima):
    def __init__(self, przeglad):
        super().__init__(przeglad)

    def wykonaj_przeglad(self, s):
        super().wykonaj_przeglad(s)
        self.__wymien_plyn_chlodniczy(s)

    def __wymien_plyn_chlodniczy(self, s):
        print(f"Wymien plyn chlodniczy w {s}")