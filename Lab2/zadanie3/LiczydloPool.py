from Lab2.zadanie3.Liczydlo import Liczydlo


class LiczydloPool:
    def __init__(self, size):
        self.size = size
        self.pool = [Liczydlo() for _ in range(size)]
        self.available = set(range(size))

    def get_object(self):
        if self.available:
            index = self.available.pop()
            return self.pool[index]
        else:
            raise Exception("Brak wolnych obiektów w puli")

    def release_object(self, obj):
        index = self.pool.index(obj)
        self.available.add(index)