print('Kids introduction')


class Participants:
    # common attributes that class poses
    def __init__(self):
        self.weight = '55kg'
        self.gender = 'male'
        self.sport = 'wrestling'

    # actions of class
    def talk(self):
        print('My weight is ', self.weight)
        print('I am ', self.gender)
        print('I am competing in ', self.sport)


class Kids:
    def __init__(self):
        self.std = '4th'
        self.teacher = 'Mr Harrington'

    def tell(self):
        print('I study in ', self.std)
        print('My Teacher name is ', self.teacher)


k1 = Kids()
k1.tell()

print('\n', 'Wrestlers introduction:')
# creating objects
w1 = Participants()
w1.talk()
