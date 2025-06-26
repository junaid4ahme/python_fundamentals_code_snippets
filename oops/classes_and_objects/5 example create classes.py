# CREATE A CLASS WITH STUDENT WITH ALL THE PARAMETERS AND DISPLAY HIS PERCENTAGE ??

class Student:
    def __init__(self, name, rno, mark):
        self.name = name
        self.rno = rno
        self.mark = mark

    def res(self):
        print("Name: ", self.name)
        print("Roll No. ", self.rno)
        x = sum(self.mark)
        y = x / len(self.mark)
        print("The Percentage: %.2f%%" % y)


name = input("Name of the student: ")
rno = int(input("Roll No. of Student: "))
marks = [int(i) for i in input("Specify marks Separated by ',': ").split(",")]
Junaid = Student(name, rno, marks)
Junaid.res()
