import pygame, os
from mainUI.constant import *

class Button:
    def __init__(self, img, x,y,width,height):
        self.img = pygame.image.load(os.path.join(DIR_IMAGE, img))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def get_image(self):
        image = pygame.Surface(WINDOW_SIZE)
        image.blit(self.img, (self.x, self.y))
        image.set_colorkey((0,0,0))
        return image

    def is_clicked(self, pos):
        if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
            return True
        else:
            return False
