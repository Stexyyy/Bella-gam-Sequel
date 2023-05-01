import pygame

#-----------------------------------------------------------------------------
pygame.display.set_caption("Bella gam the sequel")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False
pygame.init()
#--------------------------

#variables
#----------------------
xpos = 400 #xpos of player
ypos = 100 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
isOnGround = False
fall = 0
ticker = 0
keys = [False, False, False, False] #this list holds whether each key has been pressed
playerhp = 100
direction = DOWN
moving = False
frameHeight = 100
frameWidth = 100
#----------------------

#Constants
#--------------------------
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
#---------------------------

#images
#-------------------------
brick = pygame.image.load('brickss.jpg')
grass = pygame.image.load('grass.jpg')

clock = pygame.time.Clock() #putting this here just in case!
#-------------------------

#MAP!!!!! ------------------------------------------------------------------------------------------------
map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 3,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,2, 2,3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2 ,2 ,2, 0,0],
       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2 ,2 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0 ,2 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0 ,0 ,0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0,0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1,0]]

#i'm going to make 1 grass, and 2 brick for now....
#----------------------------------------------------------------------------------------------------------

#GAM LOOP!!!!-------------------------------
while not gameover:
    clock.tick(60) #basically the fps
    
    if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True
    elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
                
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
                screen.blit(dirt, (j*50+offset, i*50), (0, 0, 50, 50))
            if map[i][j]==2:
                screen.blit(brick, (j*50+offset, i*50), (0, 0, 50, 50))
            if map[i][j]==3:
                screen.blit(cat, (j*50+offset, i*50), (0, 0, 50, 50))

    
#-----------------------------------------
pygame.quit()

