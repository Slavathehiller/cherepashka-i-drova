from tkinter import*
from cherepashka import*
from mapper import*
from PIL import Image, ImageTk

window = Tk()
window.title("Черепашка и дрова")
window.geometry("800x600")
mainmenu = Menu(window)
window.config(menu=mainmenu)
menuFile = Menu(mainmenu, tearoff=0)
menuFile.add_command(label="Выход", command=lambda: exit(0))

options = SimpleOptions()

image = Image.open('grass.gif')
grassImage = ImageTk.PhotoImage(image)

VisualMap = None

turtle = None
mapper = None

def Newgame():
    global gameEnded, Map, VisualMap, turtle, mapper
    gameEnded = False
    Map = []

    turtle = Turtle(None)
    mapper = MapManager(turtle, options)
    turtle.map = mapper

    if VisualMap != None:
        VisualMap.destroy()

    VisualMap = Frame(window)
    VisualMap.pack(fill=BOTH)

    for i in range(options.sizeY):
        Line = list()
        frame = Frame(VisualMap)
        frame.pack(side=TOP)
        for j in range(options.sizeX):
            square = Label(frame)
            square.pack(side=LEFT)
            Line.append(square)
        Map.append(Line)
    mapper.createNewMap()
    drawMap()

menuGame = Menu(mainmenu, tearoff=0)
menuGame.add_command(label="Начать игру", command=Newgame)
mainmenu.add_cascade(label="Файл", menu=menuFile)
mainmenu.add_cascade(label="Игра", menu=menuGame)

winimage = ImageTk.PhotoImage(Image.open('win.gif'))
loseimage = ImageTk.PhotoImage(Image.open('lose.gif'))

gameEnded = False

def WinGame():
    global gameEnded
    gameEnded = True
    winGameWindow = Toplevel()
    winGameWindow.title("Победа")
    winGameWindow.geometry("300x280")
    winGameLabel = Label(winGameWindow, text="Вы победили!\nПройдено шагов: " + str(turtle.step))
    winGameLabel.pack()

    winGameLabelGraphic = Label(winGameWindow)
    winGameLabelGraphic.config(image=winimage)
    winGameLabelGraphic.pack()

    CloseButton = Button(winGameWindow, text="Закрыть")
    CloseButton.bind("<Button-1>", lambda event: winGameWindow.destroy())
    CloseButton.pack()
    winsound.PlaySound("yraa.wav", winsound.SND_ASYNC + winsound.SND_PURGE)

def LoseGame():
    global gameEnded
    gameEnded = True
    loseGameWindow = Toplevel()
    loseGameWindow.title("Поражение")
    loseGameWindow.geometry("300x300")
    loseGameLabel = Label(loseGameWindow, text="Вы проиграли\nПройдено шагов: " + str(turtle.step))
    loseGameLabel.pack()
    loseGameLabelGraphic = Label(loseGameWindow)
    loseGameLabelGraphic.config(image=loseimage)
    loseGameLabelGraphic.pack()
    CloseButton = Button(loseGameWindow, text="Закрыть")
    CloseButton.bind("<Button-1>", lambda event: loseGameWindow.destroy())
    CloseButton.pack()
    winsound.PlaySound("aiaiai.wav", winsound.SND_ASYNC + winsound.SND_PURGE)


def CheckGameState(state):
    if state == WIN:
        WinGame()
    elif state == LOSE:
        LoseGame()



def placeObject(x, y, object):
    if object == None:
        nowimage = grassImage
    else:
        nowimage = object.GetCurrentImage()

    Map[y][x].config(image=nowimage)


def drawMap():
    for x in range(options.sizeX):
        for y in range(options.sizeY):
            placeObject(x, y, mapper.GetObject(x, y))


def TurtleMove(direction):
    turtle.move(direction)
    CheckGameState(turtle.checkAndEat())


def KeyPress(event):
    if gameEnded:
        return
    if event.keycode == 38:
        TurtleMove(Up)
    elif event.keycode == 37:
        TurtleMove(Left)
    elif event.keycode == 40:
        TurtleMove(Down)
    elif event.keycode == 39:
        TurtleMove(Right)
    if not gameEnded:
        CheckGameState(mapper.tic())
    drawMap() 


window.bind("<Key>", KeyPress)

window.mainloop()