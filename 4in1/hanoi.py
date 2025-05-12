import pygame,sys,time
from tkinter import *

step = 0
textString = "Step: " + str(step)
black = (0,0,0)
numberOfDisks = 0
disksColors = ((230, 25, 75),(60, 180, 75),(255, 225, 25),(67, 99, 216),(245, 130, 49),(145, 30, 180),(70, 240, 240),(240, 50, 230),(188, 246, 12),(250, 190, 190),
               (0, 128, 128),(230, 190, 255),(154, 99, 36),(255, 250, 200),(128, 0, 0),(170, 255, 195),(128, 128, 0),(255, 216, 177),(0, 0, 117),(128, 128, 128))
def windowsFormError():
    window = Tk()
    window.title("Error")
    window.geometry("300x100")
    Label(text="Please enter the number less than 17",fg="red",font=("tahoma",12)).place(x=20,y=30)
    window.mainloop()
def windowsForm():
    def setNumbersOfDisks():
            global numberOfDisks,disksColor
            numberOfDisks = int(number.get())
            window.destroy()
    window = Tk()
    window.title("Hanoi Towers")
    window.geometry("300x200")
    window.resizable(height=False,width=False)
    lable = Label(window,text="Please Enter numbers of Towers",foreground="darkblue",font=("Tahoma",15))
    lable.place(x=5,y=5)
    number = Entry(window)
    number.place(x = 60,width=180 ,height=25 , y = 50)
    Button(text="OK",background="green",foreground="white",command=setNumbersOfDisks).place(x = 115,y=100,width=70,height=30)
    Label(text="Made By ( Mohammad Mahdi Babaei & Erfan KhosroBeygi ) ",fg="red",font=("Tahoma",8)).pack(side=BOTTOM)
    window.mainloop()

windowsForm()   

pygame.init()

def checkNumberOfDisks():
    if(numberOfDisks > 16) :
            windowsFormError()
            sys.exit()
checkNumberOfDisks()

size = width,height = (600,500)

#jungle = pygame.image.load("image/jungle.jpg")

bg_color = (200,200,200)

verticalBarColor = (150,75,0)
horizontalBarColor = (0,0,0)

# clock = pygame.time.Clock()

# FREQ = 1100

"""bars for 4 bars"""
bars=[0,0,0,0]

bars[3] = pygame.Rect(5,height-25,width-10,15)
for i in range(0,3):
    bars[i] = pygame.Rect(width / 3 * (i + 1) - 100, 100 , 10, bars[3].top - 100)
"""moves for tower moves"""
moves = []

disksInBars = [[],[],[]]


distanceOfDisks = 0
horizontalDiskHeight = disksHeight = 15
distanceOfVerticalBars = 125

top = bars[3].top - distanceOfDisks


diskWidth = 175

reduceDiskwidth = 25

while diskWidth / numberOfDisks <= reduceDiskwidth :
    reduceDiskwidth = reduceDiskwidth - 1

for i in range(numberOfDisks):
    disksInBars[0].append(pygame.Rect(bars[0].centerx - diskWidth / 2 ,top - horizontalDiskHeight ,diskWidth , disksHeight ))
    top = top - disksHeight - distanceOfDisks
    diskWidth = diskWidth - reduceDiskwidth
screen = pygame.display.set_mode((width,height))

def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def printScreen(): 
        global textString
        checkEvents()
        
        time.sleep(0.001)
        screen.fill(bg_color)

        stepFont = pygame.font.Font("freesansbold.ttf",32)
        Step = stepFont.render(textString,True,(255,0,0))
        stepRect = Step.get_rect()
        screenRect = screen.get_rect()
        stepRect.center = (width//2,25)
        screen.blit(Step,stepRect)
        
        pygame.display.set_caption("Tower of Hanoi")
        pygame.draw.rect(screen,verticalBarColor ,bars[3] , 0,border_top_left_radius=10,border_top_right_radius=10,border_bottom_left_radius=10,border_bottom_right_radius=10)
        for i in range(0,3):
            pygame.draw.rect(screen,horizontalBarColor,bars[i],0,border_top_left_radius=5,border_top_right_radius=5)
        for i in range(len(disksInBars)) :
            for j in range(len(disksInBars[i])) :
                disk = disksInBars[i][j].width//reduceDiskwidth 
                pygame.draw.rect(screen, disksColors[disk], disksInBars[i][j], 0,border_top_left_radius=10,border_top_right_radius=10,border_bottom_left_radius=10,border_bottom_right_radius=10)
                
        pygame.display.flip()

def move():
    global step , textString
    for i in range(len(moves)):
        start = moves[i][0]
        end = moves[i][1]

        if(len(disksInBars[end])!=0):
             endY = disksInBars[end][-1].top - 9
        else : 
             endY = bars[3].top - 9
        if(len(disksInBars[start]) != 0):    
            while (disksInBars[start][-1].top > bars[start].top - 30):
                disksInBars[start][-1].top -= 1
                printScreen()
            if(disksInBars[start][-1].centerx < bars[end].centerx):
                while(disksInBars[start][-1].centerx < bars[end].centerx):
                    disksInBars[start][-1].left += 1 
                    printScreen()
            else :
                while(disksInBars[start][-1].centerx > bars[end].centerx):
                    disksInBars[start][-1].left -= 1 
                    printScreen()
            while(disksInBars[start][-1].centery <= endY):
                disksInBars[start][-1].centery += 1
                printScreen()      
            step += 1
            textString = "Step: " + str(step)
            
            disksInBars[end].append(disksInBars[start][-1])
            disksInBars[start].pop()
def hanoi(n,A,B,C):
    if(n==1):
        moves.append([A,C])
    else :
        hanoi(n-1,A,C,B)
        moves.append([A,C])
        hanoi(n-1,B,A,C)

if __name__ == "__main__":
    hanoi(numberOfDisks,0,1,2)
    move()
    while(True):
        printScreen()
pygame.quit()