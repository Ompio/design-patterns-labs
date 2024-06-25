from Lab3.Dekorator.PrzegladD import PrzegladDekoratorD


class PrzegladZKlima(PrzegladDekoratorD):
    def __init__(self, przeglad):
        super().__init__(przeglad)

    def wykonaj_przeglad(self, s):
        super().wykonaj_przeglad(s)
        self.sprawdz_klimatyzacje(s)

    def sprawdz_klimatyzacje(self, s):
        print(f"Sprawdzam klimatyzację w {s}")