import pygame,sys,random,math
from pygame.locals import *
import time
import random
def move_food(x,y,a,b): #moves food from x,y to a,b
    pygame.draw.rect(gameDisplay,black,(x,y,blockSize,blockSize))
    pygame.draw.rect(gameDisplay,red,(a,b,blockSize,blockSize))

def snake_run(blockSize,snakeList): #renders the entire snake
    for coordinate in snakeList:
        pygame.draw.rect(gameDisplay, white, (coordinate[0],coordinate[1],blockSize,blockSize))

def coordinate_update(snakeList): #shifts the coordinates of the snake
    for i in range(len(snakeList)-1,0,-1):
        snakeList[i]=snakeList[i-1].copy()

def display_message(): #display the score to the user
    print('Game over, your score was', len(snakeList)-1)
    pygame.quit()
    time.sleep(5)
    exit()

#defining some game parameters
width = 800
height = 600
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
FPS=30
blockSize=10
init_food_x = math.floor(random.randint(0,width-blockSize)/blockSize)*blockSize
init_food_y = math.floor(random.randint(0,height-blockSize)/blockSize)*blockSize
snakeList=[]
snakeHead = [60,60] #snakehead starting coordinate, update this
snakeList.append(snakeHead)


pygame.init()
gameDisplay = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
downarrow=uparrow=leftarrow=rightarrow=False
arrow_key = [pygame.K_DOWN,pygame.K_UP,pygame.K_LEFT,pygame.K_RIGHT] #list of all keys required

#game loop
while True:
    for event in pygame.event.get(): #event handling
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type==pygame.KEYDOWN and event.key in arrow_key:
            downarrow= event.key== pygame.K_DOWN
            leftarrow= event.key== pygame.K_LEFT
            rightarrow= event.key==pygame.K_RIGHT
            uparrow= event.key==pygame.K_UP

    #conditions for game over
    if downarrow:
        if ([snakeHead[0],snakeHead[1]+blockSize] in snakeList) or snakeHead[1] >= height:
            display_message()
        coordinate_update(snakeList)
        snakeHead[1]+=blockSize

    elif uparrow:
        if [snakeHead[0],snakeHead[1]-blockSize] in snakeList or snakeHead[1] <= 0:
            display_message()
        coordinate_update(snakeList)
        snakeHead[1]-=blockSize

    elif leftarrow:
        if [snakeHead[0]-blockSize,snakeHead[1]] in snakeList or snakeHead[0] <= 0:
            display_message()
        coordinate_update(snakeList)
        snakeHead[0]-=blockSize

    elif rightarrow:
        if [snakeHead[0]+blockSize,snakeHead[1]] in snakeList or snakeHead[0] >= width:
            display_message()
        coordinate_update(snakeList)
        snakeHead[0]+=blockSize

    gameDisplay.fill((0,0,0))
    pygame.draw.rect(gameDisplay,red,(init_food_x,init_food_y,blockSize,blockSize))

    #randomize food coordinate
    new_food_x = math.floor(random.randint(0,width)/blockSize)*blockSize
    new_food_y = math.floor(random.randint(0,height)/blockSize)*blockSize

    while [new_food_x,new_food_y] in snakeList:
        new_food_x = random.randint(0,width-blockSize)
        new_food_y = random.randint(0,height-blockSize)
    #render the snake
    snake_run(blockSize,snakeList)

    if([init_food_x,init_food_y]==snakeHead): #food is eaten by snake
        snakeList.append([init_food_x,init_food_y])
        snakeHead=snakeList[0]
        move_food(init_food_x,init_food_y,new_food_x,new_food_y)
        init_food_x, init_food_y = new_food_x, new_food_y
        FPS+=1000

    pygame.display.update()
    clock.tick(FPS)
