# create a program where maximum price of the product cannot be modified more than 100;
class Product:
    def __init__(self):
        self.__maxprice = 75

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price


p = Product()
p.sell()
# change the price

p.__maxprice = 100
p.sell()
