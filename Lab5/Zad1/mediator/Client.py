from Lab5.Zad1.mediator.Mediator import Mediator


class Client:
    def __init__(self, name, max_price):
        self.name = name
        self.max_price = max_price
        self._mediator = None

    def update(self, price):
        print(f"{self.name}: I see that price changed to {price}")
        if price > self.max_price:
            return "detach me"

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator