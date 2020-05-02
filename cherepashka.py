from Consts import*
from zver import*
import winsound
from wood import*
from PILgraphicObject import*


class Turtle(Zver):
    name = "Черепаха"
    map = None
    CarryWood = False
    CarryWoodLeftImage = None
    CarryWoodRightImage = None


    def __init__(self, map):
        self.y = 0
        self.x = 1
        self.SetImage('turtle.gif')
        image = Image.open("turtlewood.gif")
        self.CarryWoodRightImage = ImageTk.PhotoImage(image)
        image1 = image.transpose(Image.FLIP_LEFT_RIGHT)
        self.CarryWoodLeftImage = ImageTk.PhotoImage(image1)

        self.map = map


    def move(self, direction):
        if self.ICanMove(direction):
            Zver.move(self, direction)


    def checkAndEat(self):
        if self.map.isHome(self.x, self.y):
            if self.CarryWood:
                self.CarryWood = False
                self.map.home.NextStage()
                if self.map.home.Stage == 3:
                    return WIN
                else:
                    return NORMAL
        if self.CarryWood:
            return NORMAL
        for i in range(len(self.map.staticobjects)):
            if isinstance(self.map.staticobjects[i], Wood) and self.map.staticobjects[i].x == self.x and self.map.staticobjects[i].y == self.y:
                del self.map.staticobjects[i]
                self.map.woodCount = self.map.woodCount - 1
                #winsound.PlaySound("Niam.wav", winsound.SND_ASYNC + winsound.SND_PURGE)
                self.CarryWood = True
                return NORMAL
        return NORMAL


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
        return self.map.isFree(tryX, tryY) or self.map.isWood(tryX, tryY) or self.map.isMole(tryX, tryY) or self.map.isHome(tryX, tryY)


    def IinHome(self):
        return self.map.isHome(self.x, self.y)

    def GetCurrentImage(self):
        if self.orientation == Left:
            if self.CarryWood:
                return self.CarryWoodLeftImage
            else:
                return self.LeftImage
        else:
            if self.CarryWood:
                return self.CarryWoodRightImage
            else:
                return self.RightImage
