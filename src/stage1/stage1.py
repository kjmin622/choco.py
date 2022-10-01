import pygame
from pygame.locals import *
import os
import sys
import random
from constant import *
import path,room,side
import room_dictionary

#나중에 지울꺼임
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game") 
###########################################

def init(screen,clock):
    background = pygame.image.load(os.path.join(DIR_IMAGE,"side.png"))
    room_dic = room_dictionary.get_room_dic()
    present = ["1",0]
    return {"screen":screen,"clock":clock,"background":background,"room_dic":room_dic,"present":present}

def main(param):
    screen = param["screen"];clock = param["clock"];background = param["background"];room_dic = param["room_dic"];present = param["present"]
    while True:
        print(present)
        screen.blit(room_dic[present[0]].sidelist[present[1]].image,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    present[1] = side.turn_right(present[1])
                if event.key == pygame.K_a:
                    present[1] = side.turn_left(present[1])
                if event.key == pygame.K_w:
                    if room_dic[present[0]].sidelist[present[1]].path != None:
                        present[0] = room_dic[present[0]].sidelist[present[1]].path.direction
        
        pygame.display.update() 
        clock.tick(60)
        
        
#나중에 지울거임
main(init(screen,clock))