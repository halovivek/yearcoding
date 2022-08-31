class Employee:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def getting_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age


person1 = Employee("Vivek", 42)
print(f"name of the employee {person1.name}", f"his age is {person1.getting_age()}")

person1.set_age(43)
print(f"name of the employee {person1.name}", f"his age is {person1.getting_age()}")
