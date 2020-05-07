from background import*
class Background_grass(Background):

    def __init__(self, x, y):
        Background.__init__(self, x, y)
        self.SetImage('grass.png')

