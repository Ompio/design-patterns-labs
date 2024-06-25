from Lab3.Strategia.PrzegladS import PrzegladStrategy


class PrzegladZKlima(PrzegladStrategy):
    def wykonaj_przeglad(self, s):
        self.wymien_swiece(s)
        self.sprawdz_klimatyzacje(s)

    def wymien_swiece(self, s):
        print(f"Wymieniam świece w {s}")

    def sprawdz_klimatyzacje(self, s):
        print(f"Sprawdzam klimatyzację w {s}")