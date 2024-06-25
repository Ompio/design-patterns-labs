from Lab3.Strategia.PrzegladS import PrzegladStrategy


class PrzegladSprawdzCisnienieS(PrzegladStrategy):
    def wykonaj_przeglad(self, s):
        self.sprawdz_cisnienie(s)

    def sprawdz_cisnienie(self, s):
        print(f"Sprawdzam cisnienie opon w {s}")