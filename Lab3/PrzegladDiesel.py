from Lab3.Przeglad import Przeglad


class PrzegladDiesel(Przeglad):
    def wykonaj_przeglad(self, s):
        print(f"Zaczynam przegląd samochodu {s}")
        self.__wymien_olej(s)
        self.__wymien_filtry(s)
        print(f"Przegląd samochodu {s} zakończony")
