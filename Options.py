from Consts import*
class SimpleOptions:
    SlowMoles = 0
    difficult = 1
    sizeX = 15
    sizeY = 10
    
    def GetMoleCount(self):
        if self.difficult == Hard:
            return 3
        if self.difficult == Normal:
            return 2
        return 1
    MoleCount = property(fget=GetMoleCount)

    def GetWoodCount(self):
        return 5 - self.difficult
    WoodCount = property(fget=GetWoodCount)

    def GetObstacleCount(self):
        return 8 - self.difficult
    ObstacleCount = property(fget=GetObstacleCount)