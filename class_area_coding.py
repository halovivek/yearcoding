class Areacalculation:

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def calcualte_area(self):
        return self.l * self.b
                                                m
area1 = Areacalculation(9,9)
area2 = Areacalculation(436,40.5)
print(area1.calcualte_area())
print(area2.calcualte_area())
