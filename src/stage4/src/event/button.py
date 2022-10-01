import pygame
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import engine.move as move

class FuncSetGround:
    def __init__(self, map_obj, row, col, mapdocumant):
        self.map_obj = map_obj
        self.row = row
        self.col = col
        self.mapdocumant = mapdocumant
        
    def removefunc(self):
        if((self.row,self.col) in self.mapdocumant["tile"]):
            self.mapdocumant["tile"].remove((self.row,self.col))
    
    def appendfunc(self):
        self.mapdocumant["tile"].append((self.row,self.col))

class Button:
    def __init__(self, rect, sprite, startfunc, endfunc):
        self.sprite = sprite
        self.rect = rect
        self.startfunc = startfunc
        self.endfunc = endfunc
        self.status = False
        self.classname = "Button"
    
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
        if(not self.status and (move.collision_object(p1, self.rect) or move.collision_object(p2, self.rect))):
            self.status = True
            self.startfunc()
            return True
        # 접촉해제
        elif(self.status and not (move.collision_object(p1, self.rect) or move.collision_object(p2, self.rect))):
            self.status = False
            self.endfunc()
            return True
        return False