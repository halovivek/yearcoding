class Person:
    def greet(self):
        print("i am person")

class Teacher(Person):
    def greet(self):
        Person.greet(self)
        print("i am teacher")

class Student(Person):
    def greet(self):
        Person.greet(self)
        print("I am student")

class TeachingAssistance(Person):
    def greet(self):
        Person.greet(self)
        print("I am Teaching Assistance")

x = TeachingAssistance()
x.greet()
