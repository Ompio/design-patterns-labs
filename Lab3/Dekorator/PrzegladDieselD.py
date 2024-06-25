from Lab3.Dekorator.PrzegladD import PrzegladDekoratorD


class PrzegladDiesel(PrzegladDekoratorD):
    def wykonaj_przeglad(self, s):
        print(f"Zaczynam przegląd diesla {s}")
        self.wymien_olej(s)
        self.wymien_filtry(s)
        print(f"Przegląd diesla {s} zakończony")

    def wymien_olej(self, s):
        print(f"Wymieniam olej w dieslu {s}")

    def wymien_filtry(self, s):
        print(f"Wymieniam filtry w dieslu {s}")