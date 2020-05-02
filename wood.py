from PILgraphicObject import*

class Wood(PILgraphicObject):
    poisoned = False

    def __init__(self, x, y):
        PILgraphicObject.__init__(self, x, y)
        self.SetImage("wood.gif")
  
        
        