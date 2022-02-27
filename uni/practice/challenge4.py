
class Student:
    def __init__(self, name, rollno, division, marks1, marks2):
        self.name = name
        self.division = division
        self.rollno = rollno
        self.marks1 = marks1
        self.marks2 = marks2

    def print_all(self):
        average = (self.marks1 + self.marks2) / 2
        print(f'\nName: {self.name} \nDivision: {self.division} \nRoll no: {self.rollno} \nAverage: {average}\n')

s1 = Student('Atharva Auti', 1, 'SE15', 100, 100)
s2 = Student('Elon Musk', 2, 'SE15', 77, 77)
s3 = Student('Bill Gates', 3, 'SE15', 66, 88)

s1.print_all()
s2.print_all()
s3.print_all()