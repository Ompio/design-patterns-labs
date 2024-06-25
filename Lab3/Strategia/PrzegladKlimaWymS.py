from Lab3.Strategia.PrzegladKlimaS import PrzegladZKlima


class PrzegladKlimaWymS(PrzegladZKlima):
    def wykonaj_przeglad(self, s):
        self.sprawdz_klimatyzacje(s)
        self.__wymien_plyn_chlodniczy(s)

    def __wymien_plyn_chlodniczy(self, s):
        print(f"Wymien plyn chlodniczy w {s}")