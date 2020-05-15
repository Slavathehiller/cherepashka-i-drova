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

options = SimpleOptions()

VisualMap = None

turtle = None
mapper = None

turtleImage = None
moleImage = None
woodImage = None
obstacleImage = None
beaverImage = None

def menuAbout():
    global turtleImage
    aboutWindow = Toplevel()
    aboutWindow.geometry('460x180')
    aboutWindow.title('О программе')
    aboutWindow.iconbitmap('turtle.ico')

    TopLabel = Label(aboutWindow, text="Черепашка и дрова")
    TopLabel.pack(anchor=N)
    turtleFrame = Frame(aboutWindow)
    turtleFrame.pack(anchor=W)
    image = Image.open('turtle.ico')
    turtleImage = ImageTk.PhotoImage(image)
    turtleLabel = Label(turtleFrame)
    turtleLabel.config(image=turtleImage)
    turtleLabel.pack(anchor=W, side=LEFT)
    creators = "Разработчики: Папа, Паша\nАктер озвучки: Мама\nИгра разработана в программе Microsoft Visual Studio\nНа версии Python 3.7\nCopyright © Python Projects 2019-2020"
    creatorsLabel = Label(turtleFrame, text=creators, justify=LEFT)
    creatorsLabel.pack(side=LEFT)
    Closebutton = Button(aboutWindow, text="Закрыть", height=1, width=6)
    Closebutton.bind("<Button-1>", lambda event: aboutWindow.destroy())
    Closebutton.pack() 


def menuInstruction():
    global turtleImage
    global moleImage
    global woodImage
    global obstacleImage
    global beaverImage

    helpWindow = Toplevel()
    helpWindow.geometry('450x385')
    helpWindow.title('Инструкция')
    helpWindow.iconbitmap('turtle.ico')
    welcomeLabel = Label(helpWindow, text="Добро пожаловать в Черепашка и дрова")
    welcomeLabel.pack(anchor=W)

    help = "Цель игры  - построить домик черепашке.\nДля этого нужно собирать бревна находящиеся на карте.\nВсего для постройки домика вам понадобится 3 связки бревен.\nИ стоит учесть что, черепашка за раз может унести всего одну свзяку."
    goalLabel = Label(helpWindow, text=help, justify=LEFT)
    goalLabel.pack(anchor=W)
    image = Image.open('turtle.png').convert('RGBA')
    turtleImage = ImageTk.PhotoImage(image)
    turtleFrame = Frame(helpWindow)
    turtleFrame.pack(anchor=W)

    turtleLabel = Label(turtleFrame)
    turtleLabel.config(image=turtleImage)
    turtleLabel.pack(anchor=W, side=LEFT)

    turtleAbout = "- Черепашка, которой ты будешь управлять в процессе игры."
    turtleAboutLabel = Label(turtleFrame, text=turtleAbout, padx="20")
    turtleAboutLabel.pack(side=LEFT)

    krotImage = Image.open('krot.png').convert('RGBA')
    moleImage = ImageTk.PhotoImage(krotImage)
    moleFrame = Frame(helpWindow)
    moleFrame.pack(anchor=W)

    moleLabel = Label(moleFrame)
    moleLabel.config(image=moleImage)
    moleLabel.pack(anchor=W, side=LEFT)

    moleAbout = "- Саблезубый крот, он тебе так просто построить дом не даст,\nон будет тебя искать но он слеп.\nГлавное успевай убегать, а то нюх у него неплохо развит!"
    moleAboutLabel = Label(moleFrame, text=moleAbout, justify=LEFT, padx="10")
    moleAboutLabel.pack(side=LEFT)

    boberImage = Image.open('bober.png').convert('RGBA')
    beaverImage = ImageTk.PhotoImage(boberImage)
    beaverFrame = Frame(helpWindow)
    beaverFrame.pack(anchor=W)

    beaverLabel = Label(beaverFrame)
    beaverLabel.config(image=beaverImage)
    beaverLabel.pack(anchor=W, side=LEFT)

    beaverAbout = "- Трусливый бобер, начинает убегать при твоем приближении.\nНаткнувшись на дерево, бобер его уничтожает,\nпосле чего появятся связка бревен."
    beaverAboutLabel = Label(beaverFrame, text=beaverAbout, justify=LEFT, padx="10")
    beaverAboutLabel.pack(side=LEFT)

    brevnaImage = Image.open('wood.png').convert('RGBA')
    woodImage = ImageTk.PhotoImage(brevnaImage)
    woodFrame = Frame(helpWindow)
    woodFrame.pack(anchor=W)

    woodLabel = Label(woodFrame)
    woodLabel.config(image=woodImage)
    woodLabel.pack(anchor=W, side=LEFT)

    woodAbout = "- Связка бревен, материал для постройки дома."
    woodAboutLabel = Label(woodFrame, text=woodAbout, justify=LEFT, padx="10")
    woodAboutLabel.pack(side=LEFT)

    OImage = Image.open('tree.png').convert('RGBA')
    obstacleImage = ImageTk.PhotoImage(OImage)
    obstacleFrame = Frame(helpWindow)
    obstacleFrame.pack(anchor=W)

    obstacleLabel = Label(obstacleFrame)
    obstacleLabel.config(image=obstacleImage)
    obstacleLabel.pack(anchor=W, side=LEFT)

    obstacleAbout = "- Препятствие в виде дерева, непроходимое для всех, кроме бобра."
    obstacleAboutLabel = Label(obstacleFrame, text=obstacleAbout, justify=LEFT, padx="10")
    obstacleAboutLabel.pack(side=LEFT)

    Closebutton = Button(helpWindow, text="Закрыть", height=1, width=6)
    Closebutton.bind("<Button-1>", lambda event: helpWindow.destroy())
    Closebutton.pack() 

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
    OptionsWindow.iconbitmap('turtle.ico')

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

menuFile = Menu(mainmenu, tearoff=0)
menuFile.add_command(label="Выход", command=lambda: exit(0))
mainmenu.add_cascade(label="Файл", menu=menuFile)

menuGame = Menu(mainmenu, tearoff=0)
menuGame.add_command(label="Начать игру", command=Newgame)
menuGame.add_command(label="Настройки", command=SetOptions)
mainmenu.add_cascade(label="Игра", menu=menuGame)

menuHelp = Menu(mainmenu, tearoff=0)
menuHelp.add_command(label="О программе", command=menuAbout)
menuHelp.add_command(label="Инструкция", command=menuInstruction)
mainmenu.add_cascade(label="Помощь", menu=menuHelp)


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