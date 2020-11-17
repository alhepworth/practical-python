class Stock:
    __slots__= ('name','price','_shares','_cost')
    def __init__(self,name,shares,price):
        self.shares = shares
        self.price = price
        self.name = name

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self,value):
        if not isinstance(value,int):
            raise TypeError('Expected int')
        self._shares=value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, delta):
        self.shares =  self.shares - delta

    def __repr__(self):
        return "Stock('%s',%s,%s)" % (self.name, self.shares, self.price)