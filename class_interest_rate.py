class RateofIntrest:
    intrest = 0.05
    def __int__(self,name,loan):
        self.name = name
        self.loan = loan
    def calculate_intrest(self):
        print("The charged intrest rate to ", self.loan * self.intrest)

p1 = RateofIntrest("OVM",50000)
RateofIntrest.intrest = 0.05
p2 = RateofIntrest("Testing", 30000)
RateofIntrest.intrest = 0.08
p1.calculate_intrest()
p2.calculate_intrest()

