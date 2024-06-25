class Pozycja:
    def __init__(self, opis, ilosc, cena=100, vat=22, ku=""):
        self.opis = opis
        self.ilosc = ilosc
        self.cena = cena
        self.vat = vat
        self.ku = ku

    class Builder:
        def __init__(self, opis, ilosc):
            self._opis = opis
            self._ilosc = ilosc
            self._cena = 100
            self._vat = 22
            self._ku = ""

        def cena(self, value):
            self._cena = value
            return self

        def vat(self, value):
            self._vat = value
            return self

        def ku(self, value):
            self._ku = value
            return self

        def build(self):
            return Pozycja(self._opis, self._ilosc, self._cena, self._vat, self._ku)
