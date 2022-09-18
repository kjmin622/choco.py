import pygame, os, sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from data.constant import *


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

#  애니메이션 변경 함수
def change_player_action(frame, action_var, new_var, frame_spd, new_frame_spd, ani_mode, new_ani_mode):
    if action_var != new_var:
        action_var = new_var
        frame = 0
        frame_spd = new_frame_spd
        ani_mode = new_ani_mode

    return frame, action_var, frame_spd, ani_mode
