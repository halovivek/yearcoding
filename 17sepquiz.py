class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

startDate = Date( 3,11, 2020)

startDate = Date(31, 3, 2020)

class Date:
    LAST_MONTH = 12
    LAST_DAY = 31
    def __init__(self, day, month, year):
        if month > self.LAST_MONTH:
            raise Exception(f"Month cannot be greater than {self.LAST_MONTH}")
        if day  > self.LAST_DAY:
            raise Exception(f"Day cannot be greater than {self.LAST_DAY}")
        self.day = day
        self.month = month
        self.year = year

startDate = Date(3,11,2020)
startDate = Date(31,13,2020)