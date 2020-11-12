class Stock:
    def __init__(self,name,shares,price):
        self.shares = shares
        self.price = price
        self.name=name

    def cost(self):
        return self.shares * self.price

    def sell(self, delta):
        self.shares =  self.shares - delta