import pygame
import sys
from tkinter import *

def create_magic_square_odd(n):
    square = [[0] * n for _ in range(n)]

    num = 1
    i, j = 0, n // 2
    
    while num <= n**2:
        square[i][j] = num
        num += 1
        new_i, new_j = (i - 1) % n, (j + 1) % n
        if square[new_i][new_j]:
            i += 1
        else:
            i, j = new_i, new_j

    return square
def create_magic_square_even(n):
    min , max = 1 , n**2
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if(i==j):
                board[i][j] = max
            elif((i+j) == n-1):
                board[i][j] = max
            else:
                board[i][j] = min
            min += 1
            max -= 1
    return board
def print_magic_square(square):
    for row in square:
        print(' '.join(str(x).ljust(2) for x in row))

def create_window():
    window = Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    width =  (screen_width // 2 ) - 300
    heigth = (screen_height // 2) - 150
    def setSudoku():
        global N
        N = int(number.get())
        window.destroy()
    window.title("Magic Square")
    window.geometry(f"300x150+{width}+{heigth}")
    window.resizable(height=False,width=False)
    lable = Label(window,text="Please Enter the number",foreground="darkblue",font=("Tahoma",18))
    lable.place(x=10,y=10)
    number = Entry(window)
    number.place(height=25,width=200,x=50,y=55)
    Button(text="Set",background="green",foreground="white",command=setSudoku).place(width=50,height=35,x=120,y=90)
    Label(text="Made By ( Mohammad Mahdi Babaei & Erfan KhosroBeygi ) ",fg="red",font=("Tahoma",8)).pack(side=BOTTOM)
    window.mainloop()
create_window()

pygame.init()

cell_size = 100
if N <= 2:
    print("No solution")
    pygame.quit()
    sys.exit()
if N > 10:
    cell_size -= 25
if N > 13:
    cell_size -= 15
if N > 17 :
    print("Please Enter Number between [3,16]")
    sys.exit()
size = width, height = ((cell_size) * N, (cell_size) * N)
screen = pygame.display.set_mode(size)
bgColor = (64, 64, 64)

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

board_square_width = board_square_height = (width - 100) / N

def print_screen(square):
    check_events()
    screen.fill(bgColor)
    pygame.display.set_caption("Magic Square")
    left = 50
    top = 50
    for i in range(N):
        for j in range(N):
            rect = pygame.Rect(left, top, board_square_width, board_square_height)
            pygame.draw.rect(screen, (0, 0, 0), rect, 0)
            pygame.draw.rect(screen, (200, 0, 0), rect, 1)
            pygame.font.init()
            font = pygame.font.SysFont('Arial', 24)
            text_surface = font.render(str(square[i][j]), True, (255, 255, 255))
            textRect = text_surface.get_rect()
            textRect.center = rect.center
            screen.blit(text_surface, textRect)
            left += board_square_width
        left = 50
        top += board_square_height
    pygame.display.flip()

if __name__ == "__main__":
    if N % 2 :
        square = create_magic_square_odd(N)
    else:
        square = create_magic_square_even(N)
    
    while True:
        print_screen(square)
pygame.quit
