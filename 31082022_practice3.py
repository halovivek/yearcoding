class Bird:
    def intro(self):
        print("hi there are so many birds")

    def flight(self):
        print("Not all birds will fly")


class Sparrow(Bird):
    def flight(self):
        print("it can fly")


class Ostrich(Bird):
    def flight(self):
        print("it cannot fly")


bird01 = Bird()
sparrow1 = Sparrow()
otter = Ostrich()

bird01.intro()
bird01.flight()

sparrow1.intro()
sparrow1.flight()

otter.intro()
otter.flight()
