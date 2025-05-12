import pygame , sys ,threading
from tkinter import *
from sudokuSolver import *
sudokuBoard = []
board = []
images = []
windowsForm()
def setBoard():
    for i in range(9):
        board.append([])
threeInThreeColors = [[(0,154,0),(107,182,255),(255,255,77)],[(255,125,21),(206,206,206),(100,100,255)],[(255,150,218),(250,250,250),(0,200,125)]]
size = width , height = (500,500)
screen = pygame.display.set_mode(size)
boarderWidth = boarderHeight = 50
bgColor = (100,100,100)

def checkEvents():
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            sys.exit()
def printScreen():
    checkEvents()
    left = 25
    top = 25
    screen.fill(bgColor)
    line = pygame.Rect(left-1,top-2,boarderWidth*9+2,2)
    pygame.draw.rect(screen,(0,0,0),line)
    line = pygame.Rect(left-2,top-2,2,boarderHeight*9+4)
    pygame.draw.rect(screen,(0,0,0),line)
    for i in range(9):
        for j in range(9):
            row = i // 3 
            col = j // 3
            board[i].append(pygame.Rect(left,top,boarderWidth,boarderHeight))
            pygame.draw.rect(screen,threeInThreeColors[row][col],board[i][j])
            if(j != 0 ):
                line = pygame.Rect(left,25,2,boarderHeight*9)
                pygame.draw.rect(screen,(70,70,70),line)
            if(i != 0):
                line = pygame.Rect(25,top-2,boarderWidth*9,2)
                pygame.draw.rect(screen,(70,70,70),line)
            left+=boarderWidth
        left = 25
        top += boarderHeight
    for i in range(9):
        for j in range(9):
            if(sudokuBoard[i][j] != '.'):
                number = int(sudokuBoard[i][j])
                numberImage = images[number - 1]
                numberImageRect = images[number - 1].get_rect()
                boardRect = board[i][j].center
                numberImageRect.center = boardRect
                screen.blit(numberImage,numberImageRect)

    line = pygame.Rect(left-1,top,boarderWidth*9+2,2)
    pygame.draw.rect(screen,(0,0,0),line)
    line = pygame.Rect(left+boarderWidth*9,23,2,boarderHeight*9+4)
    pygame.draw.rect(screen,(0,0,0),line)
    
    pygame.display.flip()
def setImage():
    for i in range(1,10):
        font = pygame.font.SysFont('Arial', 40)
        number = font.render(str(i), True, (0,0,0))
        images.append(number)

if __name__ == "__main__":
    once = True
    pygame.init()
    setBoard()
    setImage()
    while(True):
        sudokuBoard = getBoard()
        printScreen()
        if(once):
            secondForm()
            once = False
        if(isSolved()):
            run()
            solved = False
pygame.quit()