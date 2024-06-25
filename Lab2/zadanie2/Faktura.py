class Faktura:
    def __init__(self):
        self._kontrahent = None
        self._pozycje = []

    @property
    def kontrahent(self):
        return self._kontrahent

    @kontrahent.setter
    def kontrahent(self, value):
        self._kontrahent = value

    @property
    def pozycje(self):
        return self._pozycje