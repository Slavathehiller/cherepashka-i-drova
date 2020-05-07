from PILgraphicObject import*

class Wood(PILgraphicObject):

    def __init__(self, x, y):
        PILgraphicObject.__init__(self, x, y)
        self.SetImage("wood.png")
  
        
        