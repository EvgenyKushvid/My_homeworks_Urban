class Horse:

    def __init__(self, x_distance = 0, sound="Frrr" ):
        super().__init__()
        self.x_distance = x_distance
        self.sound = sound
    def run (self, dx):
        self.x_distance = self.x_distance + dx
        return self.x_distance + dx

class Eagle:
    sound = "I train, eat, sleep, and repeat"
    def __init__(self, y_distance = 0):
        self.y_distance = y_distance

    def fly (self, dy):
        self.y_distance = self.y_distance + dy
        return self.y_distance

    def sound_(self):
        print('-->',self.sound )
        return self.sound

class Pegasus (Horse, Eagle):
    def move (self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance,self.y_distance)

    def voice (self):
        print(Eagle.sound)
#   у меня этот Пегас фырчит

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
