class Person:
    """creating the person information"""
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place



person1 = Person("ovm",35,"denkanikotta")
person2 = Person("Vivek",45,"hosur")

print(person1)
print(person2)
print(person1.place)
print(person2.age)