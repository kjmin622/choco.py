import pygame, os, random

# 상수 모음
DIR_PATH = os.path.dirname(__file__)
DIR_IMAGE = os.path.join(DIR_PATH, 'image')
DIR_SOUND = os.path.join(DIR_PATH, 'sound')
DIR_FONT = os.path.join(DIR_PATH, 'font')

WINDOW_SIZE = (1080,720)
TILE_SIZE = 8
#
TILE_MAPSIZE = (int(WINDOW_SIZE[0]/7.5), int(WINDOW_SIZE[1]/20))

BACKGROUND_COLOR = (27,25,25)

DEFAULT_FONT_NAME = "munro.ttf"

PLAYER_ROWSPEED = 2
PLAYER_MAXCOLSPEED = 3
PLAYER_COLACCELERATE = 0.2


MAPLIST = [
[0 for i in range(20)],
[0 for i in range(20)],
[0 for i in range(20)],
[0 for i in range(20)],
[0 for i in range(20)],
[0 for i in range(20)],
[0 for i in range(20)],
[0 for i in range(20)],
[0 for i in range(20)],
[0 for i in range(20)],
[0 for i in range(20)],
[0 for i in range(20)],
[0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
[0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
[0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0],
[0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1],
[1 for i in range(20)],
[1 for i in range(20)],
]



class SpriteSheet:
    # spr
    # width
    # height

    def __init__(self, filename, width, height, max_row, max_col, max_index):
        baseImage = pygame.image.load(os.path.join(DIR_IMAGE,filename)).convert()
        self.spr = []
        self.width = width
        self.height = height

        for i in range(max_index):
            image = pygame.Surface((width,height))
            image.blit(baseImage, (0,0), ((i%max_row)*width, (i//max_col)*height,width,height))
            image.set_colorkey((0,0,0))
            self.spr.append(image)

def createSpriteSet(spriteSheet, index_list, index_max = None):
    spr = []

    if index_max == None:
        for index in index_list:
            spr.append(spriteSheet.spr[index])
    else:
        for index in range(index_list, index_max+1):
            spr.append(spriteSheet.spr[index])
    
    return spr

def draw_text(screen, text, size, color, x, y):
    gameFont = pygame.font.Font(os.path.join(DIR_FONT,DEFAULT_FONT_NAME),size)
    text_surface = gameFont.render(text, False, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (round(x), round(y))
    screen.blit(text_surface, text_rect)

# 맵 이미지 반환 함수
def createMapImage(sheet_ground):
    image = pygame.Surface((TILE_MAPSIZE[0]*TILE_SIZE, TILE_MAPSIZE[1]*TILE_SIZE))
    
    for row in range(len(MAPLIST)):
        for col in range(len(MAPLIST[row])):
            if(MAPLIST[row][col]==1): 
                # 맵 이미지 생성 시, 근처 블럭에 따른 이미지 변화
                # 상좌하우 - 블럭 있을 시 True
                tmpimage = None
                aroundTile = [False,False,False,False]
                #T***
                if(row>0 and MAPLIST[row-1][col]==1):
                    aroundTile[0]=True
                #*T**
                if(col>0 and MAPLIST[row][col-1]==1):
                    aroundTile[1]=True
                #**T*
                if(row<len(MAPLIST)-1 and MAPLIST[row+1][col]==1):
                    aroundTile[2]=True
                #***T
                if(col<len(MAPLIST[row])-1 and MAPLIST[row][col+1]==1):
                    aroundTile[3]=True
                    
                #FFFF
                if(aroundTile == [False,False,False,False]):
                    tmpimage = pygame.transform.rotate(sheet_ground.spr[5],0)
                #TFFF
                elif(aroundTile == [True,False,False,False]):
                    tmpimage = pygame.transform.rotate(sheet_ground.spr[3],180)
                #FTFF
                elif(aroundTile == [False,True,False,False]):
                    tmpimage = pygame.transform.rotate(sheet_ground.spr[3],270)
                #FFTF
                elif(aroundTile == [False,False,True,False]):
                    tmpimage = pygame.transform.rotate(sheet_ground.spr[3],0)
                #FFFT
                elif(aroundTile == [False,False,False,True]):
                    tmpimage = pygame.transform.rotate(sheet_ground.spr[3],90)
                #TTFF
                elif(aroundTile == [True,True,False,False]):
                    tmpimage = pygame.transform.rotate(sheet_ground.spr[2],270)
                #TFTF
                elif(aroundTile == [True,False,True,False]):
                    tmpimage = pygame.transform.rotate(pygame.transform.flip(sheet_ground.spr[4],random.choice([True,False]),random.choice([True,False])),180)
                #TFFT
                elif(aroundTile == [True,False,False,True]):
                    tmpimage = pygame.transform.rotate(sheet_ground.spr[2],180)
                #FTTF
                elif(aroundTile == [False,True,True,False]):
                    tmpimage = pygame.transform.rotate(sheet_ground.spr[2],0)
                #FTFT
                elif(aroundTile == [False,True,False,True]):
                    tmpimage = pygame.transform.rotate(pygame.transform.flip(sheet_ground.spr[4],random.choice([True,False]),random.choice([True,False])),0)
                #FFTT
                elif(aroundTile == [False,False,True,True]):
                    tmpimage = pygame.transform.rotate(sheet_ground.spr[2],90)
                #TTTF
                elif(aroundTile == [True,True,True,False]):
                    tmpimage = pygame.transform.rotate(sheet_ground.spr[1],270)
                #TTFT
                elif(aroundTile == [True,True,False,True]):
                    tmpimage = pygame.transform.rotate(sheet_ground.spr[1],180)
                #TFTT
                elif(aroundTile == [True,False,True,True]):
                    tmpimage = pygame.transform.rotate(sheet_ground.spr[1],90)
                #FTTT
                elif(aroundTile == [False,True,True,True]):
                    tmpimage = pygame.transform.rotate(sheet_ground.spr[1],0)
                #TTTT
                elif(aroundTile == [True,True,True,True]):
                    tmpimage = pygame.transform.rotate(pygame.transform.flip(sheet_ground.spr[0],random.choice([True,False]),random.choice([True,False])),random.choice([0,90,180,270]))
                    

                image.blit(tmpimage,(col*TILE_SIZE, row*TILE_SIZE))
    return image

# 바닥과 충돌 검사 함수
def collision_floor(rect):
    hit_list = []
    for row in range(len(MAPLIST)):
        for col in range(len(MAPLIST[row])):

            if MAPLIST[row][col] != 0:
                floor_rect = pygame.rect.Rect((col * TILE_SIZE, row * TILE_SIZE), (TILE_SIZE, TILE_SIZE))
                if rect.colliderect(floor_rect):
                    hit_list.append(floor_rect)

    return hit_list

# 오브젝트 이동
def move(rect, movement):
    collision_types = {'top': False, 'bottom': False, "right": False, "left": False}
    rect.x += movement[0]
    hit_list = collision_floor(rect)

    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types["left"] = True
    
    rect.y += movement[1]
    hit_list = collision_floor(rect)

    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types["bottom"] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types["top"] = True
    
    return rect, collision_types


#  애니메이션 변경 함수
def change_playerAction(frame, action_var, new_var, frameSpd, new_frameSpd, aniMode, new_aniMode):
    if action_var != new_var:
        action_var = new_var
        frame = 0
        frameSpd = new_frameSpd
        aniMode = new_aniMode

    return frame, action_var, frameSpd, aniMode