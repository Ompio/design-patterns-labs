class Samochod:
    def zatankuj(self):
        raise NotImplementedError("Metoda zatankuj musi być zaimplementowana w klasie pochodnej")

    def sprawdz_plyny(self):
        raise NotImplementedError("Metoda sprawdz_plyny musi być zaimplementowana w klasie pochodnej")

    def test(self):
        raise NotImplementedError("Metoda test musi być zaimplementowana w klasie pochodnej")