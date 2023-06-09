import pygame
import random
import math
import introscene
#-----------------------------------------------------------------------------
pygame.display.set_caption("Bella gam the sequel")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False
pygame.init()
#--------------------------
#Constants
#--------------------------
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
SPACE = True

#------------------------

#game states
START = 0
CONTINUE = 1
GAMEOVER = 2
SHOPPING = 3

#variables
#----------------------
xpos = 400 #xpos of player
ypos = 100 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
x_offset = 0
y_offset = 0
movingx = False
movingy = False
isOnGround = False
fall = 0
ticker = 0
keys = [False, False, False, False] #this list holds whether each key has been pressed

playerhp = 100
direction = DOWN
moving = False
frameHeight = 50
frameWidth = 50
offset = 0
frameNum = 0
pughp = 100

#----------------------
#---------------------------

#images
#-------------------------
brick = pygame.image.load('brickss.jpg')
grass = pygame.image.load('grass.jpg')
temp = pygame.image.load('butta dawg.jpg') #temporary image/player

#boss 1!!----
pug1 = pygame.image.load('pug1.jpg')
pug2 = pygame.image.load('pug2.jpg')

clock = pygame.time.Clock() #putting this here just in case!
#-------------------------

#ememies class----------------------------
class silly:
    
    def __init__(self, cxpos, cypos):
        self.cxpos = cxpos
        self.cypos = cypos
        self.counter = 0
        self.vx = 2
        self.vy = 0
        self.isOnGround = False
        self.alive = True
    def draw(self):
        if self.alive == True: 
            #if self.vx > 0:
                screen.blit(pug2, (self.cxpos, self.cypos))
                #screen.blit(pug2, (self.cxpos + x_offset, self.cypos + y_offset))
            # self.vx < 0:
                screen.blit(pug1, (self.cxpos, self.cypos))
                #screen.blit(pug1, (self.cxpos + x_offset, self.cypos + y_offset))
                
    
    #REFLECTION
        #if self.cxpos -20 < 0 or self.cxpos + 20 + 100 > 800:
          #self.vx *= -1

        self.cxpos += self.vx
        self.cypos += self.vy
        
    def gravity(self):

      #GRAVITY
            if self.cypos > 800 - 100: #check if your feet are on the ground
                self.isOnGround = True
                self.cypos = 800 - 100
                self.vy = 0 #stot falling if on ground
            else:
                self.isOnGround = False
            if self.isOnGround == False:
                self.vy+=.2 #if not on ground, fall downwards
                
    def death (self, pughp):
        if pughp <= 0:
            return True
        
        
#-----------------------------------------


#Fireball--------------------
class fireball:
    def __init__(self):
        self.xpos = -10 #draw offscreen when not in use
        self.ypos = -10
        self.isAlive = False
        self.direction = RIGHT
    def shoot(self, x, y, dir):
        self.xpos = x + 20
        self.ypos = y + 20
        self.isAlive = True
        self.direction = dir
    def move(self):
        if self.direction == RIGHT:
            self.xpos+=20
        if self.direction == LEFT:
            self.xpos-=20
    def draw(self):
        pygame.draw.circle(screen, (250, 0, 0), (self.xpos, self.ypos), 10)
        pygame.draw.circle(screen, (250, 250, 0), (self.xpos, self.ypos), 5)
    #def collide(self, x, y):
        
ballin = fireball()        

#MAP!!!!! ------------------------------------------------------------------------------------------------
map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 3,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 2,3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2 ,2 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0 ,2 ,0, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1,1]]

#i'm going to make 1 grass, and 2 brick for now....
#----------------------------------------------------------------------------------------------------------

bruh = silly(600, 0)

introscene.backstory()

