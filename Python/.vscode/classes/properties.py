class Product:
    def __init__(self, price):
        self.price = price

# decorator za property, umesto da eksplicitno pozivamo property funkciju da se kreira property objekat (       price = property(price, sprice) )
# mozemo da primenimo property decorator
#  na tu metodu, preimenujemo je iz get_price u samo price pozivanjem ovako napravljene funkcije kreira se property objekat, isto uradimo i sa setterom
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


product = Product(-10)
# product._price = -1
print(product._price)
