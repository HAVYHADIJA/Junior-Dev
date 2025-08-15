#Inheritance
class Pet:
     def __init__(self, name,age ):
        self.name = name
        self.age = age

     def  show(self) :
        print(f"My name is  {self.name} and i am  {self.age} years old.")

class cat(Pet):
        def speak(self):
         print("Meow")

class dog(Pet):
    def speak(self):
        print("Woof")

p = dog("bill", 2)
p.show()
c = cat("kitty", 1)
c.show()
c.speak()
p.speak()

#inheritance
class Parent:
    hair_color = "black"
class Child(Parent):
    hair_color = "brown"  #overriding the parent class attribute

class Person:
    speaks = "English"  # class attribute
class Student(Person):
    def __init__(self):
        super().__init__()
        self.speaks.append("German") #extending the class attribute









        
    

