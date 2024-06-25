from Lab3.Przeglad import Przeglad
from Lab3.PrzegladDiesel import PrzegladDiesel
from Lab3.PrzegladZKlima import PrzegladZKlima


class PrzegladFacade:
    def __init__(self):
        self.podstawowy_przeglad = Przeglad
        self.przeglad_diesel = PrzegladDiesel
        self.PrzegladZKlima = PrzegladZKlima
