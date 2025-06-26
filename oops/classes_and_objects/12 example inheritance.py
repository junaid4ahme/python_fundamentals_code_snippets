# DERIVE THE RECTANGLE CLASS FROM CIRCLE CLASS AND FIND THE AREA OF BOTH.
class square:
    def __init__(self, side1):
        self.side1 = side1

    def area1(self):
        res = self.side1 * self.side1
        return res


class rec(square):
    def __init__(self, side1, side2):
        self.side2 = side2
        self.side1 = side1

    def area2(self):
        res = self.side1 * self.side2
        return res



a1 = square(10)
print(a1.area1())

a2 = rec(20, 10)
print(a2.area2())


