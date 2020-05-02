from Consts import*
from zver import*
from cherepashka import*
from random import*

class Mole(Zver):
    name = "Крот"
    isSlow = False
    step = 0
    sniffRange = 4
    map = None

    def __init__(self, map):
        self.SetImage('krot.gif')
        self.map = map

    def move(self, direction):
        if not self.isSlow or self.step % 2 == 0:
            Zver.move(self, direction)
        else:
            print(self.name + " стоит на месте")
            self.step = self.step + 1

    def ICanMove(self, direction):
        tryX, tryY = self.x, self.y
        if direction == Up:
            tryY = tryY - 1
        if direction == Down:
            tryY = tryY + 1
        if direction == Left:
            tryX = tryX - 1
        if direction == Right:
            tryX = tryX + 1
        return self.map.isFree(tryX, tryY) or self.map.isTurtle(tryX, tryY)


    def NormalAction(self):
        if self.map.distanceToTurtle(self.x, self.y) < self.sniffRange and not self.map.turtle.IinHome():
            deltaX = self.map.turtle.x - self.x
            deltaY = self.map.turtle.y - self.y
            if abs(deltaX) > abs(deltaY):
                if deltaX > 0:
                    direction = Right
                else:
                    direction = Left
            else:
                if deltaY > 0:
                    direction = Down
                else:
                    direction = Up
        else:
            direction = randint(1, 4)
        if self.ICanMove(direction):
            self.move(direction)
        if self.map.isTurtle(self.x, self.y):
            return LOSE
        else:
            return NORMAL