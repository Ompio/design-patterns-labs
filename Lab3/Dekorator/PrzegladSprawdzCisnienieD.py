from Lab3.Dekorator.PrzegladD import PrzegladDekoratorD


class PrzegladSprawdzCisnienieD(PrzegladDekoratorD):
    def __init__(self, przeglad):
        super().__init__(przeglad)

    def wykonaj_przeglad(self, s):
        super().wykonaj_przeglad(s)
        self.sprawdz_cisnienie(s)

    def sprawdz_cisnienie(self, s):
        print(f"Sprawdzam cisnienie opon w {s}")