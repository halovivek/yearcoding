class RateofIntrest:
    def __int__(self, name, loan, intrerst):
        self.name = name
        self.loan = loan
        self.intrerst = intrerst
    def calculate_intrest(self):
        print("The charged intrest rate to ", self.loan * self.intrerst)

p1 = RateofIntrest("OVM",50000, 0.05)
p2 = RateofIntrest("Testing", 30000, 0.08)

p1.calculate_intrest()
p2.calculate_intrest()

