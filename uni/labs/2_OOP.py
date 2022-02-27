class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def print_person(self):    
        print(f"Name: {self.name}\tAge: {self.age}")

class Student(Person):
    def __init__(self, name, age, college):
        super().__init__(name, age) # Inherits name, age from the super class 
        self.college = college

    def print_college(self):
        print(f"College: {self.college}")

class CSStudent(Student):
    def __init__(self, name, age, college, subject, grade):
        super().__init__(name, age, college) # Inherits name, age and college from the super class
        self.subject = subject 
        self.grade = grade

    def print_all(self):
        self.print_person()
        self.print_college()
        print(f"Subject: {self.subject}\tGrade: {self.grade}")

s1 = CSStudent('Atharva Auti', 21, 'SAKEC', 'Python', 100)

s1.print_all()
# s1.print_person()
# s1.print_college()
