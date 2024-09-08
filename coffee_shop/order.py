class Order:
    _orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, float) or price < 1.0 or price > 10.0:
            raise ValueError("Invalid price")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order._orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @classmethod
    def all_orders(cls):
        return cls._orders