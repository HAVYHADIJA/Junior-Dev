#Classes
class Person:
    Tribe ="Baganda" #Class Attribute/Variable is shared by all instances of the class
    def __init__(self,name,age):#instace attribute
        self.name = name #self is a reference to the current instance of the class
        self.age = age
        #methods

    def greet(self):# This is a method that prints a greeting message
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def description(self):# This is a method that prints a description of the person
        print(f"{self.name} is {self.age} years old and belongs to the {self.Tribe} tribe.")


sarah = Person("Sarah", 20)
collins = Person("Collins", 21)

print(sarah.name)
print(sarah.age)
print(collins.name)
print(collins.age)
print(sarah.Tribe)

sarah.greet()
collins.greet()
sarah.description()
collins.description()

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students: 
            value += student.get_grade()
        return value / len(self.students)

s1 = Student("Alice", 20, 90)
s2 = Student("Bob", 22, 85)
s3 = Student("Charlie", 21, 88)

course  = Course("Math", 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)  # This will not be added since the max_students is
print(course.students[0].name) 
print(course.get_average_grade()) # Output: Alice
