import pygame,sys,random,math
from pygame.locals import *
import time
import random
def move_food(x,y,a,b): #moves food from x,y to a,b
    pygame.draw.rect(gameDisplay,black,(x,y,blockSize,blockSize))
    pygame.draw.rect(gameDisplay,red,(a,b,blockSize,blockSize))
def snake_init(blockSize,snakeHead):
    pygame.draw.rect(gameDisplay, white, (snakeHead[0],snakeHead[1],blockSize,snakeLength))
def snake_run(blockSize,snakeList):
    for coordinate in snakeList:
        pygame.draw.rect(gameDisplay, white, (coordinate[0],coordinate[1],blockSize,blockSize))
def coordinate_update(snakeList):
    for i in range(len(snakeList)-1,0,-1):
        snakeList[i]=snakeList[i-1].copy()

w_width = 800
w_height = 600
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
FPS=30
blockSize=10
init_x = math.floor(144/10)*10 #random.randint(0,w_height)
init_y = math.floor(133/10)*10 #random.randint(0,w_width)
snakeList=[]
snakeLength=10
snakeHead = [60,60] #snakehead starting coordinate, update this
snakeList.append(snakeHead)
#snakeList.append([60,50])
#snakeList.append([60,40])
#snakeList.append([60,30])

pygame.init()
gameDisplay = pygame.display.set_mode((w_width,w_height))
#check=not True
clock = pygame.time.Clock()
downarrow=uparrow=leftarrow=rightarrow=False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            downarrow= event.key== pygame.K_DOWN
            leftarrow= event.key== pygame.K_LEFT
            rightarrow= event.key==pygame.K_RIGHT
            uparrow= event.key==pygame.K_UP

    if downarrow:
        if ([snakeHead[0],snakeHead[1]+blockSize] in snakeList) or snakeHead[1] >= w_height:
            print("Game over, your score was", len(snakeList)-1)
            break
        coordinate_update(snakeList)
        snakeHead[1]+=blockSize

    elif uparrow:
        if [snakeHead[0],snakeHead[1]-blockSize] in snakeList or snakeHead[1] <= 0:
            print("Game over, your score was", len(snakeList)-1)
            break
        coordinate_update(snakeList)
        snakeHead[1]-=blockSize

    elif leftarrow:
        if [snakeHead[0]-blockSize,snakeHead[1]] in snakeList or snakeHead[0] <= 0:
            print("Game over, your score was", len(snakeList)-1)
            break
        coordinate_update(snakeList)
        snakeHead[0]-=blockSize

    elif rightarrow:
        if [snakeHead[0]+blockSize,snakeHead[1]] in snakeList or snakeHead[0] >= w_width:
            print("Game over, your score was", len(snakeList)-1)
            break
        coordinate_update(snakeList)
        snakeHead[0]+=blockSize

    gameDisplay.fill((0,0,0))
    pygame.draw.rect(gameDisplay,red,(init_x,init_y,blockSize,blockSize))
    new_x = math.floor(random.randint(0,w_width)/10)*10
    new_y = math.floor(random.randint(0,w_height)/10)*10
    while [new_x,new_y] in snakeList:
        new_x = random.randint(0,w_width)
        new_y = random.randint(0,w_height)
    snake_run(blockSize,snakeList)
    if([init_x,init_y]==snakeHead):
        snakeList.append([init_x,init_y])
        snakeHead=snakeList[0]
        move_food(init_x,init_y,new_x,new_y)
        init_x, init_y = new_x, new_y

    pygame.display.update()
    clock.tick(FPS)
