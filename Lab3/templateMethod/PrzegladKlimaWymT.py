from Lab3.templateMethod.PrzegladKlimaT import PrzegladZKlimaT


class PrzegladKlimaWymT(PrzegladZKlimaT):
    def __dodatkowe_opcje_serwisowe(self, s):
        super().__dodatkowe_opcje_serwisowe(s)

    def __wymien_plyn_chlodniczy(s):
        print(f"Wymien plyn chlodniczy w {s}")