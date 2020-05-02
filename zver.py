from PILgraphicObject import*
from Consts import*

class Zver:
    x = 0
    y = 0
    step = 0
    name = ""
    orientation = Right
    RightImage = None
    LeftImage = None
    
    def SetImage(self, imageFileName):
        PILgraphicObject.SetImage(self, imageFileName)        
        self.RightImage = self.DefaultImage
        image = self.BaseImage.transpose(Image.FLIP_LEFT_RIGHT)
        self.LeftImage = ImageTk.PhotoImage(image)
        #self.CurrentImage = self.RightImage


    def move(self, direction):
        if direction == Up:
            self.y = self.y - 1
        if direction == Left:
            self.x = self.x - 1
            self.orientation = direction
        if direction == Down:
            self.y = self.y + 1
        if direction == Right:
            self.x = self.x + 1
            self.orientation = direction
        self.step = self.step + 1
        print(self.name + " переходит в точку", self.x, self.y)

    def GetCurrentImage(self):
        if self.orientation == Left:
            return self.LeftImage
        else:
            return self.RightImage