import os, sys, pygame
from pygame.locals import *
import pygame.mixer
import screen_script
from constant import *

def init(screen, clock):
    scriptdata = screen_script.ScreenScript([["testbackground2.png",[("비상 출입구랍시고 만들어 놓은 저 막돼먹은 곳을",(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2-150)),
                                                                     ("어떻게든 통과해 본부에 도착한 나는",(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2-70)),
                                                                     ("재빨리 탈출 장치를 챙겨 '요원 Q'에게 향했다",(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2+10)),
                                                                     ("확실히 내려갈 때는 안 무섭더군...",(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2+90)),
                                                                    ]
                                                                ],
                                             ["testbackground2.png",[("뻔뻔한 'Q'녀석이 왜 이제야 오냐고 툴툴대길래",(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2-190)),
                                                                     ("진지하게 그냥 놓고갈까 싶었지만...",(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2-110)),
                                                                     ("내 커리어에 금이 가게 할 수는 없지...",(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2-30)),
                                                                     ("이 모양이긴 하지만 어쨌든 내 파트너니까",(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2+50)),
                                                                     ("앞으로도 이런 식의 임무는 계속 되겠지. 힘들겠지만....",(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2+130)),
                                                                    ]
                                                                ],
                                             ["testbackground2.png",[("그것이 전 세계의 고양이들을 위한 일이니까.",(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2)),
                                                                    ]
                                                                ],
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