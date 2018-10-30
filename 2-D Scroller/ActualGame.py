#[HHH]   [V][v][v]
#[HHH] = [V][v][v]
#[HHH]   [v][v][v] 
import pygame
import time
class ImageSprite:
    def __init__(self,ImageLocations,X=0,Y=0):
        self.Costumes = []
        for __x in range(0,len(ImageLocations)):
            self.Costumes.append(pygame.image.load(ImageLocations[__x]))
        self.visible = True
        self.X_Position = X
        self.Y_Position = Y
        self.Current_Costume = self.Costumes[0]
        self.CostumeIndex = 0
        self.CostumeFlip = False
        self.width,self.height = self.Current_Costume.get_rect().size
    def SetCostume(self,index):
        #print("Changing Costume to",index)
        if self.CostumeFlip:
            self.Current_Costume = pygame.transform.flip(self.Costumes[index],True,False)
        else:
            self.Current_Costume = self.Costumes[index]
        self.width,self.height = self.Current_Costume.get_rect().size
        self.CostumeIndex = index
    def SetPosition(self,X,Y):
        self.X_Position = X
        self.Y_Position = Y
pygame.init()
ShotArray = []
EnemyArray = []
def Shoot(x,y,fps,DirectionLeft):
    index = len(ShotArray)
    ShotArray.append([ImageSprite(["./Assets/Beam/Beam.png"],x,y),DirectionLeft])
    time.sleep(2/fps)
def Touching(Sprite1,Sprite2):
    bx = Sprite1.X_Position
    hb = Sprite1.height
    wb = Sprite1.width
    by = Sprite1.Y_Position
    ho = Sprite1.height
    wo = Sprite1.width
    ox = Sprite2.X_Position
    oy = Sprite2.Y_Position
    xoverlay , yoverlay = False,False
    if bx >= ox:
        if bx <= (ox + wo):
            xoverlay = True
        else:
            xoverlay = False
    else:
        if (bx + wb) > ox:
            xoverlay = True
        else:
            xoverlay = False
    if by >= oy:
        if by <= (oy + ho):
            yoverlay = True
        else:
            yoverlay = False
    else:
        if (by + hb) > oy:
            yoverlay = True
        else:
            yoverlay = False
        
    return (xoverlay and yoverlay)
    
    
def IsTouchingEdges(Sprite,DisplayX,DisplayY):
    if Sprite.X_Position <= 0:
        return "Left"
    if Sprite.Y_Position <= 0:
        return "Top"
    if Sprite.Y_Position + Sprite.height >= DisplayY:
        return "Bottom"
    if Sprite.X_Position + Sprite.width >= DisplayX:
        return "Right"
    else:
        return "None"
NewMap = """
V                                          V
V                              HHHHHH      V
V                                          V
V                                          V
VHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHV
"""
def GameLoop(DisplayX=800,DisplayY=600,Map = NewMap):
    Disp = pygame.display.set_mode((DisplayX,DisplayY))
    pygame.display.set_caption('NewGame')
    clk = pygame.time.Clock()
    GameRunning = True
    fps = 120
    images = ["./Assets/Ironman/0.png","./Assets/Ironman/1.png","./Assets/Ironman/2.png","./Assets/Ironman/3.png","./Assets/Ironman/4.png","./Assets/Ironman/5.png","./Assets/Ironman/6.png","./Assets/Ironman/7.png","./Assets/Ironman/8.png","./Assets/Ironman/9.png","./Assets/Ironman/10.png","./Assets/Ironman/11.png"]
    Ironman = ImageSprite(images,X= DisplayX/2,Y=DisplayY/2)
    Y_modifier = 0
    Ironman.SetCostume(1)
    Walking = False
    KEY_HOLDS = {"Up":False,"Down":False,"Right":False,"Left":False,"Space":False}
    BeamCapacity = 100
    Mapper = {"H":"./Assets/Scroller/H.png","V":"./Assets/Scroller/V.png"}
    MapShift = 0
    while GameRunning:
