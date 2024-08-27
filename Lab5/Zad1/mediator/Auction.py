from Lab5.Zad1.mediator.Mediator import Mediator

class Auction:
    def __init__(self, price, mediator: Mediator):
        self._price = price
        self.mediator = mediator

    def set_price(self, price):
        self._price = price
        self.mediator.notify("price change")

    def get_price(self):
        return self._price

