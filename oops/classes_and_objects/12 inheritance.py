"""
INHERITANCE:
                Creating a class from other class in such a way that the newly created class possess all the properties
                of parent class.
                Main class/Parent class >>>>> Derived class/Subclass
                Inheritance is the beauty of OOPS we can use the methods from superclass and also subclass
                all we have to do is just use the proper syntax
                if the super class is located inside other program still we can use it and we can call its methods.
                when we create a subclass object it contains a copy of superclass object.

syntax:
                class Childclass(ParentClass):

"""


class Yacht:
    def __init__(self):
        self.make = "Riva"
        self.model = "335"
        self.speed = 50
        self.cap1 = 7


class owner(Yacht):
    def __init__(self):
        self.owner = "Jack"
        self.year = 2019
        Yacht.__init__(self)

    def getName(self):
        return self.owner

    def getYear(self):
        return self.year

    def getMake(self):
        return self.make

y1 = owner()
print(y1.make)