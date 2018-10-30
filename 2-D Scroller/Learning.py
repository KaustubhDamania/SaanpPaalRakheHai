import pygame
pygame.init()
Disp = pygame.display.set_mode((800,600))#Width and height
pygame.display.set_caption('NewGame')#Give name to the window
clk = pygame.time.Clock()#Clock for the game
GameOver = False
Ix,Iy = 0,0
dx,dy = 0,0
IronmanImage = pygame.image.load("./Assets/Ironman/0.png")
fps = 120#just variable to keep control on fps
while not GameOver:#This will be the game loop
    for event in pygame.event.get():#event.get() aquires all the events such as mouse click ,position,keypress and stuff
        if event.type == pygame.QUIT:#If the cross button is pressed
            #print("Exit Button Clicked")
            exit()
        
        if event.type == pygame.KEYDOWN:#to check if any keys were pressed down
            #for key release use KEYUP
            if event.key == pygame.K_DOWN:#K_Down for down arrow key
                #Iy = Iy + 1
                dy = 5
            elif event.key == pygame.K_UP:
                #Iy = Iy - 1
                dy = -5
        if event.type == pygame.KEYUP:#to check if any keys were pressed down
            #for key release use KEYUP
            if event.key == pygame.K_DOWN:#K_Down for down arrow key
                #Iy = Iy + 1
                dy = 0
            elif event.key == pygame.K_UP:
                #Iy = Iy - 1
                dy = 0
    Disp.fill((215,215,0))#order of drawing things on surfaces matter
    Disp.blit(IronmanImage,(Ix,Iy))#thing drawn first has least z index
    Ix = Ix + dx
    Iy = Iy + dy
    print("Ix is:",Ix,"\tIy is:",Iy)
                
    
    pygame.display.update()#Makes changes to the user screen.Just like matplotlib's .show() 
    clk.tick(fps)#Frames per second is controlled here
pygame.quit()
quit()
