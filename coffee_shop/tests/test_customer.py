import pytest
from coffee import Coffee  
from customer import Customer  
from order import Order  

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("A" * 16)
    Customer("ValidName")



def test_customer_create_order():
    customer = Customer("AnnGlorious")
    order = customer.create_order("Cappuccino", 3.5)
    assert isinstance(order, Order)
    assert order.customer == customer
    assert order.coffee == "Cappuccino"
    assert order.price == 3.5

def test_customer_orders():
    customer = Customer("AnnGlorious")
    order1 = Order(customer, "Cappuccino", 3.5)
    order2 = Order(customer, "Latte", 4.0)
    assert customer.orders() == [order1, order2]

def test_customer_coffees():
    customer = Customer("AnnGlorious")
    order1 = Order(customer, "Cappuccino", 3.5)
    order2 = Order(customer, "Latte", 4.0)
    assert customer.coffees() == {"Cappuccino", "Latte"}

def test_customer_most_aficionado():
    customer1 = Customer("AnnGlorious")
    customer2 = Customer("AnnGlorious")
    order1 = Order(customer1, "Cappuccino", 3.5)
    order2 = Order(customer2, "Cappuccino", 4.0)
    assert Customer.most_aficionado("Cappuccino") == customer2