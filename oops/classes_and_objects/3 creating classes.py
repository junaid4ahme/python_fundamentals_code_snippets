"""
Syntax:
class Classname(self):
    commonvariables = value

    def __init__(self):
        self.name = "value"
        self.age = "value"

"""


class Person:
    def __init__(self):
        self.name = "Jack"
        self.age = 20

    def intoduce(self):
        print("my name is ", self.name)
        print("my age is ", self.age)


p1 = Person()
p1.intoduce()

"""
Constructors:
They are responsible for creating objects 
they holds the parameters and properties of objects

There are two types of constructors.
    1_poc.py. Default constructor
    2. Parameterized constructor
"""

# PARAMETERIZED CONSTRUCTOR:


class Pirate:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Intro(self):
        print("the name is Captain", self.name)
        print("and i have seen", self.age, "winters")


pirate1 = Pirate("Jack", 35)
pirate1.Intro()


pirate2 = Pirate("Gibbs", 50)
pirate2.Intro()

