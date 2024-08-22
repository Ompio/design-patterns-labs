
class LewContext:
    def __init__(self):
        self.jedzacy = LewJedzacy(self)
        self.spacerujacy = LewSpacerujacy(self)
        self.spiacy = LewSpiacy(self)
        self.stan = self.spacerujacy

    def nakarm(self):
        print("Bierze się do jedzenia")
        self.stan = self.jedzacy

    def zaczep(self):
        self.stan.zaczep()

    def zaspiewaj(self):
        self.stan.zaspiewaj()

    def odbierz(self):
        self.stan.odbierz()

class LewInterface:
    def zaczep(self):
        raise NotImplementedError

    def nakarm(self):
        raise NotImplementedError

    def zaspiewaj(self):
        raise NotImplementedError

    def odbierz(self):
        print("Nie ma mu czego odebrać")

class LewSpiacy(LewInterface):
    def __init__(self, lewkontekst: LewContext):
        self.lewkon = lewkontekst

    def zaczep(self):
        print("Nie reaguje")

    def zaspiewaj(self):
        print("Budzi się")
        self.lewkon.stan = self.lewkon.spacerujacy


class LewJedzacy(LewInterface):
    def __init__(self, lewkontekst: LewContext):
        self.lewkon = lewkontekst
    def zaczep(self):
        print("Warczy")

    def zaspiewaj(self):
        print("Warczy")

    def jedzacy(self):
        print("Odebrano mu jedzenie")
        self.lewkon.stan = self.lewkon.spacerujacy


class LewSpacerujacy(LewInterface):
    def __init__(self, lewkontekst: LewContext):
        self.lewkon = lewkontekst
    def zaczep(self):
        print("Rzuca się na kratę")

    def zaspiewaj(self):
        print("Zasypia")
        self.lewkon.stan = self.lewkon.spiacy



