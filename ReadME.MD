# SA.:Phase 3 Code Challenge: Assessment: Coffee Shop Domain Modeling
## Setup and Preparation

   - Create a new directory for your project named `coffee_shop`.
   - Set up a virtual environment within this directory using `pipenv`:
     ```bash
     pipenv install
     pipenv shell
     ```
   - Install any necessary packages, such as `pytest` for testing:
     ```bash
     pipenv install pytest
     ```
#### By **{List of contributors}**
This project was created and is sole property of Annglorious mueni.

### Objectives
Using object-oriented programming principles, create a Python application from scratch to model a Coffee Shop domain. This assessment will test your ability to design classes, implement methods, establish relationships between objects, and handle data appropriately.

 ### Project overview

 #### Coffee Class
Represents a coffee type and manages related orders.

1. Methods in the class 
* __init__(name): Initializes a Coffee instance with a name. The name must be a string of at least 3 characters.
* Name: Property to get the name of the coffee.
* Orders(): Returns a list of Order objects associated with this coffee.
* Customers(): Returns a set of Customer objects who have ordered this coffee.
* Num_orders(): Returns the number of orders for this coffee.
* Average_price(): Returns the average price of orders for this coffee. If there are no orders, it returns 0.

#### Customer Class
Represents a customer who can place orders for coffee.

1. Methods
* __init__(name): Initializes a Customer instance with a name. The name must be a string between 1 and 15 characters.
* Name: Property to get the name of the customer.
* Create_order(coffee, price): Creates a new Order for this customer.
* Orders(): Returns a list of Order objects associated with this customer.
* Coffees(): Returns a set of coffee names that this customer has ordered.
* Most_aficionado(coffee): Class method that returns the customer who made the most expensive order for a given coffee.

#### Order Class
Represents an order made by a customer for a specific coffee.

1. Methods
* __init__(customer, coffee, price): Initializes an Order instance with a customer, coffee, and price. The price must be a float between 1.0 and 10.0.
* Customer: Property to get the customer who placed the order.
* Coffee: Property to get the coffee ordered.
* Price: Property to get the price of the order.
* All_orders(): Class method that returns a list of all orders.

### Testing
The pytest framework is used to test the functionality of the classes. The tests cover validation, order creation, and retrieval methods.

#### Test Cases
##### Coffee Test
1. Test_coffee_name_validation: Ensures that a ValueError is raised if the coffee name is too short.
2. Test_coffee_orders: Checks that the orders method returns the correct orders for a coffee.
3. Test_coffee_customers: Verifies that the customers method returns the correct set of customers for a coffee.
4. Test_coffee_num_orders: Confirms that the num_orders method returns the correct number of orders.
5. Test_coffee_average_price: Ensures that the average_price method calculates the average price of orders correctly.

##### Customer Test 
1. Test_customer_name_validation: Ensures that a ValueError is raised if the customer name is too short or too long.
2. Test_customer_create_order: Verifies that the create_order method creates a new order with the correct details.
3. Test_customer_orders: Checks that the orders method returns the correct orders for a customer.
4. Test_customer_coffees: Ensures that the coffees method returns the correct set of coffee names for a customer.
5. Test_customer_most_aficionado: Confirms that the most_aficionado method returns the customer with the most expensive order for a coffee.

##### Order
1. Test_order_price_validation: Ensures that a ValueError is raised if the order price is out of the valid range.
2. Test_order_properties: Verifies that the Order properties return the correct details.
3. Test_order_all_orders: Checks that the all_orders method returns the correct list of orders.

##### Usage 
To run the tests you should :
Use `pytest` to run your tests:
     ```bash
     pytest
     ```

## Setup/Installation Requirements
* One would need either linux or wsl for window users
* A copy of visual basic code installed
* A github account

1. Open your terminal and go to the directory you wish to work from.
2. Go to the following url using ur github account https://github.com/ANNGLORIOUS/phase3-code-2
3. Go to the code tab and clone the ssh key
4. Go back to the termina and type git clone <-followed by the ssh key you copied /cloned ->
5. Enter your new cloned repository and type in code .
6. On the visual studio code that has now opened, go to the the run tab and hit start debugging.
## Technologies Used
This program is built purely with python using the visual code environment.

## Support and contact details
For any issues please email me at annglorious.mueni@student.moringaschool.com
### License
Apache License 2.0


