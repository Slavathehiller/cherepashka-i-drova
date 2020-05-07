from background_grass import*
from Bober import*
from random import*
from mole import*
from Options import *
from math import*
from wood import*
from home import*
from obstacle import*

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

    def distance(self, x1, y1, x2, y2):
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def distanceToTurtle(self, x, y):
        return self.distance(self.turtle.x, self.turtle.y, x, y)

    def isTurtle(self, x, y):
        return self.turtle.x == x and self.turtle.y == y

    def isBober(self, x, y):
        return isinstance(self.GetObject(x, y), Bober)

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
        return not self.isTurtle(x, y) and not self.isMole(x, y) and not self.isWood(x, y) and not self.isObstacle(x, y) and not self.isHome(x, y) and not self.isBober(x, y) and not self.isOut(x, y)

    def isAvaliableforMole(self, x, y):
        return self.isFree(x, y) and self.distanceToTurtle(x, y) > 4

    def isAvaliableforBober(self, x, y):
        return self.isFree(x, y) 

    def isAvaliableforWood(self, x, y):
        return self.isFree(x, y)

    def isHome(self, x, y):
        return self.home.x == x and self.home.y == y


    def GetStaticObject(self, x, y):
        background = None
        for object in self.staticobjects:
            if object.x == x and object.y == y:
                if isinstance(object, Background):
                    background = object
                else:
                    return object
        return background


    def GetObject(self, x, y):
        for object in self.activeObjects:
            if object.x == x and object.y == y:
                return object
        if self.home.x == x and self.home.y == y:
            return self.home
        if self.turtle.x == x and self.turtle.y == y:
            return self.turtle
        return self.GetStaticObject(x, y)


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

    def placeBober(self):
        bober = Bober(self, randint(0, self.sizeX - 1), randint(0, self.sizeY - 1))
        while not self.isAvaliableforBober(bober.x, bober.y):
            bober.x = randint(0, self.sizeX - 1)
            bober.y = randint(0, self.sizeX - 1)
        self.activeObjects.append(bober)

    def placeBackground(self):
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                if not self.isHome(x, y):
                    grass = Background_grass(x, y)
                    self.staticobjects.append(grass)
                
    def placeHome(self):
        self.home = Home(0, 0)
        self.staticobjects.append(self.home)

    def createNewMap(self):
        self.staticobjects = []
        self.activeObjects = []
        self.woodCount = self.woodNumber
        self.placeHome()
        self.placeObstacles()
        self.placeBackground()
        self.placeWoods()
        self.placeMoles()
        self.placeBober()

    def activateActiveObjects(self):
        for activeobject in self.activeObjects:
            result = activeobject.NormalAction()
            if result != NORMAL:
                return result
        return NORMAL

    def tic(self):
        Result = self.activateActiveObjects()
        return Result