#########################################################Player Control Area###############################################################################
        #print(IsTouchingEdges(Ironman,DisplayX,DisplayY))
        
        if IsTouchingEdges(Ironman,DisplayX,DisplayY) == "Bottom":
            Ironman.Y_Position = DisplayY - Ironman.height
        if IsTouchingEdges(Ironman,DisplayX,DisplayY) == "Top":
            Ironman.Y_Position = 0
        for event in pygame.event.get():
            #print("Event Checker",event)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    KEY_HOLDS["Down"] = True
                elif event.key == pygame.K_UP:
                    KEY_HOLDS["Up"] = True
                elif event.key == pygame.K_RIGHT:
                    KEY_HOLDS["Right"] = True
                    Ironman.CostumeFlip = False
                elif event.key == pygame.K_LEFT:
                    KEY_HOLDS["Left"] = True
                    Ironman.CostumeFlip = True
                elif event.key == pygame.K_SPACE:
                    KEY_HOLDS["Space"] = True
                Ironman.SetCostume(Ironman.CostumeIndex)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    KEY_HOLDS["Down"] = False
                elif event.key == pygame.K_UP:
                    KEY_HOLDS["Up"] = False
                elif event.key == pygame.K_RIGHT:
                    KEY_HOLDS["Right"] = False
                elif event.key == pygame.K_LEFT:
                    KEY_HOLDS["Left"] = False
                elif event.key == pygame.K_SPACE:
                    KEY_HOLDS["Space"] = False
        if KEY_HOLDS["Space"]:
            if IsTouchingEdges(Ironman,DisplayX,DisplayY):
                Ironman.SetCostume(10)
            else:
                Ironman.SetCostume(9)
            if not(Ironman.CostumeFlip):
                Shoot(Ironman.X_Position+Ironman.width,Ironman.Y_Position+15,fps,Ironman.CostumeFlip)
            else:
                Shoot(Ironman.X_Position-165,Ironman.Y_Position+15,fps,Ironman.CostumeFlip)
        else:
            if KEY_HOLDS["Right"] or KEY_HOLDS["Left"]:
                if IsTouchingEdges(Ironman,DisplayX,DisplayY) == "Bottom":#right arrow key pressed while on ground
                    time.sleep(2/fps)
                    Ironman.SetCostume(((int((Ironman.CostumeIndex - 1)) + 2)%5 )+ 2)#To switch between 1 to 6 costumes
                    
                    if not KEY_HOLDS["Up"]:
                        Ironman.SetPosition(Ironman.X_Position,DisplayY- Ironman.height)#if no up arrow is pressed , set position to ground level
                else:
                    Ironman.SetCostume(11)#if in air
                if Ironman.CostumeFlip:
                        MapShift = MapShift + 5
                else:
                        MapShift = MapShift - 5
            if KEY_HOLDS["Up"] and IsTouchingEdges(Ironman,DisplayX,DisplayY) != "Top":#IF not touching ceiling and up arrowkey is pressed
                Ironman.SetPosition(Ironman.X_Position,Ironman.Y_Position - 5)
                if not (KEY_HOLDS["Right"] or KEY_HOLDS["Left"]):#while in air if right arrow or left arrow key is not pressed
                    Ironman.SetCostume(0)
            if KEY_HOLDS["Down"]:
                if IsTouchingEdges(Ironman,DisplayX,DisplayY) != "Bottom":#Down arrow key is pressed
                    Ironman.SetPosition(Ironman.X_Position,Ironman.Y_Position + 5)
                    if not (KEY_HOLDS["Right"] or KEY_HOLDS["Left"]):
                        Ironman.SetCostume(0)
                else:#if  touching ground and down arrow key is pressed
                    Ironman.SetCostume(1)
                    Ironman.SetPosition(Ironman.X_Position,DisplayY- Ironman.height)
#############################################################Map Filler####################################################################################
        Disp.fill((255,255,255))
        MapSketcher = Map.split("\n")
        del MapSketcher[0]
        del MapSketcher[len(MapSketcher)-1]
        for row in range(0,len(MapSketcher)):
            for column in range(0,len(MapSketcher[row])):
                if MapSketcher[row][column] in ["H","V"]:
                    Disp.blit(pygame.image.load(Mapper[MapSketcher[row][column]]),((column*40) +40 + MapShift,DisplayY -((len(MapSketcher)- row -1)*40) -40))

####End of player character handling#######################################################################################################################
                
        Disp.blit(Ironman.Current_Costume,(Ironman.X_Position,Ironman.Y_Position))
###############################################3Shooting Collision Detection################################################################################
        for beam in  range(0,len(ShotArray)):
            if ShotArray[beam][1]:
                ShotArray[beam][0].SetPosition(ShotArray[beam][0].X_Position-5,ShotArray[beam][0].Y_Position)
            else:
                ShotArray[beam][0].SetPosition(ShotArray[beam][0].X_Position+5,ShotArray[beam][0].Y_Position)
            for guy in range(0,len(EnemyArray)):
                if Touching(ShotArray[beam],EnemyArray[guy]):
                             EnemyArray[guy].kill()
                             ShotArray[beam].kill()
                             del EnemyArray[guy]
                             del ShotArray[beam]
                if (ShotArray[beam][0].X_Position > Ironman.X_Position + DisplayX) or (ShotArray[beam][0].X_Position < Ironman.X_Position + DisplayX):
                    ShotArray[Beam].kill()
                    del ShotArray[Beam]
            Disp.blit(ShotArray[beam][0].Current_Costume,(ShotArray[beam][0].X_Position,ShotArray[beam][0].Y_Position))
        pygame.display.flip()
        clk.tick(fps)
GameLoop()
            
