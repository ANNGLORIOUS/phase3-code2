import pytest
from coffee import Coffee  
from order import Order 
from customer import Customer  

def test_order_price_validation():
    customer = Customer("AnnGlorious")
    with pytest.raises(ValueError):
        Order(customer, "Cappuccino", 0.9)
    with pytest.raises(ValueError):
        Order(customer, "Cappuccino", 10.1)
    Order(customer, "Cappuccino", 5.0)

def test_order_properties():
    customer = Customer("AnnGlorious")
    order = Order(customer, "Cappuccino", 3.5)
    assert order.customer == customer
    assert order.coffee == "Cappuccino"
    assert order.price == 3.5

def test_order_all_orders():
    customer1 = Customer("AnnGlorious")
    customer2 = Customer("JaneDoe")
    order1 = Order(customer1, "Cappuccino", 3.5)
    order2 = Order(customer2, "Latte", 4.0)
    