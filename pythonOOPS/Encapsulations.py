class Computer:
    def __init__(self):
        self.__maxPrice = 800
        self.__minPrice = 100

    def sell(self):
        print("Selling Max price {}".format(self.__maxPrice))
        print("Selling Min price {}".format(self.__minPrice))

    def selMax(self, price):
        self.__maxPrice = price

    def selMin(self, price):
        self.__minPrice = price


c = Computer()
c.sell()

c.selMin(500)
c.selMax(600)
c.sell()