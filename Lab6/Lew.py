class Lew:
    SPIACY = 0
    JEDZACY = 1
    SPACERUJACY = 2

    def __init__(self):
        self.stan = self.SPACERUJACY

    def get_stan(self):
        return self.stan

    def set_stan(self, stan):
        self.stan = stan

    def zaczep(self):
        if self.stan == self.SPIACY:
            print("Nie reaguje")
        elif self.stan == self.JEDZACY:
            print("Warczy")
        elif self.stan == self.SPACERUJACY:
            print("Rzuca się na kratę")

    def nakarm(self):
        print("Bierze się do jedzenia")
        self.stan = self.JEDZACY

    def zaspiewaj(self):
        if self.stan == self.SPACERUJACY:
            print("Zasypia")
            self.stan = self.SPIACY
        elif self.stan == self.JEDZACY:
            print("Warczy")
        elif self.stan == self.SPIACY:
            print("Budzi się")
            self.stan = self.SPACERUJACY

    def odbierz(self):
        if self.stan == self.JEDZACY:
            print("Odebrano mu jedzenie")
            self.stan = self.SPACERUJACY
        else:
            print("Nie ma mu czego odebrać")


# Interface in Python is usually represented by abstract base classes or simply by defining the required methods.
class ILew:
    def zaczep(self):
        raise NotImplementedError

    def nakarm(self):
        raise NotImplementedError

    def zaspiewaj(self):
        raise NotImplementedError

    def odbierz(self):
        raise NotImplementedError


# Creating an instance of Lew and running the same sequence of operations as in Java
lew = Lew()
print("==Zaczepiam lwa")
lew.zaczep()
print("==Karmię lwa")
lew.nakarm()
print("==Zaczepiam lwa")
lew.zaczep()
print("==Śpiewam lwu")
lew.zaspiewaj()
print("==Odbieram lwu jedzenie")
lew.odbierz()
print("==Śpiewam lwu")
lew.zaspiewaj()
print("==Odbieram lwu jedzenie")
lew.odbierz()