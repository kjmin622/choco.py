import pygame, os, random
from mapdata import *

# 상수 모음
DIR_PATH = os.path.dirname(__file__)
DIR_IMAGE = os.path.join(DIR_PATH, 'image')
DIR_SOUND = os.path.join(DIR_PATH, 'sound')
DIR_FONT = os.path.join(DIR_PATH, 'font')

WINDOW_SIZE = (1080,720)
TILE_SIZE = 8

TILE_MAPSIZE = (2000,500)

BACKGROUND_COLOR = (27,25,25)

DEFAULT_FONT_NAME = "Sunflower-Medium.ttf"

PLAYER_ROWSPEED = 2
PLAYER_MAXCOLSPEED = 3
PLAYER_COLACCELERATE = 0.2

PLAYER_NAME1 = "냥이1"
PLAYER_NAME2 = "냥이2"

TESTMODE = True
TESTSPAWN = (101,465)

MAPLIST = MAPDATA
MAPDOCUMANT = {
            "tile":[],
            "spawn":[],
        }

class Map:
    def __init__(self, screen, sheet_ground):
        global MAPDOCUMANT
        self.sheet_ground = sheet_ground
        self.screen = screen
        for data in MAPLIST.keys():
            index = data.split(",")
            index = [int(index[0]),int(index[1])]
            if MAPLIST[data]==1 :
                MAPDOCUMANT["tile"].append((index[0],index[1]))
            if MAPLIST[data]==-1 :
                MAPDOCUMANT["spawn"] = [index[0],index[1]]

    def _get_suitable_tile(self, row, col):
        tmpimage = None
        aroundTile = [False,False,False,False]
            #T***
        if((row,col-1) in MAPDOCUMANT["tile"]):
            aroundTile[0]=True
        #*T**
        if((row-1,col) in MAPDOCUMANT["tile"]):
            aroundTile[1]=True
        #**T*
        if((row,col+1) in MAPDOCUMANT["tile"]):
            aroundTile[2]=True
        #***T
        if((row+1,col) in MAPDOCUMANT["tile"]):
            aroundTile[3]=True

        #FFFF
        if(aroundTile == [False,False,False,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[5],0)
        #TFFF
        elif(aroundTile == [True,False,False,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[3],180)
        #FTFF
        elif(aroundTile == [False,True,False,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[3],270)
        #FFTF
        elif(aroundTile == [False,False,True,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[3],0)
        #FFFT
        elif(aroundTile == [False,False,False,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[3],90)
        #TTFF
        elif(aroundTile == [True,True,False,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[2],270)
        #TFTF
        elif(aroundTile == [True,False,True,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[4],90)
        #TFFT
        elif(aroundTile == [True,False,False,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[2],180)
        #FTTF
        elif(aroundTile == [False,True,True,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[2],0)
        #FTFT
        elif(aroundTile == [False,True,False,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[4],0)
        #FFTT
        elif(aroundTile == [False,False,True,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[2],90)
        #TTTF
        elif(aroundTile == [True,True,True,False]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[1],270)
        #TTFT
        elif(aroundTile == [True,True,False,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[1],180)
        #TFTT
        elif(aroundTile == [True,False,True,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[1],90)
        #FTTT
        elif(aroundTile == [False,True,True,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[1],0)
        #TTTT
        elif(aroundTile == [True,True,True,True]):
            tmpimage = pygame.transform.rotate(self.sheet_ground.spr[0],0)
        
        return tmpimage

    def create_map_image(self):
        image = pygame.Surface((TILE_MAPSIZE[0]*TILE_SIZE, TILE_MAPSIZE[1]*TILE_SIZE))
        
        for (row,col) in MAPDOCUMANT["tile"]: 
            image.blit(self._get_suitable_tile(row,col),(row*TILE_SIZE, col*TILE_SIZE))

        image.set_colorkey((0,0,0))
        return image

    def set_ground(self, row, col, remove=False):
        if(not remove):
            MAPDOCUMANT["tile"].append((row,col))
        else:
            MAPDOCUMANT["tile"].remove((row,col))

class FuncSetGround:
    def __init__(self, map_obj, row, col):
        self.map_obj = map_obj
        self.row = row
        self.col = col
        
    def removefunc(self):
        global MAPDOCUMANT
        if((self.row,self.col) in MAPDOCUMANT["tile"]):
            MAPDOCUMANT["tile"].remove((self.row,self.col))
    
    def appendfunc(self):
        global MAPDOCUMANT
        MAPDOCUMANT["tile"].append((self.row,self.col))


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

def create_sprite_set(sprite_sheet, index_list, index_max = None):
    spr = []

    if index_max == None:
        for index in index_list:
            spr.append(sprite_sheet.spr[index])
    else:
        for index in range(index_list, index_max+1):
            spr.append(sprite_sheet.spr[index])
    
    return spr


# 바닥과 충돌 검사 함수
def collision_floor(rect):
    hit_list = []
    for (row,col) in MAPDOCUMANT["tile"]:
        floor_rect = pygame.rect.Rect((row * TILE_SIZE, col * TILE_SIZE), (TILE_SIZE, TILE_SIZE))
        if rect.colliderect(floor_rect):
            hit_list.append(floor_rect)

    return hit_list

def collision_object(rect1, rect2):
    if(rect1.colliderect(rect2)):
        return True
    return False

# 오브젝트 이동
def move(rect, otherRect, movement):
    collision_types = {'top': False, 'bottom': False, "right": False, "left": False}
    rect.x += movement[0]
    hit_list = collision_floor(rect)
    if(collision_object(rect, otherRect)):
        hit_list.append(otherRect)

    for tile in hit_list:
        org_left = rect.left
        org_right = rect.right
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types["left"] = True
    
    rect.y += movement[1]
    hit_list = collision_floor(rect)
    if(collision_object(rect, otherRect)):
        hit_list.append(otherRect)

    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types["bottom"] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types["top"] = True
    
    return rect, collision_types


#  애니메이션 변경 함수
def change_player_action(frame, action_var, new_var, frame_spd, new_frame_spd, ani_mode, new_ani_mode):
    if action_var != new_var:
        action_var = new_var
        frame = 0
        frame_spd = new_frame_spd
        ani_mode = new_ani_mode

    return frame, action_var, frame_spd, ani_mode



class Button:
    def __init__(self, rect, sprite, startfunc, endfunc):
        self.sprite = sprite
        self.rect = rect
        self.startfunc = startfunc
        self.endfunc = endfunc
        self.status = False
    
    def event_image(self,image):
        if(self.status):
            pygame.draw.rect(image, (0,0,0), [self.rect.x,self.rect.y,self.rect.width, self.rect.height])
            image.blit(self.sprite.spr[1],(self.rect.x,self.rect.y))
        else:
            pygame.draw.rect(image, (0,0,0), [self.rect.x,self.rect.y,self.rect.width, self.rect.height])
            image.blit(self.sprite.spr[0],(self.rect.x,self.rect.y))
        return image

    def perceive(self, p1, p2):
        # 접촉했을 때
        if(not self.status and (collision_object(p1, self.rect) or collision_object(p2, self.rect))):
            self.status = True
            self.startfunc()
            return True
        # 접촉해제
        elif(self.status and not (collision_object(p1, self.rect) or collision_object(p2, self.rect))):
            self.status = False
            self.endfunc()
            return True
        return False

class ScriptText:
    def __init__(self,text):
        self.text = text
        self.display = False
        self.image = self.makeimage()

    def makeimage(self):
        image = pygame.Surface(WINDOW_SIZE)
        pygame.draw.rect(image,(245,245,245),[50,WINDOW_SIZE[1]-200, WINDOW_SIZE[0]-100, 180])
        
        gamefont = pygame.font.Font(os.path.join(DIR_FONT, DEFAULT_FONT_NAME),30)
        text_surface = gamefont.render(self.text,False,(50,50,50))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (round(WINDOW_SIZE[0]/2),round(WINDOW_SIZE[1]-115))
        image.blit(text_surface, text_rect)
        image.set_colorkey((0,0,0))
        return image

    def switch_display(self):
        self.display = not self.display

    def is_show(self):
        return self.display

class ScriptEvent:
    def __init__(self, rect, sprite, text):
        self.rect = rect
        self.sprite = sprite
        self.scriptText = ScriptText(text)
        self.imageinit = False
    
    def event_image(self,image):
        if not self.imageinit:
            image.blit(self.sprite.spr[2],(self.rect.x, self.rect.y))
            self.imageinit = True
        return image

    def perceive(self, p1, p2):
        #접촉했을 때
        if(self.scriptText.display==False and (collision_object(p1, self.rect) or collision_object(p2, self.rect))):
            self.scriptText.switchdisplay()
            return True
        # 접촉해제
        if(self.scriptText.display==True and not(collision_object(p1, self.rect) or collision_object(p2, self.rect))):
            self.scriptText.switchdisplay()
            return False
