from PILgraphicObject import*

class Obstacle(PILgraphicObject):

    def __init__(self, x, y):
        PILgraphicObject.__init__(self, x, y)
        self.SetImage("tree.png")
        