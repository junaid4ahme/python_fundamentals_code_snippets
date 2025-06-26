# ABSTRACTION:
#                     HIDING UNNECESSARY PART OF THE DATA FROM USER.
"""
In-short in abstraction means we can control how many instance variables a method inside
 a class can read.
means there are a lot of instance variable but a method is using only using 3-4 of them
there will be other method which is using remaining instance variables.
"""

# EXAMPLE:


class Car:
    def __init__(self, make, model, speed, drive, meter, year):
        self.make = make
        self.model = model
        self.speed = speed
        self.drive = drive
        self.meter = meter
        self.year = year

    def specs(self):
        print("Here it is ", self.make, self.model, "with top speed of ", self.speed, "comes with ", self.drive)

    def life(self):
        print("It has ran over ", self.meter, "miles and Baught in year", self.year)


# lets create an object:

car1 = Car("Bugatti", "Veyron", 200, "AWD", 300, 2016)

# car1.specs()
car1.life()
