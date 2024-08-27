class Product:
    def __init__(self, name, price, stock=0):
        self._name = name
        self._price = price
        self._stock = max(0, stock)  # Ensure stock is not negative

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, amount):
        self._stock = max(0, amount)

    def __eq__(self, other):
        return self._name == other.name

    def __add__(self, amount):
        self.stock += amount

    def __sub__(self, amount):
        self.stock -= amount
