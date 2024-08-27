from __future__ import annotations
from abc import ABC, abstractmethod

class JednostkaPolicji(ABC):
    @abstractmethod
    def accept(self, V: Visitor) -> None:
        pass

class KomendaGlowna(JednostkaPolicji):
    def __init__(self):
        self.komendant = "Papała"
        self.obszar = (200, 100)

    def accept(self, V: Visitor) -> None:
        V.visit_komenda_glowna(self)


class Posterunek(JednostkaPolicji):
    def __init__(self):
        self.nazwiskoKomendanta = "Adamski"
        self.dlugosc = 10
        self.szerokosc = 20

    def accept(self, V: Visitor) -> None:
        V.visit_posterunek(self)

class ABW(JednostkaPolicji):
    def __init__(self):
        self.obszar = None  # Placeholder as in the original Java example

    def accept(self, V: Visitor) -> None:
        V.visit_abw(self)

class Dzielnicowy(JednostkaPolicji):
    def __init__(self):
        self.nazwiskoDzielnicowego = "Kowalski"
        self.powierzchnia = 100.0

    def accept(self, V: Visitor) -> None:
        V.visit_dzielnicowy(self)


class Test:
    def __init__(self):
        self.jednostki = []
        self.jednostki.append(Dzielnicowy())
        self.jednostki.append(Posterunek())
        self.jednostki.append(KomendaGlowna())
        self.jednostki.append(ABW())
        self.odwiedzajacySzefow = VisitorSzefow()
        self.odwiedzajacyPowierzchni = VisitorPowierzchni()

    def wypiszSzefow(self):
        print("Szefowie jednostek:")
        for jednostka in self.jednostki:
            jednostka.accept(self.odwiedzajacySzefow)

    def wypiszPowierzchnie(self):
        print("Powierzchnie jednostek:")
        for jednostka in self.jednostki:
            jednostka.accept(self.odwiedzajacyPowierzchni)

class Visitor(ABC):
    @abstractmethod
    def visit_dzielnicowy(self, jednostka: Dzielnicowy):
        pass

    @abstractmethod
    def visit_posterunek(self, jednostka: Posterunek):
        pass

    @abstractmethod
    def visit_komenda_glowna(self, jednostka: KomendaGlowna):
        pass

    @abstractmethod
    def visit_abw(self, jednostka: ABW):
        pass


class VisitorSzefow(Visitor):
    def visit_dzielnicowy(self, jednostka: Dzielnicowy):
        print(f"Dzielnicowy: {jednostka.nazwiskoDzielnicowego}")

    def visit_posterunek(self, jednostka: Posterunek):
        print(f"Posterunek: {jednostka.nazwiskoKomendanta}")

    def visit_komenda_glowna(self, jednostka: KomendaGlowna):
        print(f"KG: {jednostka.komendant}")

    def visit_abw(self, jednostka: ABW):
        print("ABW: Nazwisko jest tajne!")


class VisitorPowierzchni(Visitor):
    def visit_dzielnicowy(self, jednostka: Dzielnicowy):
        print(f"Dzielnica: {jednostka.powierzchnia}")

    def visit_posterunek(self, jednostka: Posterunek):
        print(f"Posterunek: {jednostka.dlugosc * jednostka.szerokosc}")

    def visit_komenda_glowna(self, jednostka: KomendaGlowna):
        print(f"KG: {jednostka.obszar}")

    def visit_abw(self, jednostka: ABW):
        print("ABW: Nazwisko jest tajne!")


# Example usage
if __name__ == "__main__":
    test = Test()
    test.wypiszSzefow()
    test.wypiszPowierzchnie()
