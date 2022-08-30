class Person:
    def person_data(self, name, age):
        print("This is person classs")
        print("The name of the person is:", name, "The age of the employuee:", age)


# company parent class

class Company:
    def company_details(self, company_name, location):
        print("welcome to the company")
        print("The name of the company", company_name, "the location is", location)


# employee class child

class Employee(Person, Company):
    def employee_details(self, salary, skill):
        print("this is salary details", salary, "this is skill", skill)

emp01 = Employee()
emp01.person_data("Vivek",43)
emp01.employee_details(35000,"Testing")
emp01.company_details("confidential","denkanikotta")

