import pygame , sys ,os  , time
from tkinter import *
from itertools import permutations
board = []
allBoards = []
solutionNumber = 0
N = 0
const = 100
path = "image/Queen.png"

def  windowsForm():
    def setNumbersOfDisks():
            global N
            count = number.get()
            if(count == ""):
                window.quit()
            else :
                N = int(count)
            window.destroy()
    window = Tk()
    window.title("NQueen")
    window.geometry("300x200")
    window.resizable(height=False,width=False)
    lable = Label(window,text="Please Enter numbers of Queens \n  ( Number between [4,10] )",foreground="darkblue",font=("Tahoma",15))
    lable.place(x=5,y=5)
    number = Entry(window)
    number.place(x = 60,width=180 ,height=25 , y = 80)
    Button(text="OK",background="green",foreground="white",command=setNumbersOfDisks).place(x = 115,y=130,width=70,height=30)
    Label(text="Made By ( Mohammad Mahdi Babaei & Erfan KhosroBeygi ) ",fg="red",font=("Tahoma",8)).pack(side=BOTTOM)
    window.mainloop()

windowsForm()

def checkNumberOfQueens():
    global const
    if(N<=3):
        print("No solution")
        pygame.quit()
        sys.exit()
    elif(N == 10):
        const -= 20
    elif(N > 10):
        print("Please Enter Number between [4,10]",tag="Failure",tag_color="red",color='white') 
        sys.exit()

checkNumberOfQueens()

pygame.init()

size = width,height = ((const) * N , (const) * N)
screen = pygame.display.set_mode(size)
bgColor = (100,100,100)
lineColor = (72,36,10)

boardSquareWidth = boardSquareHeight = (width  - 100) / N 

def setQueenImage():
    global queenImage 
    queenImage = pygame.image.load(path)
    queenImage = pygame.transform.scale(queenImage,(boardSquareWidth,boardSquareHeight))
def setChessBoard():
    global chessBoard , solutionNumber
    chessBoard=[]
    left =  50
    top = 50
    for i in range(N):
            chessBoard.append([])
            for j in range(N):
                chessBoard[i].append(pygame.Rect(left,top,boardSquareWidth,boardSquareHeight))
                if((i+j) % 2 == 0):
                    pygame.draw.rect(screen,(255,255,255),chessBoard[i][j],0)
                else :
                    pygame.draw.rect(screen,(0,0,0),chessBoard[i][j],0)
                if(allBoards[solutionNumber][i][j] == '1'):
                    global queenImage
                    queenImageRect = queenImage.get_rect()
                    chessBoardRect = chessBoard[i][j].midbottom
                    queenImageRect.midbottom = chessBoardRect
                    screen.blit(queenImage,queenImageRect)
                left += boardSquareWidth
            left = 50
            top += boardSquareHeight
    topLine = 47
    leftLine = 50
    for _ in range(2):
            pygame.draw.line(screen,lineColor,(left-1,topLine),(width-left-1,topLine),6)
            topLine = 46
            pygame.draw.line(screen,lineColor,(leftLine,topLine-1),(leftLine,height-47),6)
            topLine = height - 50 
            leftLine = (boardSquareWidth * N) + 50
    font = pygame.font.Font("freesansbold.ttf", 25)
    text = font.render( str(solutionNumber + 1) + "/" + str(len(allBoards)) ,True,(200,200,200))
    screenRect = screen.get_rect()
    textRect = text.get_rect()
    textRect.midbottom = screenRect.midbottom
    screen.blit(text,textRect)
def nQueen(): 
    def isSafe(perm):
        for i in range(len(perm)):
            for j in range(i + 1, len(perm)):
                if abs(i - j) == abs(perm[i] - perm[j]):
                    return False
        return True

    def solveQueens(n):
        global board
    for perm in permutations(range(N)):
        if isSafe(perm):
            for row in range(N):
                line = ['0'] * N
                line[perm[row]] = '1'
                board.append(line)
            allBoards.append(board.copy())
            board.clear()
    if(len(allBoards) == 0):
        print("No solution exists.")
    solveQueens(N)


def checkEvents():
    global solutionNumber
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if(solutionNumber == 0  ):
                    solutionNumber = len(allBoards) - 1
                else:
                    solutionNumber -= 1
            if event.key == pygame.K_RIGHT:
                if(solutionNumber == len(allBoards) - 1  ):
                    solutionNumber = 0 
                else :
                    solutionNumber += 1
def printScreen():
        checkEvents()
        
        screen.fill(bgColor)
        setChessBoard()
        pygame.display.set_caption("N Queen")
        pygame_icon = pygame.image.load(path)
        pygame.display.set_icon(pygame_icon)
        pygame.display.flip()
if __name__ == "__main__":
    nQueen()
    setQueenImage()
    while(True):
        printScreen()
pygame.quit()