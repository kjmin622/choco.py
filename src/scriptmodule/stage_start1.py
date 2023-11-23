import os, sys, pygame
from pygame.locals import *
import pygame.mixer
import scriptmodule.textscript as textscript
from scriptmodule.constant import *

def init(screen, clock):
    scriptdata = textscript.Script([["1-1.png",CHR_EMPTY,["아주 먼 옛날, 고양이는 신으로 대접받았다"]],
                                ["1-2.png",CHR_EMPTY,["그리고 그것은 지금도 아마 마찬가지일 것 같다"]],
                                ["1-3.png",CHR_EMPTY,["하지만 이렇게 사회에 고양이들이 살아갈 수 있는 것은"]],
                                ["1-4.png",CHR_EMPTY,["고양이 조직 [Secret Cat Association] 덕분이다"]],
                                ["1-5.png",CHR_EMPTY,["비밀리에 활동하는 이 조직은  구성원을 제외하고는,","인간을 포함한 모든 동물들이 존재 자체를 모른다"]],
                                ["1-6.png",CHR_EMPTY,["그들은 어둠 속에서 세상의 고양이들이", "편하게 살아갈 수 있는 사회를 만들기 위해 일한다"]],
                                ["1-7.png",CHR_EMPTY,["물론, 다른 동물들에게는 고양이 카페로 보이겠지만 말이다"]],
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