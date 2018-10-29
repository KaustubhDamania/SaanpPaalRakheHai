import pygame,sys,random
from pygame.locals import *
import time
import random
def move_food(x,y,a,b): #moves food from x,y to a,b
    pygame.draw.rect(gameDisplay,black,(x,y,blockSize,blockSize))
    pygame.draw.rect(gameDisplay,red,(a,b,blockSize,blockSize))

def snake(blockSize,snakeHead):
    pygame.draw.rect(gameDisplay, white, (snakeHead[0],snakeHead[1],blockSize,snakeLength))

w_width = 800
w_height = 600
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
FPS=3
blockSize=10
init_x = random.randint(0,w_height)
init_y = random.randint(0,w_width)
snakeList=[]
snakeLength=10
snakeHead = [0,0] #snakehead starting coordinate, update this




pygame.init()
gameDisplay = pygame.display.set_mode((w_width,w_height))
check=True
clock = pygame.time.Clock()
#event=[pygame.K_DOWN]
#for _ in range(1):

downarrow= False
leftarrow= False
rightarrow= False
uparrow= False
new_x = random.randrange(0,w_width,10)
new_y = random.randrange(0,w_height,10)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type==pygame.KEYDOWN:
            downarrow= event.key== pygame.K_DOWN
            leftarrow= event.key== pygame.K_LEFT
            rightarrow= event.key==pygame.K_RIGHT
            uparrow= event.key==pygame.K_UP

    if downarrow and snakeHead[1] < w_height:
        snakeHead[1]+=blockSize
    elif uparrow and snakeHead[1] > 0:
        snakeHead[1]-=blockSize
    elif leftarrow and snakeHead[0] > 0:
        snakeHead[0]-=blockSize
    elif rightarrow and snakeHead[0] < w_width:
        snakeHead[0]+=blockSize


    gameDisplay.fill((0,0,0))
    pygame.draw.rect(gameDisplay,red,(new_x,new_y,blockSize,blockSize))
    #update check when snake head coordinate = init_x,init_y
    check = snakeHead == [new_x, new_y]
    print(check)
    print()

    if check:
        move_food(init_x,init_y,new_x,new_y)
        init_x, init_y = new_x, new_y
        snakeLength+=10
        new_x = random.randrange(0,w_width,10)
        new_y = random.randrange(0,w_height,10)

    snake(blockSize,snakeHead)

    pygame.display.update()
    clock.tick(FPS)
