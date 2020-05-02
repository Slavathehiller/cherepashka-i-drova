from PILgraphicObject import*

class Home(PILgraphicObject):
    home25 = None
    home50 = None
    homefull = None
    Stage = 0
    images = []

    def __init__(self, x, y):
        PILgraphicObject.__init__(self, x, y)
        self.SetImage("home0.gif")
        image = Image.open("home25.gif")
        self.home25 = ImageTk.PhotoImage(image)
        image = Image.open("home50.gif")
        self.home50 = ImageTk.PhotoImage(image)
        image = Image.open("homefull.gif")
        self.homefull = ImageTk.PhotoImage(image)
        self.images = [self.DefaultImage, self.home25, self.home50, self.homefull]


    def GetCurrentImage(self):
        return self.images[self.Stage]

    def NextStage(self):
        self.Stage = self.Stage + 1


