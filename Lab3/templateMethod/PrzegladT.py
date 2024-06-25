from abc import ABC, abstractmethod

class PrzegladT:
    def __wymien_olej(self, s):
        print(f"Wymieniam olej w {s}")

    def __wymien_swiece(self, s):
        print(f"Wymieniam świece w {s}")

    def __wymien_filtry(self, s):
        print(f"Wymieniam filtry w {s}")

    @abstractmethod
    def __dodatkowe_opcje_serwisowe(self, s):
        pass

    def __serwisuj_silnik(self, s):
        self.__wymien_swiece(s)

    def wykonaj_przeglad(self, s):
        print(f"Zaczynam przegląd samochodu {s}")
        self.__wymien_olej(s)
        self.__wymien_filtry(s)
        self.__serwisuj_silnik(s)
        self.__dodatkowe_opcje_serwisowe(s)
        print(f"Przegląd samochodu {s} zakończony")