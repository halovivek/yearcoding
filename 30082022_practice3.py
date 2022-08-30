class Person:
    """creating the person information"""
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place

    """This is display all the datas which is collected in the above variable"""
    def display_data(self):
        print("my name is ",self.name, "my age is",self.age ,"i am staying in",self.place)





person1 = Person("ovm",35,"denkanikotta")
person2 = Person("Vivek",45,"hosur")

print(person1)
print(person2)
print(person1.place)
print(person2.age)

person1.display_data()
person2.display_data()