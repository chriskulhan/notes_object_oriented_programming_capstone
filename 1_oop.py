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


#notes from https://youtu.be/6c6NYPjO_rI

#parent class is Guitar:
class Guitar:
    #the init method is automatically being called everytime you create a new object (below: my_guitar)
    # def __init__(self): (changed this to add n_strings=6 parameter, so the default n_strings will be 6)
    def __init__(self, n_strings=6):
        #how many strings does the guitar have?
        #create an attribute:
        # self.n_strings = 6 changed this to use the n_strings parameter added above
        self.n_strings = n_strings
        #^^this attribute can be accessed outside of the class definition
        # by generating a guitar object

        self.play()
        #output: dum dum dum dum dum dum

        #try to add a secret attribute in the parent class:
        self.__cost = 50
        #check by printing my_guitar._ElectricGuitar__cost) below

    #create a new method:
    #in order to turn it into a method, you have to pass the self parameter: 
    # **if you only say def play():, you are creating a function
    def play(self):    
        #want this to print some type of melody:
        print("dum dum dum dum dum dum")

#Guitar() is the object   
# assign Guitar() to the variable my_guitar:
my_guitar = Guitar()
#print to see if it worked:
print(my_guitar.n_strings) 
#output: 6
# 
#Call the method play on the object itself:
my_guitar.play()   
#output:   dum dum dum dum dum dum

#INHERITANCE#******
#Own a guitar shop and want to keep track of the stock, 
#Allow a new class to inherit the attributes and methods of the class Guitar from above:
#parent class is now Guitar, and all the attributes are now available to ElectricGuitar by passing 
#it inside the parentheses: 

#Create new class called BaseGuitar that will inherite all the attributes of the Guitar class:
class BaseGuitar(Guitar):
    #only want to change is the number of strings
    #add another paramater called n_strings to the parent class called Guitar:
    #now looks like: def __init__(self, n_strings=6): above in parent class Guitar
    #add pass to this class to have all the attributes of the parent class
    pass
    #go to the very bottom to change the number of strings in the BaseGuitar:


#Child class is Electric Guitar:
class ElectricGuitar(Guitar):
    #if you want the child and the parent class to 100% match, type the "pass" statement:
    #pass

    #if you'd like to slightly alter the parent class, maybe to play louder:
    def playLouder(self):
        print("dum dum dum dum dum dum".upper())

    #add a secret (though not really) method to the parent class Electric Guitar:
    def __secret(self):
        #concatinate a private member from the parent class:
        #special way, trying to access self.__cost = 50 in class Guitar
        print("This guitar actually cost me $", self._Guitar__cost, "only!" )        

    #if you want to change the parameter in the child class, but not the parent class:
    #first do an init it the child class:
    def __init__(self):
        #because the child class inherited everything from the parent class, 
        # you will need to access the "super" function to access the init from the parent class
        #DO NOT pass the self parameter here:
        # super().__init__()
        # #now that we have access to the attributes in the parent class, replace
        # #the number of strings for the ElectricGuitar child class to 8:
        # self.n_strings = 8

        #change the above to accomodate the n_strings parameter added to the class Guitar
        # so remove the  self.n_strings = 8 and and pass the number of strings 
        # (n_strings = 8) in the super().__init__()
        super().__init__(n_strings=8)

        #add new attributes in the child class:
        #add colors: black = #000000 and white = #FFFFFF (hexidecimal colors)
        self.color = ("#000000", "FFFFFF")   

        #store some confidential information inside the child class:
        #how much does the guitar cost to the store owner?
        #create a "private member" by putting two underscores before the info you want hidden (not really hidden):
        #self.__cost = 50
           
#assign my_guitar to ElectricGuitar:
my_guitar= ElectricGuitar()
#can we access the n_strings here?:
# print(my_guitar.n_strings)
#output: 6

my_guitar.playLouder()
#output: DUM DUM DUM DUM DUM DUM

print("child class:", my_guitar.n_strings)
#output: child class: 8
print("parent class:", Guitar().n_strings)
#output: parent class: 6

#can you access the "secret info" in __cost?
# print(my_guitar.__cost)
#this will produce an error because you can't access it:
#output: Traceback (most recent call last):
#   File "/workspaces/notes_object_oriented_programming_capstone/1_oop.py", line 262, in <module>
#     print(my_guitar.__cost)
#           ^^^^^^^^^^^^^^^^
# AttributeError: 'ElectricGuitar' object has no attribute '__cost'

#the attribute __cost can be accessed this way:
#print(my_guitar._ElectricGuitar__cost)
#output: 50

