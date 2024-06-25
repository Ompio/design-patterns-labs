from Lab3.templateMethod.PrzegladT import PrzegladT


class PrzegladZKlimaT(PrzegladT):
    def __sprawdz_klimatyzacje(self, s):
        print(f"Sprawdz klimatyzacje w {s}")

    def __dodatkowe_opcje_serwisowe(self, s):
        self.__sprawdz_klimatyzacje(s)
        