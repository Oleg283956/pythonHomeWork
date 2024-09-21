class Horse():
    x_distance = 0
    sound = 'Frrr'

    def __init__(self):
        self.x_distance = Horse.x_distance
        self.sound = Horse.sound

    def run(self, dx):
        self.x_distance += dx

class Eagle():
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self):
        self.y_distance = Eagle.y_distance
        self.sound = Eagle.sound

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse,Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def get_pos(self):
        res = ()
        res += self.x_distance,self.y_distance,
        return res

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def vioce(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.vioce()
