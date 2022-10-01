
import pygame,os,sys
from constant import *
class ScreenScript:
    #script_list : [[image, [(script,(x,y)) ... ]], ...]
    def __init__(self, script_list):
        self.script_list = [[os.path.join(DIR_IMAGE,image),scripts] for image, scripts in script_list]
        self.now = [0,0]
        self.gamefont = pygame.font.Font(os.path.join(DIR_FONT, DEFAULT_FONT_NAME),END_FONT_1)
        self.highlightfont = pygame.font.Font(os.path.join(DIR_FONT, DEFAULT_FONT_NAME),END_FONT_2)
    
    def get_draw_image(self):
        image = pygame.Surface(WINDOW_SIZE)
        image.fill((255,255,255))
        background = pygame.image.load(self.script_list[self.now[0]][0])
        
        image.blit(background,(0,0))

        for i in range(self.now[1]+1):
            text = self.script_list[self.now[0]][1][i][0]
            text_surface = self.gamefont.render(text,False,(255,255,255))
            if(self.now[0]==len(self.script_list)-1):
                text_surface = self.highlightfont.render(text,False,(255,255,255))
            
            text_rect = text_surface.get_rect()
            text_rect.midtop = (self.script_list[self.now[0]][1][i][1])
            image.blit(text_surface, text_rect)

        return image
    
    def next(self):
        self.now[1] += 1
        if self.now[1] >= len(self.script_list[self.now[0]][1]):
            self.now[1] = 0
            self.now[0] += 1
            if self.now[0] >= len(self.script_list):
                return False
        return True