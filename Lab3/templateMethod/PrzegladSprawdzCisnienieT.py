from Lab3.templateMethod.PrzegladT import PrzegladT


class PrzegladSprawdzCisnienieT(PrzegladT):
    def sprawdz_cisnienie(self, s):
        print(f"Sprawdz klimatyzacje w {s}")

    def __dodatkowe_opcje_serwisowe(self, s):
        self.sprawdz_cisnienie(s)
