"""
Instance Variables:
these variables are specific to an object created by using a class.

To retrieve these variables we have to Use INSTANCE METHOD:
there are two types of Instance methods:
1. Getter Method.
                    It only retrieves the value of instance variable.

2. Setter Method.
                    It will retrieve the value as well as it will modify the value of instance variable.
"""


class Person:
    def __init__(self):
        self.name = "jack"
        self.id = 2020

    # getter Method here we are only retriving the value of an instance variable.
    def retrivid(self):
        return self.id

    def getNam(self):
        return self.name

    # setter method here we are modifying the value of an instance variable.
    def setName(self, name):
        self.name = name
        return self.name


e = Person()

print(e.getNam())
f = e.setName("Jonah")
print(f)





