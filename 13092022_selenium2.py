"""
Creating a class by class keyword
creating a function called method inside the class
Just a sample program for further training
"""
class Calculator:
    num = 100

    def getData(self):
        print("This is my getdata details")

    print(num)



obj = Calculator()
obj.getData()
obj.num = 200
print(obj.num)
