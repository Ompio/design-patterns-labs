from Lab2.zadanie3 import LiczydloSingleton
from Lab2.zadanie3.Liczydlo import Liczydlo
from Lab2.zadanie3.LiczydloPool import LiczydloPool


class Test:
    @staticmethod
    def main():
        o1 = Liczydlo()
        o1.obliczenia1()
        o1.obliczenia2()

        o2 = LiczydloSingleton
        o2.obliczenia1()
        o2.obliczenia2()
        pool = LiczydloPool(3)
        for i in range(1, 6):
            print("Attempt:", i)
            o3 = pool.get_object()
            if o3 is not None:
                o3.obliczenia1()
                o3.obliczenia2()
            else:
                print("No free objects!")



Test.main()