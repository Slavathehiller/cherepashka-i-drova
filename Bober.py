from wood import*
from obstacle import*
from zver import*
from Consts import*
from random import*
from PILgraphicObject import*

class Bober(Zver):
    name = "Бобер"
    map = None
    fearRange = 4

    def __init__(self, map, x, y):
        self.SetImage('bober.png')
        self.map = map

    def SetImage(self, imageFileName):
        Zver.SetImage(self, imageFileName)        


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
        return (self.map.isFree(tryX, tryY) or self.map.isWood(tryX, tryY) or self.map.isObstacle(tryX, tryY)) and not self.map.isHome(tryX, tryY)

    def NormalAction(self):
        nearobject = self.map.turtle
        #for object in self.map.activeObjects:
            #if self.map.distance(object.x, object.y, self.x, self.y) < self.map.distance(nearobject.x, nearobject.y, self.x, self.y) and not isinstance(object, Bober):
               # nearobject = object
        if self.map.distance(nearobject.x, nearobject.y, self.x, self.y) < self.fearRange:
            deltaX = nearobject.x - self.x
            deltaY = nearobject.y - self.y
            if abs(deltaX) > abs(deltaY):
                if deltaX > 0:
                    direction = Left
                else:
                    direction = Right
            else:
                if deltaY > 0:
                    direction = Up
                else:
                    direction = Down
        else:
            direction = randint(1, 4)
        if self.ICanMove(direction):
            self.move(direction)
            for i in range(len(self.map.staticobjects)):
                if isinstance(self.map.staticobjects[i], Obstacle) and self.map.staticobjects[i].x == self.x and self.map.staticobjects[i].y == self.y:
                    del self.map.staticobjects[i]
                    wood = Wood(self.x, self.y)
                    self.map.staticobjects.append(wood)
                