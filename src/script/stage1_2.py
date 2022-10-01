import os, sys, pygame
from pygame.locals import *
import pygame.mixer
import script
# trash code
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1024,768))
clock = pygame.time.Clock()

def init(screen, clock):
    scriptdata = script.script([["testbackground.png","testcharacter.png",["test1","test2","test3"]],
                                ["testbackground.png","testcharacter2.png",["test4","test5","test6"]],
                                ])
    return {"screen":screen, "clock":clock, "scriptdata":scriptdata}


def main(param):
    screen = param["screen"]; clock = param["clock"]; scriptdata = param["scriptdata"]

    while True:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            if event.type == KEYDOWN:
                if event.key == K_SPACE or event.key == K_RETURN:
                    exist_next = scriptdata.next()
                    if not exist_next:
                        return True
        
        screen.blit(scriptdata.get_draw_image(),(0,0))
        pygame.display.update()
        clock.tick(60)

main(init(screen,clock))