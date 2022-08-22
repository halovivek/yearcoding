class Bankaccount:
    def __int__(self,name, balance =0):
        self.name = name
        self.balance = balance

    def display(self):
        print(self.name, self.balance)

    def withdraw(self, amount):
        self.balance -= amountm

    def deposit(self,amount):
        self.balance += amount


a1 = Bankaccount('Mike', 50000)
a2 = Bankaccount('Good', 20000)

a1.display()
a2.display()

a1.withdraw(10000)
a2.withdraw(30000)

a1.display()
a2.display()
