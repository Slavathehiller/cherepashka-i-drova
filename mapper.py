from random import*
from mole import*
from Options import *
from math import*
from wood import*
from home import*
from obstacle import*
import winsound

class MapManager:
    sizeY = 5
    sizeX = 5
    turtle = None
    home = None
    obstaclesNumber = 0
    molesNumber = 0
    slowMoles = 0
    woodNumber = 0
    staticobjects = []
    activeObjects = []
    woodCount = 0
    

    def __init__(self, turtle, options):
        self.turtle = turtle
        self.molesNumber = options.MoleCount
        self.slowMoles = options.SlowMoles
        self.woodNumber = options.WoodCount
        self.obstaclesNumber = options.ObstacleCount
        self.sizeY = options.sizeY
        self.sizeX = options.sizeX

    def distanceToTurtle(self, x, y):
        return sqrt((self.turtle.x - x) ** 2 + (self.turtle.y - y) ** 2)

    def isTurtle(self, x, y):
        return self.turtle.x == x and self.turtle.y == y

    def isMole(self, x, y):
        return isinstance(self.GetObject(x, y), Mole)

    def isOut(self, x, y):
        return x < 0 or y < 0 or x > self.sizeX - 1 or y > self.sizeY - 1

    def isObstacle(self, x, y):
        return isinstance(self.GetObject(x, y), Obstacle)

    def isWood(self, x, y):
        return isinstance(self.GetObject(x, y), Wood)

    def isObstacleOrOut(self, x, y):
        return self.isObstacle(x, y) or self.isOut(x, y)

    def isFree(self, x, y):
        return self.GetObject(x, y) == None and not self.isOut(x, y)

    def isAvaliableforMole(self, x, y):
        return self.isFree(x, y) and self.distanceToTurtle(x, y) > 4

    def isAvaliableforWood(self, x, y):
        return self.isFree(x, y)

    def isHome(self, x, y):
        return self.home.x == x and self.home.y == y

    def GetObject(self, x, y):
        for object in self.activeObjects:
            if object.x == x and object.y == y:
                return object
        if self.home.x == x and self.home.y == y:
            return self.home
        if self.turtle.x == x and self.turtle.y == y:
            return self.turtle
        for object in self.staticobjects:
            if object.x == x and object.y == y:
                return object
        return None


    def placeObstacles(self):
        self.obstacles = []
        for i in range(self.obstaclesNumber):
             obstacle = Obstacle(randint(0, self.sizeX - 1), randint(0, self.sizeY - 1))
             while not self.isAvaliableforMole(obstacle.x, obstacle.y):
                 obstacle.x = randint(0, self.sizeX - 1)
                 obstacle.y = randint(0, self.sizeY - 1)
             self.staticobjects.append(obstacle)


    def placeMoles(self):
        self.moles = []
        for i in range(self.molesNumber):
            mole = Mole(self)
            mole.isSlow = self.slowMoles == 1
            mole.x = randint(0, self.sizeX - 1)
            mole.y = randint(0, self.sizeY - 1)
            while not self.isAvaliableforMole(mole.x, mole.y):
                mole.x = randint(0, self.sizeX - 1)
                mole.y = randint(0, self.sizeY - 1)
            self.activeObjects.append(mole)


    def placeWoods(self):
        for i in range(self.woodNumber):
            wood = Wood(randint(0, self.sizeX - 1), randint(0, self.sizeY - 1))
            while not self.isAvaliableforWood(wood.x, wood.y):
                wood.x = randint(0, self.sizeX - 1)
                wood.y = randint(0, self.sizeY - 1)
            self.staticobjects.append(wood)

    def placeHome(self):
        self.home = Home(0, 0)
        self.staticobjects.append(self.home)

    def createNewMap(self):
        self.staticobjects = []
        self.activeObjects = []
        self.woodCount = self.woodNumber
        self.placeHome()
        self.placeObstacles()
        self.placeWoods()
        self.placeMoles()

    def activateActiveObjects(self):
        for activeobject in self.activeObjects:
            result = activeobject.NormalAction()
            if result != NORMAL:
                return result
        return NORMAL

    def tic(self):
        Result = self.activateActiveObjects()
        return Result