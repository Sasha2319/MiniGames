from Sudoku import SudokuGame
import Sudoku
from tkinter import *
import random
from tkinter import messagebox as mb
from functions import *
from tkinter.ttk import *
from asadad import main, menu
import functions
import stars

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
    print('Test mode')

def sudokuStarter(e):
    print(functions.testMode)
    if functions.testMode == False:
        global levelChoose
        levelChoose = Toplevel()
        levelChoose.geometry('250x100')
        levelChoose.title('Level')
        levelChoose.resizable(False, False)
        center(levelChoose)

        Choose = Label(levelChoose, text='Select level', font='Arial 18')
        Choose.pack(pady=0)

        easyButton = Button(levelChoose, text='Easy')
        easyButton.bind('<Button-1>', easy)
        easyButton.pack(side='left', padx=5)

        normalButton = Button(levelChoose, text='Normal')
        normalButton.pack(side='left')
        normalButton.bind('<Button-1>', normal)

        hardButton = Button(levelChoose, text='Hard')
        hardButton.pack(side='left', padx=5)
        hardButton.bind('<Button-1>', hard)

    if functions.testMode == True:
        stars.stars = 3
        print('Test Game')
        main.destroy()
        SudokuGame()


main.title('MiniGames')
main.geometry('405x400')
main.resizable(False, False)
center(main)
main.tk.call('wm', 'iconphoto', main._w, PhotoImage(file=r'assets/img/games.png'))

frameTop = Frame(main)
frameTop.pack()

frameMenu = Frame(main)
frameMenu.pack(side='left')

labelGame_1 = Label(frameTop, justify='center', text='Mini Games', font='Courier 30 bold', foreground='#BB00B8')
labelGame_1.pack(pady=10)

labelGame_2 = Label(frameTop, justify='center', text='Choose the game', font='Courier 21 bold', foreground='#000')
labelGame_2.pack(side='top')

sudokuImg = PhotoImage(file= r'assets\img\sudoku.png')
sudokuImg = sudokuImg.subsample(2, 2)

sudokuButton = Button(frameMenu, image=sudokuImg)
sudokuButton.bind('<Button-1>', sudokuStarter)
sudokuButton.pack(anchor='nw')

testButton = Button(text='test')
testButton.bind('<Button-1>', testFunc)
testButton.pack(anchor='se', side='bottom')

menu()















