from typing import List

# Abstract base class for police units
class JednostkaPolicji:
    pass

# Derived classes with their specific attributes
class KomendaGlowna(JednostkaPolicji):
    def __init__(self):
        self.komendant = "Papała"
        self.obszar = (200, 100)  # Using tuple to represent dimension

class Posterunek(JednostkaPolicji):
    def __init__(self):
        self.nazwiskoKomendanta = "Adamski"
        self.dlugosc = 10
        self.szerokosc = 20

class ABW(JednostkaPolicji):
    def __init__(self):
        self.obszar = None  # Placeholder as in the original Java example

class Dzielnicowy(JednostkaPolicji):
    def __init__(self):
        self.nazwiskoDzielnicowego = "Kowalski"
        self.powierzchnia = 100.0

# Main class to manage police units and operations
class Test:
    def __init__(self):
        self.jednostki = []
        self.jednostki.append(Dzielnicowy())
        self.jednostki.append(Posterunek())
        self.jednostki.append(KomendaGlowna())
        self.jednostki.append(ABW())

    def wypiszSzefow(self):
        print("Szefowie jednostek:")
        for jednostka in self.jednostki:
            if isinstance(jednostka, Dzielnicowy):
                print(f"Dzielnicowy: {jednostka.nazwiskoDzielnicowego}")
            elif isinstance(jednostka, Posterunek):
                print(f"Posterunek: {jednostka.nazwiskoKomendanta}")
            elif isinstance(jednostka, KomendaGlowna):
                print(f"KG: {jednostka.komendant}")
            elif isinstance(jednostka, ABW):
                print("ABW: Nazwisko jest tajne!")

    def wypiszPowierzchnie(self):
        for jednostka in self.jednostki:
            if isinstance(jednostka, Dzielnicowy):
                print(f"Dzielnica: {jednostka.powierzchnia}")
            elif isinstance(jednostka, Posterunek):
                print(f"Posterunek: {jednostka.szerokosc * jednostka.dlugosc}")
            elif isinstance(jednostka, KomendaGlowna):
                print(f"KG: {jednostka.obszar}")
            elif isinstance(jednostka, ABW):
                print("ABW: Cała Polska")

# Visitor interface using Python's approach
class Visitor:

    def visit(self, jednostka: Dzielnicowy):
        print(f"Dzielnicowy: {jednostka.nazwiskoDzielnicowego}")

    def visit(self, jednostka: Posterunek):
        print(f"Posterunek: {jednostka.nazwiskoKomendanta}")

    def visit(self, jednostka: KomendaGlowna):
        print(f"KG: {jednostka.komendant}")

    def visit(self, jednostka: ABW):
        print("ABW: Nazwisko jest tajne!")


# Example usage
if __name__ == "__main__":
    test = Test()
    test.wypiszSzefow()
    test.wypiszPowierzchnie()
