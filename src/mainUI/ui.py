import pygame,os,sys
from pygame.locals import *
import mainUI.button as button
from mainUI.constant import *
def init(screen, clock):

    return {"screen":screen, "clock":clock}

def main(param):
    screen = param["screen"];clock = param["clock"]
    background = pygame.image.load(os.path.join(DIR_IMAGE,"background.png"))
    startbutton = button.Button("start.png", WINDOW_SIZE[0]/2-176,WINDOW_SIZE[1]/2-275,352,150)
    loadbutton = button.Button("load.png",WINDOW_SIZE[0]/2-176,WINDOW_SIZE[1]/2-75,352,150)
    quitbutton = button.Button("quit.png",WINDOW_SIZE[0]/2-176,WINDOW_SIZE[1]/2+125,352,150)
    while(True):
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                return 3
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startbutton.is_clicked(pygame.mouse.get_pos()):
                    return 1
                if loadbutton.is_clicked(pygame.mouse.get_pos()):
                    return 2
                if quitbutton.is_clicked(pygame.mouse.get_pos()):
                    return 3
        screen.blit(startbutton.get_image(), (0,0))
        screen.blit(loadbutton.get_image(), (0,0))
        screen.blit(quitbutton.get_image(), (0,0))
        pygame.display.update()
        clock.tick(60)