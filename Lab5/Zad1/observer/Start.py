from Lab5.Zad1.observer.Auction import Auction
from Lab5.Zad1.observer.Client import Client


class Start:
    def __init__(self):
        auction = Auction(10)
        k1 = Client("Adam", 40)
        k2 = Client("Olek", 30)
        auction.attach(k1)
        auction.attach(k2)
        for i in range(0, 200, 10):
            auction.set_price(i)

if __name__ == "__main__":
    Start()