#Object Oriented Programming - Classes and Inheritance with Python

#Learn to implement classes and inheritance in Python for effective object-oriented 
#programming

#Overview
# This lesson covers the fundamentals of classes and inheritance in Python, exploring how 
# to create and use classes, implement inheritance, and leverage object-oriented principles 
# for robust software development.

# Let's Take a Look at the Key Concepts
# Classes:
    # Classes are the building blocks of OOP. They define the structure and behavior of 
    # objects. Each class can have attributes (variables) and methods (functions) 
    # associated with it.
# 
# Objects:
    # Objects are instances of classes. They represent a specific data structure with 
    # its own unique set of values for the attributes defined by the class.

# Encapsulation:
    # Encapsulation is the practice of bundling data (attributes) and methods (behavior) 
    # that operate on the data within a class. This helps in hiding the internal 
    # implementation details of an object and allows for better control over how the 
    # data is accessed and modified.

# Inheritance:
    # Inheritance is a mechanism in which a class (known as the child or subclass) 
    # inherits attributes and methods from another class (known as the parent or 
    # superclass). This promotes code reusability and allows for defining hierarchical 
    # relationships between classes.

# Polymorphism:
    # Polymorphism allows objects of different classes to be treated as objects of a 
    # common superclass. This enables flexibility in designing systems where different 
    # classes can have different implementations for common methods.

# Benefits of OOP
# 1. Modularity:
    # OOP promotes modular design, making it easier to break down a system into smaller, manageable 
    # components.

# 2.Code reusability:
    #Through inheritance and polymorphism, OOP encourages the reuse of existing code which leads to 
    # less duplication and easier maintenance.

# 3.Flexibility:
    # OOP allows for easier modification and extension of code as new classes can be added without 
    # affecting the existing codebase.

# 4.Scalability:
    # OOP supports building complex systems by breaking them down into smaller, 
    # interconnected objects.

# 5.Implementation in Python
    # Python is a popular programming language that fully supports OOP concepts. In Python, classes 
    # are defined using the class keyword, and objects are created by calling the class as if it were 
    # a function. Python also provides features like inheritance, encapsulation, and polymorphism to 
    # facilitate OOP development.

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car: {self.make} {self.model}")

my_car = Car("Toyota", "Corolla")
my_car.display_info()

# In this example, Car is a class with attributes make and model, and a method display_info that prints 
# information about the car. An object my_car is created using the Car class and its method is called to 
# display the car information.

# Understanding OOP principles and applying them in Python programming opens up a world of possibilities 
# for building robust, scalable, and maintainable software applications.

# Class Diagram
# Here is a class diagram that shows the car class, it's attributes, and the datatype for the attributes.

