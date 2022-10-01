import os, sys, pygame
from pygame.locals import *
import pygame.mixer
import scriptmodule.textscript as textscript
from scriptmodule.constant import *

def init(screen, clock):
    scriptdata = textscript.Script([["testbackground.png",AGENT_C,["[요원 C]이번 임무에 투입된 요원 Q와의 연락이 방금 끊어졌다","[요원 C]무슨 일이 생긴 것 같으니 즉시 현장으로 출동하도록."]],
                                ["testbackground.png",AGENT_T,["[요원 T]흠... 이 시간대면 도로를 지나가는 것이 최단 루트겠군","[요원 T]본부에 의하면... '공사중'...? 이게 뭐지?"]],
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