from Consts import*
from tkinter import*
from cherepashka import*
from mapper import*
from PIL import Image, ImageTk

window = Tk()
window.title("Черепашка и дрова")
window.geometry("800x600")
window.iconbitmap('turtle.ico')
mainmenu = Menu(window)
window.config(menu=mainmenu)
menuFile = Menu(mainmenu, tearoff=0)
menuFile.add_command(label="Выход", command=lambda: exit(0))

options = SimpleOptions()

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
            square = Label(frame, bd=0)
            square.pack(side=LEFT)
            Line.append(square)
        Map.append(Line)
    mapper.createNewMap()
    drawMap()

def OptionsOK(W, DLC, SMV):
    options.difficult = DLC.get()
    options.SlowMoles = SMV.get()
    W.destroy()

def SetOptions():
    OptionsWindow = Toplevel(window)
    OptionsWindow.geometry('300x180')
    OptionsWindow.title("Настройки игры")

    DifficultLevelChoise = IntVar()

    lbDifficultLevel = Label(OptionsWindow, text="Уровень сложности:", padx=15, pady=10)
    lbDifficultLevel.grid(row=0, column=0, sticky=W)

    rbEasy = Radiobutton(OptionsWindow, text="Легкий", value=Easy, variable=DifficultLevelChoise)
    rbNormal = Radiobutton(OptionsWindow, text="Нормальный", value=Normal, variable=DifficultLevelChoise)
    rbHard = Radiobutton(OptionsWindow, text="Сложный", value=Hard, variable=DifficultLevelChoise)

    DifficultLevelChoise.set(options.difficult)

    rbEasy.grid(row=1, column=0, sticky=W, padx=4, pady=2)
    rbNormal.grid(row=2, column=0, sticky=W, padx=4, pady=2)
    rbHard.grid(row=3, column=0, sticky=W, padx=4, pady=2)

    SlowMolesVar = IntVar()
    SlowMolesVar.set(options.SlowMoles)

    cbSlowMoles = Checkbutton(OptionsWindow, text="Медленные кроты", variable=SlowMolesVar)
    cbSlowMoles.grid(row=0, column=1, sticky=W, padx=4, pady=2)

    OKbutton = Button(OptionsWindow, text="Ok", height=1, width=6)
    OKbutton.grid(row=4, column=0, sticky=E, padx=30, pady=15)
    OKbutton.bind("<Button-1>", lambda event: OptionsOK(OptionsWindow, DifficultLevelChoise, SlowMolesVar))
    
    Cancelbutton = Button(OptionsWindow, text="Cancel", height=1, width=6)
    Cancelbutton.grid(row=4, column=1, padx=30, pady=15) 
    Cancelbutton.bind("<Button-1>", lambda event: OptionsWindow.destroy())

menuGame = Menu(mainmenu, tearoff=0)
menuGame.add_command(label="Начать игру", command=Newgame)
menuGame.add_command(label="Настройки", command=SetOptions)
mainmenu.add_cascade(label="Файл", menu=menuFile)
mainmenu.add_cascade(label="Игра", menu=menuGame)



winimage = ImageTk.PhotoImage(Image.open('win.png'))
loseimage = ImageTk.PhotoImage(Image.open('lose.png'))

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