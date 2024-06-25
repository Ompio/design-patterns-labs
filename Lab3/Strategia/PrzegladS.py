class PrzegladStrategy:
    def wykonaj_przeglad(self, s):
        raise NotImplementedError("Metoda musi być zaimplementowana")


class PrzegladPodstawowy(PrzegladStrategy):
    def wykonaj_przeglad(self, s):
        self.wymien_swiece(s)

    def wymien_swiece(self, s):
        print(f"Wymieniam świece w {s}")


class PrzegladContext:
    def __init__(self, strategy: PrzegladStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PrzegladStrategy):
        self._strategy = strategy

    def wykonaj_przeglad(self, s):
        print(f"Zaczynam przegląd samochodu {s}")
        self.wymien_olej(s)
        self.wymien_filtry(s)
        self._strategy.wykonaj_przeglad(s)
        print(f"Przegląd samochodu {s} zakończony")

    def wymien_filtry(self, s):
        print(f"Wymieniam filtry w {s}")

    def wymien_olej(self, s):
        print(f"Wymieniam olej w {s}")
