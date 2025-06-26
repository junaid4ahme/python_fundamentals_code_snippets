"""
Inner Class:
            It is the class created inside other class.
            there is special method to call the inner class and create object from inner class.
"""


# LET'S CREATE OUTER CLASS:

class Pirate:
    def __init__(self):
        self.name = "jack Sparrow"
        self.age = 35

    def say(self):
        print("Iam ", self.name)
        print("I have seen", self.age, "winters")

    class Cases:
        def __init__(self):
            self.case = "Murder, Theft, Piracy"

        def tell(self):
            print("My charges are", self.case)


# LETS CREATE OBJECTS NOW:

p1 = Pirate()
p2 = p1.Cases()

p1.say()
p2.tell()
