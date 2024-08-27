from Lab5.Zad1.chain_of_responsibility.Clients import ClientHandler


class Start:
    def __init__(self):
        k1 = ClientHandler("Adam", 40)
        k2 = ClientHandler("Olek", 30)
        k1.set_next(k2)
        for i in range(0, 200, 10):
            k1.handle(i)

if __name__ == "__main__":
    Start()