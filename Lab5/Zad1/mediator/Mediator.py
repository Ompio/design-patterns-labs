from Lab5.Zad1.mediator.Auction import Auction
from Lab5.Zad1.mediator.Client import Client


class Mediator:

    def __init__(self):
        auction = Auction(10)
        k1 = Client("Adam", 40)
        k2 = Client("Olek", 30)
        auction.attach(k1)
        auction.attach(k2)

    def notify(self, component: ) -> None:
        print("Subject: Notifying observers...")
        component.update()