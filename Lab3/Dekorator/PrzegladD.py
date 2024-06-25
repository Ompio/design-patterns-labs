class PrzegladD:
    def wykonaj_przeglad(self, s):
        raise NotImplementedError("Metoda musi być zaimplementowana")

class PrzegladPodstawowyD(PrzegladD):
    def wykonaj_przeglad(self, s):
        print(f"Zaczynam przegląd samochodu {s}")
        self.wymien_olej(s)
        self.wymien_filtry(s)
        self.wymien_swiece(s)
        print(f"Przegląd samochodu {s} zakończony")

    def wymien_olej(self, s):
        print(f"Wymieniam olej w {s}")

    def wymien_swiece(self, s):
        print(f"Wymieniam świece w {s}")

    def wymien_filtry(self, s):
        print(f"Wymieniam filtry w {s}")

class PrzegladDekoratorD(PrzegladD):
    def __init__(self, przeglad):
        self._przeglad = przeglad

    def wykonaj_przeglad(self, s):
        self._przeglad.wykonaj_przeglad(s)