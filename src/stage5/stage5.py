import random, pygame, time, os


WHITE = (255,255,255)
YELLOW = (255,255,0)
pad_size = (1024,768)
GameTime = 90
Phase1 = 16
Phase2 = 20
Phase3 = 24

def main(param):
    screen=param['screen'];clock=param['clock'];wall=param['wall'];wall_width=param['wall_width'];wall_height=param['wall_height'];wall_1=param['wall_1']
    wall_2=param['wall_2'];wall_3=param['wall_3'];wall_4=param['wall_4'];wall_5=param['wall_5'];cat=param['cat'];cat_width=param['cat_width']
    cat_height=param['cat_height'];background1=param['background1'];background2=param['background2'];font=param['font'];background3=param['background3'];bgm=param['bgm'];collision_sound = param['collision_sound']
    boost_sound=param['boost_sound']
    chr_idx = 0
    max_chr_idx = 9
    phase = 1
    devide_idx = 3
    regen_wall = True

    def drawObject(obj, x, y):
        screen.blit(obj, (x, y))
    
    def drawCharacter(obj, x, y):
        obj.set_colorkey((0,0,0))
        screen.blit(obj, (x, y))

    def drawTime(time):
        time = GameTime-time
        text=font.render("Time left : %sm %ss"%(int(time//60), int(time%60)),True,WHITE)
        screen.blit(text, (0,10))

    def isCollision(x1, y1, width1, height1, x2, y2, width2, height2):
        if y1< y2+height2 and y2<y1+height1 and x1<x2+width2 and x2<x1+width1:
            return True
        else:
            return False

    def drawLife(x):
        text=font.render("%d"%(x),True,WHITE)
        screen.blit(text,(1000,10))
    
    
    def resetWalls(x):
        if x==1:
            return random.randrange(pad_size[0]*2, pad_size[0]*2+400)
        elif x==2:
            return random.randrange(pad_size[0]*2, pad_size[0]*2+400)
        elif x==3:
            return random.randrange(pad_size[0]*2, pad_size[0]*2+200)
        elif x==4:
            return random.randrange(pad_size[0]*2, pad_size[0]*2+200)
        elif x==5:
            return random.randrange(pad_size[0]*2, pad_size[0]*2+700)
        elif x==6:
            return random.randrange(pad_size[0]*2, pad_size[0]*2+700)
        elif x==7:
            return random.randrange(275, pad_size[1])
        elif x==8:
            return random.randrange(275, pad_size[1]-wall_height)
        elif x==9:
            return random.randrange(pad_size[1]-wall_height, pad_size[1])
    phase2_r = False
    phase3_r = False
    isClear = False
    life = 3
    speed = 16
    start_ticks = pygame.time.get_ticks()
    x=pad_size[0]*0.05  
    y=pad_size[1]*0.8
    wall_x = resetWalls(1)
    wall_1_x = resetWalls(2)
    wall_2_x = resetWalls(3)
    wall_3_x = resetWalls(4)
    wall_4_x = resetWalls(5)
    wall_5_x= resetWalls(6)
    wall_y = resetWalls(7)
    wall_1_y = resetWalls(7)
    wall_2_y = resetWalls(7)
    wall_3_y = resetWalls(7)
    wall_4_y = resetWalls(8)
    wall_5_y = resetWalls(9)
    x_change = 0
    y_change = 0
    background_y = 0
    background1_x = 0
    background2_x =pad_size[0]
    background3_x =pad_size[0]*2
    running = True
    bgm.play()
    while running:
        seconds = (pygame.time.get_ticks()-start_ticks)/1000
        if seconds >= GameTime : #시작 3분 후 클리어
            bgm.stop()
            isClear = True
            running = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bgm.stop()
                running = False
                isClear = None

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
        elif x<pad_size[0]-cat_width and x_change>0:
            x+=x_change
            
        if y>275 and y_change<0:
            y+=y_change
        elif y<pad_size[1]-cat_height and y_change>0:
            y+=y_change

        if seconds <30:
            speed = Phase1
        elif seconds<60:
            if not phase2_r:
                boost_sound.play()
                life += 1
                phase2_r = True
                speed = Phase2
        elif seconds<80:
            if not phase3_r:
                boost_sound.play()
                life += 2
                phase3_r = True
                speed = Phase3
            
        background1_x-=speed
        background2_x-=speed
        background3_x-=speed

        wall_x-=speed
        wall_1_x-=speed
        wall_2_x-=speed
        wall_3_x-=speed
        wall_4_x-=speed
        wall_5_x-=speed

        if isCollision(x, y, cat_width, cat_height, wall_x, wall_y, wall_width, wall_height):
            collision_sound.play()
            life-=1
            wall_x=resetWalls(1)
            wall_y=resetWalls(7)
        elif isCollision(x, y, cat_width, cat_height, wall_1_x, wall_1_y, wall_width, wall_height):
            collision_sound.play()
            life-=1
            wall_1_x=resetWalls(2)
            wall_1_y=resetWalls(7)
        elif isCollision(x, y, cat_width, cat_height, wall_2_x, wall_2_y, wall_width, wall_height):
            collision_sound.play()
            life-=1
            wall_2_x=resetWalls(3)
            wall_2_y=resetWalls(7)
        elif isCollision(x, y, cat_width, cat_height, wall_3_x, wall_3_y, wall_width, wall_height):
            collision_sound.play()
            life-=1
            wall_3_x=resetWalls(4)
            wall_3_y=resetWalls(7)
        elif isCollision(x, y, cat_width, cat_height, wall_4_x, wall_4_y, wall_width, wall_height):
            collision_sound.play()
            life-=1
            wall_4_x=resetWalls(5)
            wall_4_y=resetWalls(8)
        elif isCollision(x, y, cat_width, cat_height, wall_5_x, wall_5_y, wall_width, wall_height):
            collision_sound.play()
            life-=1
            wall_5_x=resetWalls(6)
            wall_5_y=resetWalls(9)

            
        if not(27 < seconds < 31) and not(57 < seconds < 61):    
            if wall_x+wall_width*0.8<=0:   
                wall_x=resetWalls(1)
                wall_y=resetWalls(7)
            if wall_1_x+wall_width*0.8<=0:
                wall_1_x=resetWalls(2)
                wall_1_y=resetWalls(7)
            if wall_2_x+wall_width*0.8<=0:
                wall_2_x=resetWalls(3)
                wall_2_y=resetWalls(7)
            if wall_3_x+wall_width*0.8<=0:
                wall_3_x=resetWalls(4)
                wall_3_y=resetWalls(7)
            if wall_4_x+wall_width*0.8<=0:
                wall_4_x=resetWalls(5)
                wall_4_y=resetWalls(8)
            if wall_5_x+wall_width*0.8<=0:
                wall_5_x=resetWalls(6)
                wall_5_y=resetWalls(9)
            
        if background1_x <=-pad_size[0]:
            background1_x+=pad_size[0]*3
        if background2_x <= -pad_size[0]:
            background2_x+=pad_size[0]*3
        if background3_x <= -pad_size[0]:
            background3_x+=pad_size[0]*3
        screen.fill(WHITE)
        drawObject(background1, background1_x, background_y)
        drawObject(background2, background2_x, background_y)
        drawObject(background3, background3_x, background_y)
        drawObject(wall,wall_x,wall_y)
        drawObject(wall_1,wall_1_x, wall_1_y)
        drawObject(wall_2,wall_2_x, wall_2_y)
        drawObject(wall_3,wall_3_x, wall_3_y)
        drawObject(wall_4,wall_4_x, wall_4_y)
        drawObject(wall_5,wall_5_x, wall_5_y)

        if(speed == 20 and phase==1): 
            chr_idx = 0
            devide_idx = 2
            phase = 2
        if(speed == 24 and phase==2): 
            chr_idx = 0
            devide_idx = 1
            phase = 3

        drawCharacter(cat[chr_idx//devide_idx], x, y)
        chr_idx += 1
        if(chr_idx == max_chr_idx*devide_idx): chr_idx = 0
        drawTime(seconds)
        drawLife(life)
        if life==0:
            bgm.stop()
            time.sleep(1.5)
            running = False
        clock.tick(60)
        pygame.display.update()

    return isClear


def init(screen, clock):
    DIR_PATH = os.path.abspath(os.path.dirname(__file__))
    DIR_IMAGE = os.path.join(DIR_PATH, 'images')
    DIR_BGM = os.path.join(DIR_PATH,'bgms')
    player = pygame.image.load(os.path.join(DIR_IMAGE,"character.png"))
    spr=[]
    # spriteSheet_player = sprite.SpriteSheet(16,16,8,8,12)  width = 16, height = 16, max_row = 8, max_col = 8, max_index = 12
    for i in range(12):
        image = pygame.Surface((16, 16))
        image.blit(player, (0, 0), ((i % 8) * 16, (i // 8) * 16, 16, 16))
        img = pygame.transform.scale(image, (64, 64))
        img.set_colorkey((0, 0, 0))
        spr.append(img)
    
    wall = pygame.image.load(os.path.join(DIR_IMAGE,"wall.png"))
    wall = pygame.transform.rotozoom(wall,0,0.08)
    wall_width = wall.get_width()
    wall_height = wall.get_height()
    wall_1= wall.copy()
    wall_2= wall.copy()
    wall_3= wall.copy()
    wall_4= wall.copy()
    wall_5= wall.copy()
    cat = spr
    cat_width = cat[0].get_width()
    cat_height = cat[0].get_height()
    font = pygame.font.Font(None,  30)
    background1 = pygame.image.load(os.path.join(DIR_IMAGE,"background.png"))
    background_width = background1.get_width()
    background_height = background1.get_height()
    background2 = background1.copy()
    background3 = background1.copy()
    bgm = pygame.mixer.Sound(os.path.join(DIR_BGM,"bgm.wav"))
    collision_sound = pygame.mixer.Sound(os.path.join(DIR_BGM,"collision.wav"))
    boost_sound = pygame.mixer.Sound(os.path.join(DIR_BGM,"boost.wav"))
    res = {'screen': screen,'clock':clock , 'wall':wall,'wall_width':wall_width,'wall_height':wall_height,'wall_1':wall_1,
    'wall_2':wall_2,'wall_3':wall_3,'wall_4':wall_4,'wall_5':wall_5,'cat':cat,'cat_width':cat_width,'cat_height':cat_height,'font':font,
    'background1':background1,'background_width':background_width,'background_height':background_height,'background2':background2, 'background3':background3, 'bgm':bgm, 'collision_sound' : collision_sound,'boost_sound':boost_sound}
    return res