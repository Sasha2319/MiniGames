from tkinter import *
from tkinter import messagebox as mb
import random
from functions import *
import functions
from asadad import menu
import stars
import keyboard
import tkinter

def print_pressed_keys(e):
    print(e, e.event_type, e.name)


def windowEntry():
    global root2
    root2 = Toplevel()
    root2.geometry('250x100')
    root2.title('Enter')
    root2.resizable(False, False)
    center(root2)

    numLabel = Label(root2, text='Enter the number', font='Arial 18')
    numLabel.pack()

    global numEntry
    numEntry = Entry(root2, width=40, takefocus=1)
    numEntry.pack()
    numEntry.focus()

    numButton = Button(root2, text='OK', width=5, command=ret)
    numButton.pack()



def ret():
    try:
        if type(int(numEntry.get())) == int and len(numEntry.get()) == 1 and numEntry.get()[0] != '0':
            print("Hello world!")

            index = [int(str(w)[3]), int(str(w)[6])]

            vars[index[0]][index[1]].set(int(numEntry.get()))
            sudoku[index[0]][index[1]] = int(numEntry.get())
            print(sudoku)

            w.config(textvariable=vars[index[0]][index[1]])
            root2.destroy()
    # except ValueError:
    #     print('Это не число, выходим)')
    #     print(ValueError)
    except TclError:
        print('что это еще такое?')



def click(e):
    global w
    w = e.widget
    windowEntry()
    print(w)
    w.config(background='#FFFF9D')
    keyboard.add_hotkey('Enter', ret)

def check(e):
    if sudoku == SudokuToCheck:
        print('True')
        mb.showinfo('You are winner!!!', 'You are winner!!!')
        functions.testMode = False
        stars.stars = 0
        delButtons()
        root.destroy()
        menuf(e)
    else:
        functions.testMode = False
        print('False')
        mb.showinfo('try again', 'Try again!')

def menuStarter(e):
    stars.stars = 0
    root.destroy()
    menuf(e)

gamelist = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

def delButtons():
    for i in range(9):
        for j in range(9):
            gamelist[i][j].grid_forget()


SudokuToCheck = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]



vars = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
r1 = 1
r2 = 2
stars.stars = 5

def SudokuGame():
    print('hello world')
    print(stars.stars)

    # set sudoku to SudokuToCheck
    for i in range(9):
        for j in range(9):
            sudoku[i][j] = SudokuToCheck[i][j]
    # set * for 0
    for i in range(stars.stars):
        r1=round(random.random()*9)-1
        r2=round(random.random()*9)-1
        sudoku[r1][r2] = 0

    global root
    root = Tk()
    root.geometry("405x400")
    root.resizable(False, False)
    root.title('Sudoku')
    center(root)
    root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file=r'assets/img/sudoku.png'))

    print(stars.stars)
    for i in range(9):
        for j in range(9):

            if sudoku[i][j] == 0:
                gamelist[i][j] = Button(root, text=f'*', width=5, height=2, background='#D7FFFC', activebackground='#0076FF', name=f'*[{i}][{j}]')
                gamelist[i][j].bind('<Button-1>', click)
                gamelist[i][j].grid(row=i, column=j)
            else:
                gamelist[i][j] = Button(root, text=f'{sudoku[i][j]}', width=5, height=2, name=f'[{i}][{j}]', activebackground='#F97B6E')
                gamelist[i][j].grid(row=i, column=j)
                gamelist[i][j]['state'] = 'disabled'

    global homeImg
    homeImg = tkinter.PhotoImage(file=r'assets/img/home.png').subsample(20, 20)


    global homeButton
    homeButton = Button(root, image=homeImg)
    homeButton.bind('<Button-1>', menuStarter)
    homeButton.place(x=1, y=370)

    global checkButton
    checkButton = Button(root, text="Check", width=10, background='#F97B6E')
    checkButton.bind('<Button-1>', check)
    checkButton.place(x=160, y=371)


    for i in range(9):
        for j in range(9):
            vars[i][j] = IntVar()
    print(vars)

    print(gamelist)
    root.mainloop()


#
#
#
#
#
'''The END of SudokuGame code'''
#
#
#
#
#





print('Menu')



#
#
#
#
#
'''The start of the menu cod'''
#
#
#
#
#

def menuf(e):
    functions.testMode = False
    global main
    main = Tk()
    main.title('MiniGames')
    main.geometry('405x400')
    main.resizable(False, False)
    center(main)

    global frameTop
    global frameMenu
    global labelGame_1
    global labelGame_2
    global sudokuImg
    global sudokuButton
    global testButton

    frameTop = Frame(main)
    frameTop.pack()

    frameMenu = Frame(main)
    frameMenu.pack(side='left')

    labelGame_1 = Label(frameTop, justify='center', text='Mini Games', font='Courier 30 bold', foreground='#BB00B8')
    labelGame_1.pack(pady=10)

    labelGame_2 = Label(frameTop, justify='center', text='Choose the game', font='Courier 21 bold', foreground='#000')
    labelGame_2.pack(side='top')

    sudokuImg = PhotoImage(file=r'assets\img\sudoku.png')
    sudokuImg = sudokuImg.subsample(2, 2)

    sudokuButton = Button(frameMenu, image=sudokuImg)
    sudokuButton.bind('<Button-1>', sudokuStarter)
    sudokuButton.pack(anchor='nw')

    testButton = Button(text='test', width=10)
    testButton.bind('<Button-1>', testFunc)
    testButton.pack(anchor='se', side='bottom')

    menu()





def sudokuStarter(e):
    print(functions.testMode)
    if functions.testMode == False:
        print('test mode is False')
        global levelChoose
        global Choose
        global easyButton
        global normalButton
        global hardButton
        levelChoose = Toplevel()
        levelChoose.geometry('250x100')
        levelChoose.title('Level')
        levelChoose.resizable(False, False)
        center(levelChoose)

        Choose = Label(levelChoose, text='Select level', font='Arial 18')
        Choose.pack(pady=0)

        easyButton = Button(levelChoose, text='Easy', width=10)
        easyButton.bind('<Button-1>', easy)
        easyButton.pack(side='left', padx=5)

        normalButton = Button(levelChoose, text='Normal', width=10)
        normalButton.pack(side='left')
        normalButton.bind('<Button-1>', normal)

        hardButton = Button(levelChoose, text='Hard', width=10)
        hardButton.pack(side='left', padx=5)
        hardButton.bind('<Button-1>', hard)

    if functions.testMode == True:
        print('test mode is True')
        stars.stars = 3
        print('Test Game')
        main.destroy()
        SudokuGame()



def easy(e):
    stars.stars = functions.easy
    print('Easy Game')
    main.destroy()
    SudokuGame()


def normal(e):
    stars.stars = functions.normal
    print('Normal Game')
    main.destroy()
    SudokuGame()

def hard(e):
    stars.stars = functions.hard
    print('Hard Game')
    main.destroy()
    SudokuGame()

def testFunc(e):
    functions.testMode = True
    stars.stars = 3
    print('Test mode')


