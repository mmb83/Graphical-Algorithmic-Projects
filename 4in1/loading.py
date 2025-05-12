import pygame , sys , time
size = width , height = (500,500)
bgColor = (0,0,0)
lineColor = (255,255,255)
loadingBarColor = (0,179,0)
screen = pygame.display.set_mode(size)
textString = "Loading"
loadingNumber = "0.0 %"
white = (255,255,255)
red = (179,0,0)
addBar = 0
running = True
pygame.init()
def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or pygame.K_q:
                sys.exit() 
def printScreen():
    global addBar , textString , loadingNumber ,running
    checkEvents()
    screen.fill(bgColor)
    pygame.display.set_caption('Magic Square')
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(textString,True,red)
    loadingFont = pygame.font.Font("freesansbold.ttf",15)
    loading = loadingFont.render(loadingNumber,True,white)
    loadingRect = loading.get_rect()
    loadingRect.center = (250,415)
    
    screenRect = screen.get_rect()
    textRect = text.get_rect()
    textRect.center = (250,220)
    screen.blit(text,textRect)
    pygame.draw.line(screen,lineColor,(50,399),(450,399),1)
    pygame.draw.line(screen,lineColor,(50,430),(450,430),1)
    pygame.draw.line(screen,lineColor,(49,399),(49,430),1)
    pygame.draw.line(screen,lineColor,(450,400),(450,430),1)
    loadingBar =  pygame.Rect(50,400,addBar,30)
    pygame.draw.rect(screen,loadingBarColor,loadingBar)
    screen.blit(loading,loadingRect)
    if(addBar <= 400):
        loadingNumber = str(round((addBar/399)*100)) + " %" 
        time.sleep(0.02)
        addBar += 1
        if(addBar % 18 == 0):
            textString = textString +" ."
        if(addBar % 90 == 0):
            textString = "Loading"
    else :
        running = False
        time.sleep(2)
    
    pygame.display.flip()
while(running):
    printScreen()
pygame.quit()