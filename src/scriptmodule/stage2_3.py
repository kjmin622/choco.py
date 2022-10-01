import os, sys, pygame
from pygame.locals import *
import pygame.mixer
import scriptmodule.textscript as textscript
from scriptmodule.constant import *

def init(screen, clock):
    scriptdata = textscript.Script([["testbackground.png",CHR_EMPTY,["두 요원이 탈출에 성공하나 싶었지만","'요원 Q'의 탈출장치가 고장나 출구에서 빠져나올 수 없다","결국 '요원 T'가 다시 본부에 복귀해서","탈출 장치를 가져오기로 하고 발걸음을 서둘렀다"]],
                                ["testbackground.png",AGENT_T,["[요원 T]헉..헉...","[요원 T] 그 녀석, 장치가 고장났으면 고장났다고 말을 해야할 거 아니야...","[요원 T]음..? 본부 앞이 왜 이렇게 붐비는거지? 한시가 급한데 말야","[요원 T]오늘이.. 월요일이군 정문으로 들어가면 늦겠어","[요원 T]하... 어쩔 수 없나? 이 길은 진짜 무서운데..."]],
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