import random, pygame, time
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


WHITE = (255,255,255)
pad_width = 1024
pad_height = 768
GameTime = 180
Pase1 = 16
Pase2 = 20
Pase3 = 24

def drawObject(obj, x, y):
    gamepad.blit(obj, (x, y))


def drawScore(x, y):
    text=font.render("%s, %s"%(x, y), True, WHITE)
    gamepad.blit(text, (724,10))

def drawTime(time):
    time = GameTime-time
    text=font.render("Time left : %sm %ss"%(int(time//60), int(time%60)),True,WHITE)
    gamepad.blit(text, (0,10))

def isCollision(x1, y1, width1, height1, x2, y2, width2, height2):
    if y1< y2+height2 and y2<y1+height1 and x1<x2+width2 and x2<x1+width1:
        return True
    else:
        return False

def drawLife(x):
    if(x==1):
        text=font.render("1",True,WHITE)
        gamepad.blit(text,(1000,10))
    elif(x==2):
        text=font.render("2",True,WHITE)
        gamepad.blit(text,(1000,10))
    else:
        text=font.render("3",True,WHITE)
        gamepad.blit(text,(1000,10))
    
    
    


def runGame():
    global gamepad, clock, speed, life
    life = 3
    speed = 16
    start_ticks = pygame.time.get_ticks()
    x=pad_width*0.05
    y=pad_height*0.8
    wall_x = random.randrange(pad_width, pad_width+400)
    wall_1_x=random.randrange(pad_width, pad_width+400)
    wall_2_x=random.randrange(pad_width, pad_width+200)
    wall_3_x=random.randrange(pad_width, pad_width+200)
    wall_4_x=random.randrange(pad_width, pad_width+700)
    wall_5_x=random.randrange(pad_width, pad_width+700)
    wall_y = random.randrange(0,pad_height-wall_height)
    wall_1_y = random.randrange(0,pad_height-wall_height)
    wall_2_y = random.randrange(0,pad_height-wall_height)
    wall_3_y = random.randrange(0,pad_height-wall_height)
    wall_4_y = random.randrange(0,wall_height)
    wall_5_y = random.randrange(pad_height-wall_height*4,pad_height-wall_height)
    x_change = 0
    y_change = 0
    background_y = 0
    background1_x = 0
    background2_x =pad_width
    running = True
    while running:
        seconds = (pygame.time.get_ticks()-start_ticks)/1000
        if seconds >= GameTime : #시작 3분 후 클리어
            running = False
        
        if life==0:

                time.sleep(1)
                pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    y_change = -10
                elif event.key==pygame.K_s:
                    y_change = 10
                elif event.key==pygame.K_a:
                    x_change=-10
                elif event.key==pygame.K_d:
                    x_change= 5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_w or event.key==pygame.K_s:
                    y_change = 0
                elif event.key==pygame.K_a or event.key==pygame.K_d:
                    x_change = 0

        if x>0 and x_change<0:
            x+=x_change
        elif x<pad_width-cat_width and x_change>0:
            x+=x_change
            
        if y>0 and y_change<0:
            y+=y_change
        elif y<pad_height-cat_height and y_change>0:
            y+=y_change


        if seconds <60:
            speed = Pase1
        elif seconds<120:
            speed = Pase2
        else:
            speed = Pase3
            
        background1_x-=16
        background2_x-=16

        wall_x-=speed
        wall_1_x-=speed
        wall_2_x-=speed
        wall_3_x-=speed
        wall_4_x-=speed
        wall_5_x-=speed

        if isCollision(x, y, cat_width, cat_height, wall_x, wall_y, wall_width, wall_height):
            life-=1
            wall_x=random.randrange(pad_width, pad_width+200)
            wall_y=random.randrange(0,pad_height-wall_height)
        elif isCollision(x, y, cat_width, cat_height, wall_1_x, wall_1_y, wall_width, wall_height):
            life-=1
            wall_1_x=random.randrange(pad_width, pad_width+400)
            wall_1_y=random.randrange(0,pad_height-wall_height)
        elif isCollision(x, y, cat_width, cat_height, wall_2_x, wall_2_y, wall_width, wall_height):
            life-=1
            wall_2_x=random.randrange(pad_width, pad_width+200)
            wall_2_y=random.randrange(0,pad_height-wall_height)
        elif isCollision(x, y, cat_width, cat_height, wall_3_x, wall_3_y, wall_width, wall_height):
            life-=1
            wall_3_x=random.randrange(pad_width, pad_width+400)
            wall_3_y=random.randrange(0,pad_height-wall_height)
    
        elif isCollision(x, y, cat_width, cat_height, wall_4_x, wall_4_y, wall_width, wall_height):
            life-=1
            wall_4_x=random.randrange(pad_width, pad_width+600)
            wall_4_y=random.randrange(0,wall_height*2)
        elif isCollision(x, y, cat_width, cat_height, wall_5_x, wall_5_y, wall_width, wall_height):
            life-=1
            wall_5_x=random.randrange(pad_width, pad_width+600)
            wall_5_y=random.randrange(pad_height-(wall_height*2),pad_height-wall_height)

            
            
        if wall_x+wall_width*0.8<=0:
            wall_x=random.randrange(pad_width, pad_width+200)
            wall_y=random.randrange(0,pad_height-wall_height)
        if wall_1_x+wall_width*0.8<=0:
            wall_1_x=random.randrange(pad_width, pad_width+400)
            wall_1_y=random.randrange(0,pad_height-wall_height)
        if wall_2_x+wall_width*0.8<=0:
            wall_2_x=random.randrange(pad_width, pad_width+200)
            wall_2_y=random.randrange(0,pad_height-wall_height)
        if wall_3_x+wall_width*0.8<=0:
            wall_3_x=random.randrange(pad_width, pad_width+400)
            wall_3_y=random.randrange(0,pad_height-wall_height)
        if wall_4_x+wall_width*0.8<=0:
            wall_4_x=random.randrange(pad_width, pad_width+600)
            wall_4_y=random.randrange(0,wall_height*2)
        if wall_5_x+wall_width*0.8<=0:
            wall_5_x=random.randrange(pad_width, pad_width+600)
            wall_5_y=random.randrange(pad_height-(wall_height*2),pad_height-wall_height)
            
        if background1_x ==-pad_width:
            background1_x=pad_width

        if background2_x == -pad_width:
            background2_x=pad_width
        gamepad.fill(WHITE)
        drawObject(background1, background1_x, background_y)
        drawObject(background2, background2_x, background_y)
        drawObject(wall,wall_x,wall_y)
        drawObject(wall_1,wall_1_x, wall_1_y)
        drawObject(wall_2,wall_2_x, wall_2_y)
        drawObject(wall_3,wall_3_x, wall_3_y)
        drawObject(wall_4,wall_4_x, wall_4_y)
        drawObject(wall_5,wall_5_x, wall_5_y)
        drawObject(cat, x, y)
        drawTime(seconds)
        drawLife(life)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


def initGame():
    global gamepad, clock, cat, cat_width, cat_height, font, wall, wall_1,wall_2, wall_3, wall_4, wall_5, wall_width, wall_height
    global background1, background2, background_width, background_height
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width,pad_height))
    pygame.display.set_caption('Stage 5')
    wall = pygame.image.load("images/wall.png")
    wall = pygame.transform.rotozoom(wall,0,0.2)
    wall_width = wall.get_width()
    wall_height = wall.get_height()
    wall_1= wall.copy()
    wall_2= wall.copy()
    wall_3= wall.copy()
    wall_4= wall.copy()
    wall_5= wall.copy()
    cat = pygame.image.load("images/cat.png")
    cat = pygame.transform.rotozoom(cat,0,0.1)
    cat_width = cat.get_width()
    cat_height = cat.get_height()
    clock = pygame.time.Clock()
    font = pygame.font.Font(None,  30)
    background1 = pygame.image.load("images/background.png")
    background_width = background1.get_width()
    background_height = background1.get_height()
    background2 = background1.copy()
    runGame()


initGame()
