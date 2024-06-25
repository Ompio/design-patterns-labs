from Lab3.Przeglad import Przeglad


class PrzegladZKlima(Przeglad):
    def __sprawdz_klimatyzacje(self, s):
        print(f"Sprawdz klimatyzacje w {s}")
    def wykonaj_przeglad(self, s):
        print(f"Zaczynam przegląd samochodu {s}")
        self.__wymien_olej(s)
        self.__wymien_filtry(s)
        self.__wymien_swiece(s)
        self.__sprawdz_klimatyzacje(s)
        print(f"Przegląd samochodu {s} zakończony")
