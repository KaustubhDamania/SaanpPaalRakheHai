import pygame
import time
import random
import math
from pygame.locals import *

def displaySnake(snakeList):
    for coordinate in snakeList:
        pygame.draw.rect(gameDisplay,white,(coordinate[0],coordinate[1],10,10))

def snake_init(snakeHead):
    pygame.draw.rect(gameDisplay,white,(snakeHead[0],snakeHead[1],10,snakeLength))

def snake_move(snakeList):
    for i in range(len(snakeList)-1, 0, -1):
        snakeList[i] = snakeList[i-1].copy()

def changeFood(init_food_x,init_food_y,new_food_x,new_food_y):
    pygame.draw.rect(gameDisplay,black,(init_food_x,init_food_y,10,10))
    pygame.draw.rect(gameDisplay,red,(new_food_x,new_food_y,10,10))

FPS = 30
width = 800
height = 600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
clock = pygame.time.Clock()
#snakeHead = [math.floor(random.randint(0,width)/10)*10,math.floor(random.randint(0,height)/10)*10]
snakeHead = [60,60]
snakeLength = 10
snakeList=[]
snakeList.append(snakeHead)
init_food_x = 100
init_food_y = 100

downarrow = False
uparrow = False
rightarrow = False
leftarrow = False
pygame.init()
gameDisplay = pygame.display.set_mode((width,height))
arrow_key = [pygame.K_DOWN,pygame.K_UP,pygame.K_LEFT,pygame.K_RIGHT]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


        if event.type == pygame.KEYDOWN:
            if event.key in arrow_key:
                downarrow = event.key == pygame.K_DOWN
                uparrow = event.key == pygame.K_UP
                rightarrow = event.key == pygame.K_RIGHT
                leftarrow = event.key == pygame.K_LEFT

    if downarrow and snakeHead[1]<height:
        if [snakeHead[0],snakeHead[1]+10] in snakeList:
            print('Game Over')
            break
        snake_move(snakeList)
        snakeHead[1]+=10

    elif uparrow and snakeHead[1]>0:
        if [snakeHead[0],snakeHead[1]-10] in snakeList:
            print('Game Over')
            break
        snake_move(snakeList)
        snakeHead[1]-=10

    elif rightarrow and snakeHead[0]<width:
        if [snakeHead[0]+10,snakeHead[1]] in snakeList:
            print('Game Over')
            break
        snake_move(snakeList)
        snakeHead[0]+=10

    elif leftarrow and snakeHead[0]>0:
        if [snakeHead[0]-10,snakeHead[1]] in snakeList:
            print('Game Over')
            break
        snake_move(snakeList)
        snakeHead[0]-=10

    gameDisplay.fill((0,0,0))
    pygame.draw.rect(gameDisplay,red,(init_food_x,init_food_y,10,10))

    new_food_x = math.floor(random.randint(0,width)/10)*10
    new_food_y = math.floor(random.randint(0,height)/10)*10
    while [new_food_x,new_food_y] in snakeList:
        new_food_x = math.floor(random.randint(0,width)/10)*10
        new_food_y = math.floor(random.randint(0,height)/10)*10

    displaySnake(snakeList)
    if ([init_food_x,init_food_y] == snakeHead):
        snakeList.append([init_food_x,init_food_y])
        snakeHead = snakeList[0]
        changeFood(init_food_x,init_food_y,new_food_x,new_food_y)
        init_food_x,init_food_y = new_food_x,new_food_y

    pygame.display.update()
    clock.tick(FPS)
