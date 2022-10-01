import os, sys, pygame
from pygame.locals import *
import pygame.mixer
from constant import *

class script:
    # screen_list = [[image_path, character_image_path, [script, ...]], ...]
    def __init__(self, screen_list): 
        self.screen_list = [[os.path.join(DIR_IMAGE, image_path),os.path.join(DIR_IMAGE, character_image_path),script_list]  for image_path, character_image_path, script_list in screen_list]
        self.now = [0,0]
        self.gamefont = pygame.font.Font(os.path.join(DIR_FONT, DEFAULT_FONT_NAME),33)
        self.namefont = pygame.font.Font(os.path.join(DIR_FONT, DEFAULT_FONT_NAME),33, bold=True)
    
    def split_name_text(self, text):
        if(text[0] == '['):
            return text[1:].split(']')
        else:
            return ["",text]

    def get_draw_image(self):
        image = pygame.Surface(WINDOW_SIZE)
        image.fill((255,255,255))
        background = pygame.image.load(self.screen_list[self.now[0]][0])
        character = pygame.image.load(self.screen_list[self.now[0]][1])
        character.set_colorkey((255,255,255))
        textbox = pygame.image.load(os.path.join(DIR_IMAGE, "scriptbox.png"))
        textbox.set_colorkey((0,0,0))
        fulltext = self.split_name_text(self.screen_list[self.now[0]][2][self.now[1]])
        name = fulltext[0]
        if(name==""):
            textbox = pygame.image.load(os.path.join(DIR_IMAGE, "scriptbox2.png"))
        name_surface = self.namefont.render(name,False,(225,225,225))
        name_rect = name_surface.get_rect()
        name_rect.midtop = (round(WINDOW_SIZE[0]/5),round(WINDOW_SIZE[1]-280))
        text = fulltext[1]
        text_surface = self.gamefont.render(text,False,(50,50,50))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (round(WINDOW_SIZE[0]/2),round(WINDOW_SIZE[1]-135))
        
        image.blit(background,(0,0))
        image.blit(character,(0,0))
        image.blit(textbox,(0,0))
        image.blit(name_surface, name_rect)
        image.blit(text_surface, text_rect)

        return image

    def next(self):
        self.now[1] += 1
        if self.now[1] >= len(self.screen_list[self.now[0]][2]):
            self.now[1] = 0
            self.now[0] += 1
            if self.now[0] >= len(self.screen_list):
                return False
        return True