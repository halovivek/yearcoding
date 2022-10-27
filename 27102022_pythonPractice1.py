class MoveCharacters:
    def move_forward(self):
        print("move forward one step")
    def move_backward(self):
        print("move backward one step")
class JumpCharacters:
    def jump_forward(self):
        print("jump one step forward")
    def jump_backward(self):
        print("jump one step backwards")

class Pokeman(JumpCharacters,MoveCharacters):
    pass

p = Pokeman()
p.move_forward()
p.move_backward()
p.jump_forward()
p.jump_forward()
