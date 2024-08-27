from Lab5.Zad1.mediator.Auction import Auction
from Lab5.Zad1.mediator.Client import Client
from Lab5.Zad1.mediator.AuctionMediator import AuctionMediator


class Start:
    def __init__(self):
        mediator = AuctionMediator()
        auction = Auction(10, mediator)
        mediator.set_auction(auction)
        k1 = Client("Adam", 40)
        k2 = Client("Olek", 30)
        mediator.register_client(k1)
        mediator.register_client(k2)
        for i in range(0, 200, 10):
            auction.set_price(i)

if __name__ == "__main__":
    Start()