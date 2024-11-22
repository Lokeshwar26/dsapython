class chair:
    def __init__(self,min):
        self.__max=1000
        self.min=min


    def sell(self):
        print("max selling price of a chair:{}".format(self.__max))
        print("min selling price of a chair:",format(self.min))
    def setprice(self,price):
        self.__max=price
    
c=chair(400)
c.sell()

c.setprice(1500)
c.min=850
c.sell()

