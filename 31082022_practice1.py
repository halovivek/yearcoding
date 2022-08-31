class Employee:

    def __init__(self, name ,salary, project):
        self.name = name
        self.salary = salary
        self.project = project

    def show_details(self):
        print("The name is ", self.name, "and salary is " ,self.salary)

    def show_project(self):
        print("The project working is", self.project , "and salary is", self.salary)

# entering the details to the variables and class
employee1 = Employee("Vinayagar", 200000,"gifting")
employee2 = Employee("Vivek", 20000, "Trading")

employee1.show_project()
employee2.show_project()
employee1.show_details()
employee2.show_details()