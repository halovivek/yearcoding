# parent class
class Vehicle:
    def Vehicle_data(self):
        print("Hello from the class")


# child class
class Car(Vehicle):
    def Car_data(self):
        print("Hello from the Car class")


car01 = Car()
car01.Vehicle_data()
car01.Car_data()
