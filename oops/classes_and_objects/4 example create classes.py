# CREATE A CLASS VEHICLE WITH ATTRIBUTES OF IT ??


# LETS DEFINE CLASS:

class Vehicle:
    # LET'S CREATE A CONSTRUCTOR WITH ALL THE PARAMETERS.
    def __init__(self, speed, acc, drive):
        self.speed = speed
        self.acc = acc
        self.drive = drive

    # LET'S CREATE A FUNCTION INSIDE THE CLASS THERE CAN BE MULTIPLE FUNCTION INSIDE SAME CLASS.
    def specs(self):
        print("\n The speed is ", self.speed, "\n The Acceleration is ", self.acc, "\n The Drive is ", self.drive)


# LETS CREATE OBJECTS.

modelX = Vehicle(200, 2.5, "RWD")
modelX.specs()


#  LETS CREATE BUGATTI VEYRON.

veyron = Vehicle(280, 2, "AWD")
veyron.specs()
