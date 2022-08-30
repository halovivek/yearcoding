class SnakeName:
    """snake name inserting inside a method"""
    def __init__(self,name):
        self.name = name
    def __init__(self,newname):
        self.name = newname

snake1 = SnakeName("Rajanagam")
print(snake1.name)

snake1.newname = "cobra"
print(snake1.newname)