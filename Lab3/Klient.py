from Lab3.Przeglad import Przeglad
from Lab3.Samochod import Samochod


class Client:
    def main(self):
        s = Samochod("Fiat Punto")
        przeglad = Przeglad()
        przeglad.wykonaj_przeglad(s)

        s = Samochod("Ford Mondeo")
        przeglad.wykonaj_przeglad(s)


if __name__ == "__main__":
    client = Client()
    client.main()
