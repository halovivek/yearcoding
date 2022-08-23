class Employee:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print(self.name, self.email)


e1 = Employee('John', 'john@gmail.com')
e2 = Employee('Jack', 'jack@yahoo.com')
e3 = Employee('Jill', 'jill@outlook.com')
e4 = Employee('Ted', 'ted@yahoo.com')
e5 = Employee('Tim', 'tim@xmail.com')