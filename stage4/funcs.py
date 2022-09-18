import pygame, os
from constant import *
from globalvariable import *


class FuncSetGround:
    def __init__(self, map_obj, row, col):
        self.map_obj = map_obj
        self.row = row
        self.col = col
        
    def removefunc(self):
        global g_mapdocumant
        if((self.row,self.col) in g_mapdocumant["tile"]):
            g_mapdocumant["tile"].remove((self.row,self.col))
    
    def appendfunc(self):
        global g_mapdocumant
        g_mapdocumant["tile"].append((self.row,self.col))


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
    for (row,col) in g_mapdocumant["tile"]:
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
            self.scriptText.switch_display()
            return True
        # 접촉해제
        if(self.scriptText.display==True and not(collision_object(p1, self.rect) or collision_object(p2, self.rect))):
            self.scriptText.switch_display()
            return False
