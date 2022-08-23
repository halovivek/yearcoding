class Salesperson:
    def __int__(self,name,age):
        self.name = name
        self.age = age
        self.salesamount =0
    def make_sale(self,money):
        self.salesamount += money

    def show(self):
        print(self.name,self.age,self.salesamount)


s1 = Salesperson('bob',25)
s2 = Salesperson('Vasantha', 53)
s3 = Salesperson('Rajagopalan','74')

s1.make_sale(1000)
s1.make_sale(2000)
s2.make_sale(5000)
s2.make_sale(5000)
s3.make_sale(20000)

s1.show()
s2.show()
s3.show()
