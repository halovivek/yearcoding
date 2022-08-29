from dataclasses import dataclass

@dataclass()
class TestDrivenToCoin:
    value: float

    def add(self,other):
        if not isinstance(other,TestDrivenToCoin):
            return NotImplemented
        return TestDrivenToCoin(value= self.value + other.value)

my_coins = TestDrivenToCoin(value=120).add(TestDrivenToCoin(value=357.01))
print(my_coins)


@dataclass()
class TestDrivenToCoin:
    value: float

    def __add__(self, other):
        if not isinstance(other,TestDrivenToCoin):
            return
        return TestDrivenToCoin(value=self.value + other.value)

my_coins = TestDrivenToCoin(value=120) + TestDrivenToCoin (value= 357.01)
print(my_coins)
