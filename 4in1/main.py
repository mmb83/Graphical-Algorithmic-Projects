import pygame ,sys , os
from pygame.locals import *

os.system("python loading.py")
pygame.init()
bgColor = (255,100,0)
size = width,heigth = (500,500)
screen = pygame.display.set_mode(size)
font = pygame.font.Font("freesansbold.ttf", 25)
textFont = pygame.font.Font(None,46)
path = "image/im.jpg"
textsColor = (0,0,0)
textsChooseColor = (255,255,255)

click_sound = pygame.mixer.Sound("sound/sound2.wav")  

bg = pygame.image.load(path)
bg = pygame.transform.scale(bg,size)


choiseText = textFont.render("Choose one of these options", True, (104, 210, 255))
choiseTextRect = choiseText.get_rect(center=(width // 2 , 45))

hanoiText = font.render("Hanoi Tower", True, textsColor)
hanoiTextRect = hanoiText.get_rect(center=( width // 2, 120))

nQueenText = font.render("N Queen", True, textsColor)
nQueenTextRect = hanoiText.get_rect(center=( width // 2 +22,180))

sudokuText = font.render("Sudoku ", True, textsColor)
sudokuTextRect = sudokuText.get_rect(center=( width // 2,240))

magicalSquareText = font.render("Magical Square", True, textsColor)
magicalSquareTextRect = magicalSquareText.get_rect(center=( width //2,300))  

makerFont = pygame.font.Font(None,25)
makerText = makerFont.render("Made by Mohammad Mahdi Babaei and Erfan Khosrobeigy", True, (255,255,100))
makerTextRect = makerText.get_rect(center=(width //2 ,heigth - 35))  
def checkEvents():
    global hanoiText , nQueenText , sudokuText,magicalSquareText , choosed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            if hanoiTextRect.collidepoint(event.pos):
                click_sound.play()
                os.system("python hanoi.py")

            elif nQueenTextRect.collidepoint(event.pos):
                click_sound.play()
                os.system("python NQueen.py")
            
            elif sudokuTextRect.collidepoint(event.pos):
                click_sound.play()
                os.system("python sudoku.py")
            
            elif magicalSquareTextRect.collidepoint(event.pos):
                click_sound.play()
                os.system("python magicalSquare.py")

        elif event.type == MOUSEMOTION:
            if hanoiTextRect.collidepoint(event.pos):
                hanoiText = font.render("Hanoi Tower", True, textsChooseColor)
            else:
                hanoiText = font.render("Hanoi Tower", True, textsColor)

            if nQueenTextRect.collidepoint(event.pos):
                nQueenText = font.render("N Queen", True, textsChooseColor)
                
            else:
                nQueenText = font.render("N Queen", True, textsColor)

            if sudokuTextRect.collidepoint(event.pos):
                sudokuText = font.render("Sudoku", True, textsChooseColor)
            else:
                sudokuText = font.render("Sudoku", True, textsColor)
            if magicalSquareTextRect.collidepoint(event.pos):
                magicalSquareText = font.render("Magical Square", True,textsChooseColor)
                
            else:
                magicalSquareText = font.render("Magical Square", True, textsColor)
def printScreen():
    
    checkEvents()
    screen.fill(bgColor)
    bgRect = bg.get_rect()
    screenRect = screen.get_rect()
    bgRect.center = screenRect.center
    screen.blit(bg,bgRect)
    screen.blit(choiseText,choiseTextRect)
    screen.blit(hanoiText,hanoiTextRect)
    screen.blit(nQueenText,nQueenTextRect)
    screen.blit(sudokuText,sudokuTextRect)
    screen.blit(magicalSquareText,magicalSquareTextRect)
    screen.blit(makerText,makerTextRect)
    pygame.display.flip()


if __name__ == '__main__':
    while(True):
        printScreen()
    
pygame.quit()