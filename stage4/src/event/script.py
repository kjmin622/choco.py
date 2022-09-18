import os
import sys
import pygame

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from data.constant import *
import engine.move as move


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
        if(self.scriptText.display==False and (move.collision_object(p1, self.rect) or move.collision_object(p2, self.rect))):
            self.scriptText.switch_display()
            return True
        # 접촉해제
        if(self.scriptText.display==True and not(move.collision_object(p1, self.rect) or move.collision_object(p2, self.rect))):
            self.scriptText.switch_display()
            return False