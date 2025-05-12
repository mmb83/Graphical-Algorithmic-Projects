import time,os,ast
from tkinter import *
N = 9 
board = []
solved = False
sample = []
tripleBoard = [[[] for _ in range(3)]for _ in range(3) ]  
def windowsForm():
    def setSudoku():
        global board
        iniList = sudoku.get()
        sudokuBoard = ast.literal_eval(iniList)
        for i in range(N):
            board.append([])
            for j in range(N):
                    board[i].append(sudokuBoard[i][j])
        print(board)
        window.destroy()
    window = Tk()
    window.title("Sudoku")
    window.geometry("300x150")
    window.resizable(height=False,width=False)
    lable = Label(window,text="Please Enter your Sudoku",foreground="darkblue",font=("Tahoma",18))
    lable.place(x=10,y=10)
    sudoku = Entry(window)
    sudoku.place(height=25,width=200,x=50,y=55)
    Button(text="Set",background="gray",foreground="white",command=setSudoku).place(width=50,height=35,x=120,y=90)
    Label(text="Made By ( Mohammad Mahdi Babaei & Erfan KhosroBeygi ) ",fg="red",font=("Tahoma",8)).pack(side=BOTTOM)
    window.mainloop()
def secondForm():
    def solve():
        global solved
        solved = True
        window.destroy()
    window = Tk()
    window.title("Sudoku")
    window.geometry("300x120")
    window.resizable(height=False,width=False)
    lable = Label(window,text="Click to solve your Sudoku",foreground="darkblue",font=("Tahoma",18))
    lable.place(x=10,y=10)
    Button(text="Solve",font=("tahoma",10),background="green",foreground="white",command=solve).place(width=50,height=35,x=130,y=60)
    Label(text="Made By ( Mohammad Mahdi Babaei & Erfan KhosroBeygi ) ",fg="red",font=("Tahoma",8)).pack(side=BOTTOM)
    window.mainloop()
def checkTriplesBoard():
    count = 0
    for i in range(3):
        for j in range(3):
            mySet = set(tripleBoard[i][j])
            if(len(mySet)==len(tripleBoard[i][j])):
                count += 1
    if(count==9):
        return True
    return False
def checkOneTripleBoard(row,col):
    tripleSet = set(tripleBoard[row][col])
    if(len(tripleSet) == len(tripleBoard[row][col])):
        return True
    return False   
def setOneTripleBoard(row,col):
    tripleBoard[row][col].clear()
    for i in range(N):
        for j in range(N):
            if(board[i][j]!="."):
                if(row == i // 3 and col == j // 3):
                    tripleBoard[row][col].append(board[i][j])
def setTripleBoard():
    tripleBoard = [[[] for _ in range(3)]for _ in range(3) ] 
    for i in range(N):
        for j in range(N):
            if(board[i][j]!="."):
                row = i // 3 
                col = j // 3
                tripleBoard[row][col].append(board[i][j])
def setBoard():
    for i in range(N):
        for j in range(N):
            if(board[i][j]!="."):
                number = int(str(board[i][j]))
                board[i][j] = number 
def printBoard():
    for i in range(N):
        print("| ",end="")
        for j in range(N):
            if(j%3==2 ):
                str = " | "
            else :
                str = " "
            print(board[i][j],end=str)
        if(i%3==2):
            print()
        print()
def isSafe(row,col,value):
    tripleRow = row // 3
    tripleCol = col // 3
    setOneTripleBoard(tripleRow ,tripleCol)
    for i in range(N):
        if(board[row][i] == value or board[i][col] == value):
            return False
    if(not checkOneTripleBoard(tripleRow,tripleCol)):
        return False
    return True

def solveSudoku():
    for row in range (N):
        for col in range(N):
            if(board[row][col] == "."):
                for value in range(1,10):
                    if(isSafe(row,col,value)):
                        board[row][col] = value
                        if(solveSudoku()):
                            return True
                    board[row][col] = "."
                return  False
    return True
                
def isUserSudokuValid():
    setTripleBoard()
    if(not checkTriplesBoard()):
        return False
    horizontalList = []
    verticalList = []
    for i in range(N):
        for j in range(N):
            if(board[i][j]!= "."):
                horizontalList.append(board[i][j])
            if(board[j][i] != "."):
                verticalList.append(board[j][i])
        horizontalSet = set(horizontalList)
        verticalSet = set(verticalList)
        if(len(horizontalSet)==len(horizontalList) and len(verticalSet)==len(verticalList)):
            pass
        else:
            return False
        horizontalList.clear()
        verticalList.clear()  
    return True  
def run():
    setBoard()
    if(isUserSudokuValid()):
        solveSudoku()
        return
    print("Sudoku is invalid")
def getBoard():
    return board
def isSolved():
    return solved
