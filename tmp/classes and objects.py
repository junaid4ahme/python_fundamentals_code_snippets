# Write a program which will generate car details brochure when entered the car specs.

class Vehicle:
    def __init__(self):
        self.type1 = "Car"
        self.type2 = "SUV"
        self.type3 = "Commercial"


class Car(Vehicle):
    def __init__(self, make, model, fuel, drive, engine, turbo):
        Vehicle.__init__(self)
        self.make = make
        self.model = model
        self.fuel = fuel
        self.drive = drive
        self.engine = engine
        self.turbo = turbo

    def intro1(self):
        print("This right here is ", self.make, "{}.".format(self.model))
        print("Its got ", self.drive, "drive", "with ", self.engine, "layout.")
        print("It comes under", self.type1, "Category.")

    def intro2(self):
        print("This right here is ", self.make, "{}.".format(self.model))
        print("Its got ", self.drive, "drive", "with ", self.engine, "layout.")
        print("It comes under", self.type2, "Category.")


car1 = Car("Porsche", "911 Turbo S", "Petrol", "Rear Wheel", "Mid Engine", "Twin Turbo")
car2 = Car("Bugatti", "Veyron Sport", "Petrol", "All Wheel", "Mid Engine", "Naturally Aspirated")
car3 = Car("Ferrari", "458 Italia", "Petrol", "Rear Wheel", "Mid Engine", "Naturally Aspirated")
car4 = Car("Range Rover", "Evoque", "Diesel", "All Wheel", "Front", "Naturally Aspirated")
car5 = Car("Mercedes", "AMG GTR", "Diesel", "Rear Wheel", "Front", "Naturally Aspirated")


car1.intro1()
print("\n")
car2.intro1()
print("\n")
car3.intro1()
print("\n")
car4.intro2()
print("\n")
car5.intro1()
