class Player:
    Team_name = "Team2022"
    def __init__(self,name,age):
        self.name = name
        self.age  = age
    def display_info(self):
        return f"The {self.name} player has {self.age} years old"

player01 = Player("a1",25)
player02 = Player("a2",99)

print(player01.age)
print(player02.name)
print(player02.display_info())
print(player01.display_info())