import pygame, sys, time
import random
Black = (0, 0, 0)
WHITE = (255,255,255)
WindowWidth = 1024
WindowHeight = 768
GameTime = 180

def drawObject(obj, x, y):
    gamepad.blit(obj, (x, y))


def drawScore(x, y):
    text=font.render("%s, %s"%(x, y), True, WHITE)
    gamepad.blit(text, (724,10))

def drawTime(time):
    time = GameTime-time
    text=font.render("Time left : %sm %ss"%(int(time//60), int(time%60)),True,WHITE)
    gamepad.blit(text, (0,10))


def runGame():
    global gamepad, clock, start_ticks
    isCrash = False
    start_ticks = pygame.time.get_ticks()
    x=WindowWidth*0.4
    y=WindowHeight*0.8
    x_change=0
    background_x = (WindowWidth-background_width)/2
    wall_x=random.randint(background_x, 1024-background_x)
    wall_y=0
    background1_y=0
    background2_y=-WindowHeight
    running = True
    while running:
        if isCrash:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    x_change=-8
                elif event.key==pygame.K_d:
                    x_change=8
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_a or event.key==pygame.K_d:
                    x_change=0
        
        if x>background_x and x_change<0:
            x+=x_change
        elif x<1024-(background_x+cat_width) and x_change>0:
            x+=x_change
        
        wall_y+=16
        if wall_y>768:
            wall_x=random.randint(background_x,1024-background_x)
            wall_y=0

        
            
        background1_y+=16#in game range = background_x < range < 1024-(background_x+cat_width)
        background2_y+=16
        if background1_y>=WindowHeight:
            background1_y=-WindowHeight
        if background2_y>=WindowHeight:
            background2_y=-WindowHeight
        
        seconds = (pygame.time.get_ticks()-start_ticks)/1000
        if seconds >= GameTime : #시작 3분 후 클리어
            running = False
        gamepad.fill(Black)
        drawObject(background1, background_x, background1_y)
        drawObject(background2, background_x, background2_y)
        drawObject(cat, x, y)
        drawObject(wall, wall_x, wall_y)
        drawScore(x,y)
        drawTime(seconds)
        
        pygame.display.update()
        clock.tick(60) #fps 60
    pygame.quit()

def main():
    global gamepad, clock, cat, cat_width, cat_height, font, wall, wall_width, wall_height
    global background1, background2, background_width, background_height
    pygame.init()
    gamepad = pygame.display.set_mode((WindowWidth,WindowHeight))
    pygame.display.set_caption('Stage 5')
    wall = pygame.image.load("images/wall.png")
    wall_width = wall.get_width()
    wall_height = wall.get_height()
    wall = pygame.transform.rotozoom(wall,0,0.18)
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

main()
