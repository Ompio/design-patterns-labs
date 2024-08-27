from typing import List

from Lab5.Zad1.mediator.Auction import Auction
from Lab5.Zad1.mediator.Client import Client
from Lab5.Zad1.mediator.Mediator import Mediator


class AuctionMediator(Mediator):
    def __init__(self):
        self._clients: List[Client] = []
        self._auction: Auction = None

    def set_auction(self, auction: 'Auction'):
        self._auction = auction

    def register_client(self, client: 'Client'):
        print(f"Mediator: Registering client {client.name}.")
        client.mediator = self
        self._clients.append(client)

    def notify(self, event: str):
        if event == "price change":
            print("Mediator: Notifying` clients...")
            for client in self._clients:
                if client.update(self._auction.get_price()) is "detach me":
                    self._clients.remove(client)
                    print(f"Mediator: `Removing client {client.name} due to price limit.")