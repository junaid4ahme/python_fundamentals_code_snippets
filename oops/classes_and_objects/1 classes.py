# CLASS:
# A CLASS IS A BLUEPRINT BY USING THAT WE CAN CREATE MULTIPLE OBJECTS.
# CLASS IS ARTIFICIAL ENTITY
# OBJECT IS REAL ENTITY
# BY USING CLASS WE CAN CREATE AN OBJECT.
# A GOOD EXAMPLE WOULD BE COLOUR RED, BLUE, GREEN,YELLOW, BLACK THEY ALL ARE THE OBJECTS OF COLOUR CLASS
# LILY, ROSE, JASMINE, TULIP THEY ALL ARE THE OBJECT OF FLOWERS CLASS.
# THESE OBJECTS POSSESS CERTAIN PROPERTIES. PROPERTIES - VARIABLES LIKE COLOR, SMELL, SHAPE
# A CLASS IS THE COMMON BEHAVIOUR OF GROUP OF OBJECTS

# HERE I WILL CREATE A CLASS WITH ALL THE DETAILS ABOUT A PROGRAMMER AND I WILL USE THOSE DETAILS LATER.


class Programmer:
    kind = "human"

    def __init__(self):
        self.name = "Jonah Hex"
        self.age = 25
        self.town = "New Mexico County"
        self.project = "Zombie"
        self.exp = 12

    def intro1(self):
        print("my name is ", self.name)
        print("my age is ", self.age)
        print("my hometown is ", self.town)

    def pres1(self):
        print("my exp is ", self.exp)
        print("my project is ", self.project)
        print("my kind is ", self.kind)


me = Programmer()

me.pres1()
me.intro1()
