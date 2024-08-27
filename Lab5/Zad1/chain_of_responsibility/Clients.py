from Lab5.Zad1.chain_of_responsibility.Handler import AbstractHandler


class ClientHandler(AbstractHandler):
    def __init__(self, name, max_price):
        self.name = name
        self.max_price = max_price
        self.doing_auctions = True

    def handle(self, price) -> str:
        if self.doing_auctions is False:
            print(f"{self.name} no longer auctioning")
            return super().handle(price)
        if price > self.max_price:
            self.doing_auctions = False
            print(f"{self.name} quits auction")
            return super().handle(price)
        else:
            print(f"{self.name} continues auctioning")
            return super().handle(price)
