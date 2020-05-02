from PIL import Image, ImageTk

class PILgraphicObject:
    BaseImage = None
    DefaultImage = None
    CurrentImage = None
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    #def LoadImage(self, property, imageFileName):
    #   image = Image.open(imageFileName)
    #   property = ImageTk.PhotoImage(image)

    def SetImage(self, imageFileName):
       self.BaseImage = Image.open(imageFileName)
       #self.LoadImage(self.DefaultImage, imageFileName)
       self.DefaultImage = ImageTk.PhotoImage(self.BaseImage)
       self.CurrentImage = self.DefaultImage

    def GetCurrentImage(self):
        return self.CurrentImage

   
       