import pygame  #importing pygame
import time    #for delay
def GameLoop(DisplayX=800,DisplayY=600):
    Disp = pygame.display.set_mode((DisplayX,DisplayY))  #explain tuple
    pygame.display.set_caption('Pong Unleashed')
    clk = pygame.time.Clock()
    GameRunning = True
    fps = 60
    paddle1 = pygame.image.load("./Assets/paddle1.bmp")
    paddle2 = pygame.image.load("./Assets/paddle2.bmp")
    ball  = pygame.image.load("./Assets/ball.bmp")
    ballPos = [DisplayX/2,DisplayY/2]
    KEY_HOLDS = {"Up":False,"Down":False,"W":False,"S":False}  #explain dictionary
    width,height = paddle1.get_rect().size   #explain about get_rect
    radius,_ = ball.get_rect().size    #underscore explain
    p1 = [10,0]
    p2 = [DisplayX -width -10,0]
    p1VelY = 0
    p2VelY = 0
    BallVel = [4,4]
    RedScore = 0
    BlueScore = 0
    while GameRunning:
        #event handling
        for event in pygame.event.get():     #list of all the events occuring in the game window 
            if event.type == pygame.QUIT:    
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:   #TO keep track of key press
                if event.key == pygame.K_DOWN:
                    KEY_HOLDS["Down"] = True
                elif event.key == pygame.K_UP:
                    KEY_HOLDS["Up"] = True
                if event.key == pygame.K_w:
                    KEY_HOLDS["W"] = True
                elif event.key == pygame.K_s:
                    KEY_HOLDS["S"] = True
            if event.type == pygame.KEYUP:    #to check if keys is not pressed which was previously pressed 
                if event.key == pygame.K_DOWN:
                    KEY_HOLDS["Down"] = False
                elif event.key == pygame.K_UP:
                    KEY_HOLDS["Up"] = False
                if event.key == pygame.K_w:
                    KEY_HOLDS["W"] = False
                elif event.key == pygame.K_s:
                    KEY_HOLDS["S"] = False
        if KEY_HOLDS["W"]:   
            p1VelY = -10       #why? explain it
        elif KEY_HOLDS["S"]:
            p1VelY = 10
        else:
            p1VelY = 0
        
        if KEY_HOLDS["Up"]:
            p2VelY = -10
        elif KEY_HOLDS["Down"]:
            p2VelY = 10
        else:
            p2VelY = 0
        #asdsfs=[]
        #End of event handling
        if p1[1] > DisplayY - height:#lower boundary  
                p1[1] = DisplayY - height
                p1VelY = 0
        if p1[1] < 0:#upper boundary
                p1[1] = 0
                p1VelY = 0    
        if p2[1] > DisplayY - height:#lower boundary
                p2[1] = DisplayY - height
                p2VelY = 0        
        if p2[1] < 0:#upper boundary
                p2[1] = 0
                p2VelY = 0

        ballPos[0],ballPos[1] = ballPos[0] + BallVel[0] ,ballPos[1] + BallVel[1]   #this helps the ball to move in XY plane
        if ballPos[1] < 0 or ballPos[1] > DisplayY - radius: #boundary conditions for ball
           BallVel[1] = -BallVel[1]
        if ballPos[0] < 0:#boundary
           BallVel[0] = -BallVel[0]
           #Blue Loses
           #BallVel[0] = -BallVel[0]
           RedScore += 1
           ballPos = [DisplayX/2,DisplayY/2]
           print("Red:",RedScore,"\tBlue:",BlueScore)
           time.sleep(1)
        if ballPos[0] > DisplayX - radius:   #wall boundary conditions
            #Red loses
            BallVel[0] = -BallVel[0]
            BlueScore += 1
            print("Red:",RedScore,"\tBlue:",BlueScore)
            ballPos = [DisplayX/2,DisplayY/2]
            time.sleep(1)
        if ballPos[0] < p2[0] + width and ballPos[0] + radius > p2[0]:          #collision detector
            if ballPos[1] + radius > p2[1] and ballPos[1] < p2[1] + height:
                BallVel[0] = -BallVel[0]
                BallVel[1] = BallVel[1] #+ (p2VelY/5) things go crazy if you comment this out.
        if ballPos[0] > p1[0] and ballPos[0] < p1[0]+width:          #collision detector
            if ballPos[1] + radius > p1[1] and ballPos[1]  < p1[1] + height:
                BallVel[0] = -BallVel[0]
                BallVel[1] = BallVel[1] #+ (p1VelY/5)   chiti chiti boom boom for pong
        Disp.fill((255,255,255))   #to remove the previous traces of our drawn components in the game
        
        #p1[1] = ballPos[1] - (height/2)#Computer as opponent
        #p2[1] = ballPos[1] - (height/2)#Computer as opponent  #SastaAI
        #p2[512<<6>>15 & 1] = ballPos[1344654534535**sum(asdsfs)] - (height>>1) 
        p2[1] = p2[1] + p2VelY     #this operation helps to move the paddle with the velocity defined above. 
        p1[1] = p1[1] + p1VelY
        Disp.blit(ball,(ballPos[0],ballPos[1]))   #blit() is used to actually draw the game components.  
        Disp.blit(paddle1,(p1[0],p1[1]))
        Disp.blit(paddle2,(p2[0],p2[1]))
        pygame.display.flip()
        clk.tick(fps)
GameLoop()
