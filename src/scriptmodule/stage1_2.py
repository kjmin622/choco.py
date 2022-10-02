import os, sys, pygame
from pygame.locals import *
import pygame.mixer
import scriptmodule.textscript as textscript
from scriptmodule.constant import *

def init(screen, clock):
    scriptdata = textscript.Script([["script2_bg.png",AGENT_T,["[요원 T]후... 저런 것들이 길을 막고 있다니...","[요원 T]하마터면 나도 큰일날 뻔 했어","[요원 T]여긴가... Q가 있는 곳은? 저기 흰 덩어리겠군"]],
                                ["script2_bg.png",AGENT_Q,["[요원 Q]T! 구하러 와줬구나!"]],
                                ["script2_bg.png",AGENT_T,["[요원 T]아니 나도 갇혔어"]],
                                ["script2_bg.png",AGENT_Q,["[요원 Q]??????????"]],
                                ["script2_bg.png",AGENT_T,["[요원 T]농담이고, 구조를 보니 탈출하기 쉽지 않을 거 같은데?"]],
                                ["script2_bg.png",AGENT_Q,["[요원 Q]둘러보니까 혼자서는 탈출 못하는 구조야. 서로 힘을 합쳐야 해"]],
                                ["script2_bg.png",AGENT_T,["[요원 T]너랑?","[요원 T]합을?","[요원 T]흠..."]],
                                ["script2_bg.png",AGENT_Q,["[요원 Q]빨리 와!"]],
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