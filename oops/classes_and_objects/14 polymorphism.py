"""
POLYMORPHISM:
                multiple forms of the methods.
                it deals with methods.
"""


class French:
    def say(self):
        print("Bonjour")


class Italiano:
    def say(self):
        print("Cumista")


def greetings(x):
    x.say()


p1 = French()
p2 = Italiano()

greetings(p1)
greetings(p2)
