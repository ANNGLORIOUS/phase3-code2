import pytest
from coffee import Coffee  # assuming the coffee module is in the same directory
from order import Order  # assuming the order module is in the same directory
from customer import Customer  # assuming the customer module is in the same directory

def test_order_price_validation():
    customer = Customer("JohnDoe")
    with pytest.raises(ValueError):
        Order(customer, "Cappuccino", 0.9)
    with pytest.raises(ValueError):
        Order(customer, "Cappuccino", 10.1)
    Order(customer, "Cappuccino", 5.0)

def test_order_properties():
    customer = Customer("JohnDoe")
    order = Order(customer, "Cappuccino", 3.5)
    assert order.customer == customer
    assert order.coffee == "Cappuccino"
    assert order.price == 3.5

def test_order_all_orders():
    customer1 = Customer("JohnDoe")
    customer2 = Customer("JaneDoe")
    order1 = Order(customer1, "Cappuccino", 3.5)
    order2 = Order(customer2, "Latte", 4.0)
    