#try to print again after adding the class to the parent and removing from child:
#seems hidden, but it's not:
# print(my_guitar._ElectricGuitar__cost)
#output: Traceback (most recent call last):
#   File "/workspaces/notes_object_oriented_programming_capstone/1_oop.py", line 287, in <module>
#     print(my_guitar._ElectricGuitar__cost)
#           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'ElectricGuitar' object has no attribute '_ElectricGuitar__cost'

#try to access the cost again, but remove the Electric from (child class ElectricGuitar)
print(my_guitar._Guitar__cost)
#prints!!!
#output: 50

#You really can't hide things in python, even in private, they are accessible.
#added a __secret method to the parent class, and it is accessbile:
#print the secret thing:
my_guitar._ElectricGuitar__secret()


#from BaseGuitar take in the number of strings "4" in the parentheses:
# print(BaseGuitar(4).n_strings)
# output: 4

#Verify changing the super().__init__(n_strings=8) in the Electric Guitar class worked:
print("my base guitar has", BaseGuitar(4).n_strings, "strings")
#output: my base guitar has 4 strings

print("my electric guitar has", my_guitar.n_strings, "strings" )
#output: my electric guitar has 8 strings

#Brocode video: https://youtu.be/an59YHkdK9A

#Inheritance

#class for all animals parent!:
class Animal:
    #class variable (all animals have to be alive)
    alive = True

    #methods:
    def eat(self):
        #what happens when we call this method:
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

    #testing out method overloading:
    def speak(self):
        print("Animal speaks")

#create classes for different types of animals:
#Rabbit is the child class, Animal is the parent class
#child class (Rabbit), inherits everything the Animal class has
class Rabbit(Animal):
    #pass allows complete inheritance from the parent class of Animal:
    # pass
    #add unique methods to the Rabbit class:
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    # pass
    #add unique method to the Fish class:
    def swim(self):
        print("This fish is swimming")
    

class Hawk(Animal):
    # pass
    #add unique methods to hawk class:
    def fly(self):
        print("This hawk is flying")
    #testing method overloading (added speak method to Animal SuperClass)
    def speak(self):
        print("Hawks screech") 

#create objects from the classes: 
rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#check to see if there is an alive variable in each of the objects:
print(rabbit.alive)
#output: True

print(fish.alive)
#output: True

print(hawk.alive)
#output: True

#check if there are eat functions in each objects: #this is wrong:
# print(rabbit.eat) no output, bound method
# print(fish.eat) wrong
# print(hawk.eat) wrong

#check if there are sleep functions in each object: #this is wrong!
# print(rabbit.sleep) wrong
# print(fish.sleep) wrong
# print(hawk.sleep) wrong

#check if the fish has an eat method:
fish.eat()
#output: This animal is eating

hawk.sleep()
#output: This animal is sleeping

rabbit.run()
# output: This rabbit is running
fish.swim()
#output: This fish is swimming
hawk.fly()
#output: This hawk is flying

 

# Method overriding
# re-write a method from the superclass in the underclass:
#added speak to the Superclass animal
#added an overwrite of speak in the hawk underclass

#this gets its attribute from the superclass Animal:
fish.speak()
#output: Animal speaks

#this gets its attribute from the underclass Hawk, it has overwritten the Superclass:
hawk.speak()
# output: Hawks screech


#Method overloading:
#Python does not natively support method overloading as in some other programming languages. 
# However, we can achieve a form of method overloading using default arguments or variable arguments.
class Calculator:
    def add(self, a, b=None):
        if b is not None:
            return a + b
        else:
            return a

calc = Calculator()

print(calc.add(2, 3))  
# Output: 5
print(calc.add(2))     
# Output: 2

#Polymorphism with Inheritance:
#A common use case of polymorphism is with inheritance, where different subclasses 
# implement the same method from a superclass in their own way. This allows for 
# flexible and reusable code.
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Circle drawn")

class Square(Shape):
    def draw(self):
        print("Square drawn")

shapes = [Circle(), Square()]

for shape in shapes:
    shape.draw()
    #TODO there was no output here. Figure out how to use this

#In the example, both Circle and Square classes inherit from the Shape class and provide 
# their own implementation of the draw method. When iterating through a list of shapes, 
# polymorphism allows each shape object to be treated uniformly, regardless of its 
# specific subclass.

#Polymorphism enhances code reusability, flexibility, and maintainability in object-oriented 
# programming, making it a powerful concept to leverage when designing applications in Python.
    

