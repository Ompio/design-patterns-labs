from typing import List

from Lab5.Zad1.Client import Client


class Auction:
    def __init__(self, price):
        self.price = price
        self._observers: List[Client] = []

    def set_price(self, price):
        self.price = price
        self.notify()

    def get_price(self):
        return self.price

    def attach(self, observer: Client) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Client) -> None:
        self._observers.remove(observer)
        print('detaching observer')

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update()
            if self.price > observer.max_price:
                self.detach(observer)
