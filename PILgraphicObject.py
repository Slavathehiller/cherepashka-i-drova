from PIL import Image, ImageTk

class PILgraphicObject:
    BaseImage = None
    DefaultImage = None

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def SetImage(self, imageFileName):
       self.BaseImage = Image.open(imageFileName).convert('RGBA')
       self.DefaultImage = ImageTk.PhotoImage(self.BaseImage)

    def GetCurrentImage(self):
        return self.DefaultImage


   
       