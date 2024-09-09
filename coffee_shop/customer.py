class Customer:
    def __init__(self, name):

        """checks if the customer's name is between 1 and 15 characters long."""
        if not isinstance(name, str) or len(name) < 1 or len(name) > 15:
            
            """if the condition is not meet a ValueError message will be returned."""
            raise ValueError("Invalid customer name")
        
        """since the codition is satisfied the name is assigned an instance variable _name."""
        self._name = name

    """Allow the method to be accessed like an attribute by using a decorator."""
    @property
    def name(self):
        """Encapsulation."""
        return self._name

    """create a new order for the customer."""
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    """retrive all orders that customers have made."""
    def orders(self):
        from order import Order
        return [order for order in Order.all_orders() if order.customer == self]

    def coffees(self):
        #if the customer has ordered a unique set of coffees the coffee namee is extracted from the order.
        return set(order.coffee for order in self.orders())

    @classmethod
    def most_aficionado(cls, coffee):
        """Returns the customer with the most expensive order."""
        from order import Order
        orders = [order for order in Order.all_orders() if order.coffee == coffee]
        if not orders:
            return None
        return max(orders, key=lambda order: order.price).customer