import pygame
from pygame.locals import *
import os
import sys
import random
from constant import *
import path,room,side
pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional

# 화면 크기 설정

# 게임 내 

# 게임 프레임 초기 설정
FramePerSec = pygame.time.Clock()
# 게임 가로, 세로 창 크기 설정
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Game") # 게임 이름
# 아이템
# class Item:

# 배경 이미지
background = pygame.image.load(os.path.join(DIR_IMAGE,"bg.png"))

room_dic = {
    "1":room.Room([
        side.Side([],"bg.png",path.Path("2")),
        side.Side([],"bg.png"),
        side.Side([],"bg.png"),
        side.Side([],"bg.png"),
    ]),
    "2":room.Room([
        side.Side([],"bg.png"),
        side.Side([],"bg.png"),
        side.Side([],"bg.png"),
        side.Side([],"bg.png"),
    ]),
}
present = ["1",0]
# 이벤트 루프
running = True
while running:
    print(present)
    screen.blit(room_dic[present[0]].sidelist[present[1]].image,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                present[1] = side.turn_right(present[1])
            if event.key == pygame.K_a:
                present[1] = side.turn_left(present[1])
            if event.key == pygame.K_w:
                if room_dic[present[0]].sidelist[present[1]].path != None:
                    present[0] = room_dic[present[0]].sidelist[present[1]].path.direction
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                pass
            if event.key == pygame.K_a:
                pass
            if event.key == pygame.K_w:
                pass
    screen.blit(background, (0, 0))
    
    pygame.display.update() #게임화면 계속 그려주기
    
# pygame 종료
pygame.quit()


"""class Path:
    def __init__(self,인자들...):
        self.d = d
        self.wid = wid
        self.hei = hei
class Side:
    def __init__(self,인자들...):
        self.objs = objs
        self.bg1 = bg1
class Room:
    def __init__(self,인자들...):
        self.sidelist = sidelist
몇번째 패스=클래스이름(인자들...) 좌라락 나열
dic = {"a":"b","C":"d",..}
dic ["a"] => "b"
key 랑 value
room_dic = {~~~~}
"1" : oom(룸 설명)
        side()
        side()
        side()
        side()
"2"(얘네는 문자열) : room(룸 설명)
        side()"""
