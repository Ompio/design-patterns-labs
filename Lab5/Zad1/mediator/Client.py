class Client:
    def __init__(self, name, max_price):
        self.name = name
        self.max_price = max_price

    def update(self):
        print('i see that price changed')
