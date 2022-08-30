#This is snake programming practice

class Snake:
    name = "Rajanagam"

    def modifyname(self, new_name):
        self.name = new_name


snake1 = Snake()
print(snake1.name)

#modify the name
snake1.modifyname("Cobra")

print(snake1.name)