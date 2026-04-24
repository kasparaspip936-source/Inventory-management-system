Inventory Management System – OOP Coursework
1. Introduction
1.1 What is the application?

This project is an Inventory Management System developed in Python using Object-Oriented Programming (OOP) principles. The system manages different categories of items, stores them in a centralized inventory, and allows clients to create and manage orders.

The application supports:

Multiple item types (Electronics, Vehicles, Furniture, Tools)
Centralized inventory using a Singleton pattern
Client order management
Reading data from a file
Writing processed results to a file

1.2 How to run the program
Requirements
Python 3 installed
Project structure

Make sure all files are in the same folder:

data.txt – input data file (items and clients)
inventory.py – Singleton inventory class
item.py – base Item class
sub_classes.py – item subclasses
kursinis2.py – main program file
test.py – unit tests
rez.txt – output file (generated)
Run the main program

Open a terminal in the project folder and run:

  python kursinis2.py

What the program does
Reads data from data.txt
Creates item and client objects
Adds items automatically to the inventory
Assigns orders to clients
Writes results to rez.txt
Run unit tests
python test.py

This runs all tests and verifies system functionality.

1.3 How to use the program
The system runs automatically based on data.txt
No user input is required
Output is written to rez.txt

2. Body / Analysis
   
2.1 OOP Principles

Encapsulation

Encapsulation is implemented using private attributes and property methods.
Example:

@property
def name(self):
    return self._name
Inheritance

Inheritance is used through a base Item class and subclasses:

Electronics
Vehicle
Furniture
Tool

Each subclass extends the base class with additional attributes.

Polymorphism

Polymorphism is implemented by overriding the display_info() method in each subclass, allowing different item types to define their own output format.

Abstraction

The Item class provides a general structure for all item types, hiding implementation details while exposing common behavior.

2.2 Design Pattern – Singleton

The Inventory class uses the Singleton pattern to ensure only one instance exists.

class Inventory:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.items = []
        return cls._instance

This ensures all items are stored in one shared inventory.

2.3 Composition

The system uses composition to model relationships:

A Client has an Order
An Order contains multiple Selected_Item objects

This reflects real-world ordering systems.

2.4 File Reading and Writing

The program reads from data.txt and creates objects dynamically.

Example format:

Electronics,1,Laptop,1200,50,2
Client,Alice

The program writes results to rez.txt, including:

Inventory contents
Client orders
Total prices
2.5 Code Structure

The project is divided into multiple files:

inventory.py – inventory logic
item.py – base class
sub_classes.py – subclasses
kursinis2.py – main execution file
test.py – unit tests

This improves readability and organization.

2.6 Unit Testing

The project includes unit tests using Python’s unittest framework.

Tested functionality includes:

Item creation and total value
Subclass behavior
Inventory Singleton behavior
Order calculations
Client operations

Example:

def test_total_price(self):
    order = Order()
    item1 = Item(1, "Test1", 10.0, 5)
    item2 = Item(2, "Test2", 20.0, 5)
    order.add_item(item1, 1)
    order.add_item(item2, 2)
    self.assertEqual(order.total_price, 50.0)
    
3. Results
   
The system successfully manages multiple item types.
Inventory is centralized using a Singleton pattern.
File input allows dynamic object creation.
Orders are processed correctly with accurate totals.
Output is written to a file.
Unit tests confirm correctness of functionality.

4. Conclusions

This project demonstrates the effective use of Object-Oriented Programming in Python.

It successfully:
    Implements all four OOP principles
    Uses the Singleton design pattern
    Demonstrates composition relationships
    Supports file-based input and output
    Includes unit testing
    Possible improvements
    Stock validation when ordering
    Automatic stock updates
    Command-line interface
    Better error handling
    Database integration
