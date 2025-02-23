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
#output: Toyota Corolla

# In this example, Car is a class with attributes make and model, and a method display_info that prints 
# information about the car. An object my_car is created using the Car class and its method is called to 
# display the car information.

# Understanding OOP principles and applying them in Python programming opens up a world of possibilities 
# for building robust, scalable, and maintainable software applications.

# Class Diagram
# Here is a class diagram that shows the car class, it's attributes, and the datatype for the attributes.
# Car
# id string pk
# make string
# model string

# 02Classes in Python

# Introduction
# In Python, a class is a blueprint for creating objects. Objects are instances of classes, and they can have attributes (variables) and methods (functions). Classes are a fundamental concept in object-oriented programming (OOP) that allows for code reusability and organization.

# Defining a Class
# To define a class in Python, you use the class keyword followed by the name of the class. Here is an example of a simple class named Person:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# In the example, Person is a class that has two attributes (name and age) and a method greet that returns a greeting message.

# Creating Objects
# Once a class is defined, you can create objects (instances of the class) by calling the class as if it were a function. Here is an example of creating two Person objects:
person1 = Person("Abdi", 30)
person2 = Person("Bao", 25)

# Each object created from the Person class will have its own name and age attributes.

# Instance Attributes and Methods
# Instance attributes are variables that belong to each object created from a class. These attributes can be accessed using dot notation. For example:

print(person1.name)  
# Output: Abdi

# Instance methods are functions defined within a class that operate on the object's data. These methods always have self as the first parameter, which refers to the object itself. For example:

print(person1.greet())  
# Output: Hello, my name is Abdi and I am 30 years old.

# Class Attributes and Methods
# Class attributes are variables that are shared by all instances of a class. They are defined outside of any method in the class. Class methods are methods that operate on class-level data rather than instance-level data. They are defined using the @classmethod decorator.

# Here is a class diagram that shows the person class:
#person
# id string pk
# name string
# age integer

# Inheritance

# 03Inheritance
# Inheritance
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit properties and behavior from another 
# class. In Python, inheritance is achieved by creating a new class that derives from an existing class, known as the base class or parent class.
#  The new class is called the derived class or child class. Through inheritance, the derived class can access and reuse the attributes and methods 
# of the base class.

# Benefits of Inheritance
# 1.	Code Reusability: Inheritance promotes code reusability by allowing classes to inherit properties and behaviors from existing classes, 
# reducing redundancy and promoting a modular approach to programming.

# 2.	Hierarchy: Inheritance allows the creation of class hierarchies, where more specialized classes inherit from more general classes, 
# facilitating a clear and organized structure in the code.

# 3.	Polymorphism: Inheritance allows polymorphic behavior, where objects of different classes can be treated as objects of a common 
# base class, promoting flexibility and extensibility in the code.

# Syntax Inheritance in Python
# Inheritance is the ability of a class to inherit attributes and methods from a parent class. In Python, you can create a new class that 
# inherits from an existing class by placing the name of the parent class in parentheses after the class name. Here is an example:

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

# In this example, the Employee class inherits from the Person class and adds an employee_id attribute.

# Class Diagram of Person and Employee
# Here is a class diagram that shows the relationship between the parent class, Person, and the child class, Employee. 
# This diagram shows the attributes of the Employee class, like the employee ID, and the attributes of the Person class, like the name and age.

# employees
# id string pk
# person_id string fk
# employee_id string

#^^^connects to vvv:: via the id string pk attribute

# persons
# id string pk
# name string
# age int