#GAM LOOP!!!!-------------------------------
while not gameover:
    clock.tick(60) #basically the fps
    ticker+=1
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
    
    
        if event.type == pygame.KEYDOWN: #keyboard input
                if event.key == pygame.K_LEFT:
                    keys[LEFT]=True
                elif event.key == pygame.K_RIGHT:
                    keys[RIGHT]=True
                elif event.key == pygame.K_UP:
                    keys[UP]=True
                elif event.key == pygame.K_SPACE:
                      SPACE = True
             
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    keys[LEFT]=False
                elif event.key == pygame.K_RIGHT:
                    keys[RIGHT]=False
                elif event.key == pygame.K_UP:
                    keys[UP]=False
                elif event.key == pygame.K_SPACE:
                    SPACE = False
                

     #LEFT MOVEMENT
    if keys[LEFT]==True:
        if xpos > 400:
            vx = -3
        elif offset<0:
            offset+=3
            vx =0
        else:
            vx = -3
        RowNum = 0
        direction = LEFT
        moving = True
    
        
    #RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        if xpos<400:
            vx=3
        elif offset>-800:
            offset-=3
            vx = 0
        else:
            vx = 3
        RowNum = 1
        direction = RIGHT
        moving = True
    #turn off velocity
    else:
        vx = 0
        moving = False
        
    
    if SPACE == True:
        print("shoot")
        ballin.shoot(xpos, ypos, direction)
        print("shoot LOL")
        
        
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        RowNum = 2
        isOnGround = False
        direction = UP
        moving = True
    
    xpos+=vx #update player xpos
    ypos+=vy
    print(vx, vy)
    
    #check space for shooting
    
       
    ballin.move()
    
    bruh.gravity()
    
    
# collision so you dont fall through the floor like an idiot
    if map[int((ypos+frameHeight)/50)][int((xpos-offset+frameWidth/2)/50)]==1 or map[int((ypos+frameHeight)/50)][int((xpos-offset+frameWidth/2)/50)]==2:
        isOnGround = True
        vy=0
    else:
        isOnGround = False
    
    #you're going to hit your head on the bottom of a brick perhaps
    if map[int((ypos)/50)][int((xpos-offset+frameWidth/2)/50)]==1 or map[int((ypos)/50)][int((xpos-offset+frameWidth/2)/50)]==2:
        vy=0
        
    #left collision (it's extra long because we check both head and feets(well, knees) for left collision
    if (map[int((ypos+frameHeight-10)/50)][int((xpos-offset-10)/50)]==1 or map[int((ypos)/50)][int((xpos-offset-10)/50)]==1 or map[int((ypos+frameHeight-10)/50)][int((xpos-offset-10)/50)]==2 or map[int((ypos)/50)][int((xpos-offset-10)/50)]==2 ) and direction == LEFT:
        xpos+=3
        
    #right collision needed here
    if (map[int((ypos+frameHeight-10)/50)][int((xpos-offset+frameWidth+5)/50)]==1 or map[int((ypos)/50)][int((xpos-offset+frameWidth+5)/50)]==1 or map[int((ypos+frameHeight-10)/50)][int((xpos-offset+frameWidth+5)/50)]==2 or map[int((ypos)/50)][int((xpos-offset+frameWidth+5)/50)]==2 ) and direction == RIGHT:
        xpos-=3
    
    #stop moving if you hit edge of screen (will be removed for scrolling)
    if xpos+frameWidth > 800:
        xpos-=3
    if xpos<0:
        xpos+=3
        
    #stop falling if on bottom of game screen
    if ypos > 800-frameHeight:
        isOnGround = True
        vy = 0
        ypos = 800-frameHeight
    
    #gravity
    if isOnGround == False:
        vy+=.2
        
    
#render section-----------------------------------
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    
    #draw map
    for i in range (16):
        for j in range(32):
            if map[i][j]==1:
                screen.blit(grass, (j*50+offset, i*50), (0, 0, 50, 50))
                
            
            if map[i][j]==2:
                screen.blit(brick, (j*50+offset, i*50), (0, 0, 50, 50))
    
    if ballin.isAlive == True:
        ballin.draw()
    
    print(offset)
    screen.blit(temp, (xpos, ypos))
    bruh.draw()
    pygame.display.flip()
    
#-----------------------------------------
pygame.quit()

