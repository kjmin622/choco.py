from asyncio import events
import pygame, sys, os
from pygame.locals import *
import pygame.mixer

from constant import *
from globalvariable import *
from funcs import *
from map import *


pygame.init()
pygame.mixer.init()

#
pygame.display.set_caption("stage4")
clock = pygame.time.Clock()

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
screen_scaled = pygame.Surface((WINDOW_SIZE[0]/4,WINDOW_SIZE[1]/4))

spriteSheet_player = SpriteSheet("character.png", 16,16,8,8,12)
spriteSheet_player2 = SpriteSheet("character2.png",16,16,8,8,12)
spriteSheet_ground = SpriteSheet("ground.png",8,8,48,8,6)
spriteSheet_object = SpriteSheet("object.png", 8,8,80,8,10)
spriteSheet_map1 = SpriteSheet("map1.png",8,8,16,16,87)

spr_player = {}
spr_player["stay"] = create_sprite_set(spriteSheet_player, [0])
spr_player['run'] = create_sprite_set(spriteSheet_player, 1, 8)
spr_player['jump'] = create_sprite_set(spriteSheet_player, [9, 10, 11])

spr_player2 = {}
spr_player2["stay"] = create_sprite_set(spriteSheet_player2, [0])
spr_player2['run'] = create_sprite_set(spriteSheet_player2, 1, 8)
spr_player2['jump'] = create_sprite_set(spriteSheet_player2, [9, 10, 11])

mapManager = Map(screen_scaled, spriteSheet_ground)

# 최초 스폰 위치
player_spawn_x, player_spawn_y = g_mapdocumant["spawn"]
mapImage = mapManager.create_map_image()

## test
if(TESTMODE):
    player_spawn_x, player_spawn_y = TESTSPAWN

# event list
eventList = []
scriptEventList = []
button_Ground_List = [
    # 버튼 위치 + 땅 생성 위치 + 리버스 여부
    
    #2단점프
    (44,444,49,448,False),

    #2단점프
    (31,478,34,442,False),
    (31,478,49,448,False),
    (31,478,41,467,False),

    # 문열기
    (35,468,40,478,True),
    (35,468,42,478,True),
    (35,468,41,477,True),
    (35,468,40,476,True),
    (35,468,42,476,True),
    (35,468,41,468,False),
    (45,478,41,475,True),
    (45,478,40,474,True),
    (45,478,42,474,True),
    (45,478,41,473,True),
    (45,478,40,472,True),
    (45,478,42,472,True),

    #엘레베이터
    (101,465,107,465,False),
    (101,465,107,464,False),
    (101,465,107,463,False),
    (101,465,107,462,False),
    (101,465,107,461,False),
    (101,465,107,460,False),
    (101,465,107,459,False),
    (101,465,107,458,False),
    (101,465,107,457,False),
    (101,465,107,456,False),
    (101,465,107,455,False),
    (101,465,107,454,False),
    (101,465,107,453,False),
    (101,465,107,452,False),
    (101,465,107,451,False),
    (101,465,107,450,False),
    (101,465,107,449,False),
    (101,465,107,448,False),
    (101,465,107,447,False),
    (101,465,107,446,False),
    (101,465,107,445,False),
    (101,465,107,444,False),
    (101,465,107,443,False),
    (101,465,107,442,False),

    #이후 문열기
    (111,447,108,464,True),
    (111,447,108,465,True),

    # 스위치점프맵
    (112,465,122,444,False),
    (114,465,126,442,False),
    (112,465,130,442,False),
    (114,465,133,439,False),
    (112,465,138,438,False),
    (114,465,142,437,False),
    (112,465,139,432,False),
    (114,465,131,433,False),
    (112,465,131,429,False),
    (114,465,131,425,False),
    (112,465,131,421,False),
    (114,465,131,417,False),
    (112,465,137,420,False),
    (114,465,145,425,False),
    (112,465,155,434,False),
    (112,465,156,434,False),
    (112,465,157,434,False),
    (112,465,158,434,False),
    (112,465,159,434,False),
    (112,465,160,434,False),
    (112,465,161,434,False),
    (112,465,162,434,False),
    (112,465,163,434,False),
    (112,465,164,434,False),
    (112,465,165,434,False),
    (112,465,166,434,False),
    (112,465,167,434,False),

    #스위치 점프맵2
    (168,433,129,465,False),
    (168,433,133,462,False),
    (168,433,133,461,False),
    (168,433,133,460,False),
    (168,433,133,459,False),
    (168,433,133,458,False),
    (168,433,137,465,False),
    (168,433,141,462,False),
    (168,433,141,461,False),
    (168,433,141,460,False),
    (168,433,141,459,False),
    (168,433,141,458,False),
    (168,433,145,465,False),
    (168,433,149,462,False),
    (168,433,149,461,False),
    (168,433,149,460,False),
    (168,433,149,459,False),
    (168,433,149,458,False),
    (168,433,153,465,False),
    (168,433,157,462,False),
    (168,433,157,461,False),
    (168,433,157,460,False),
    (168,433,157,459,False),
    (168,433,157,458,False),
    (168,433,161,465,False),
    (168,433,166,463,False),
    (168,433,166,461,False),
    (168,433,166,459,False),
    (168,433,166,457,False),
    (168,433,166,455,False),
    (168,433,166,453,False),
    (168,433,166,451,False),
    (168,433,166,449,False),

    #내려보내기
    (167,447,162,448,True),
    #스위치 점프맵3
    (171,433,122,444,False),
    (173,433,126,442,False),
    (171,433,130,442,False),
    (173,433,133,439,False),
    (171,433,138,438,False),
    (173,433,142,437,False),
    (171,433,139,432,False),
    (173,433,131,433,False),
    (171,433,131,429,False),
    (173,433,131,425,False),
    (171,433,131,421,False),
    (173,433,131,417,False),
    (171,433,137,420,False),
    (173,433,145,425,False),
    (171,433,155,434,False),
    (173,433,156,434,False),
    (171,433,157,434,False),
    (173,433,158,434,False),
    (171,433,159,434,False),
    (173,433,160,434,False),
    (171,433,161,434,False),
    (173,433,162,434,False),
    (171,433,163,434,False),
    (173,433,164,434,False),
    (171,433,165,434,False),
    (173,433,166,434,False),
    (171,433,167,434,False),

]

script_text_List = [
    (40,467,f"{PLAYER_NAME2}는 방향키로 움직일 수 있다."),
    (43,467,"Q를 누르면 시점이 바뀌니 거리가 멀어지면 활용하자"),
    (53,453,"공중에 있는 친구 머리를 밟고 뛰면... 높게는 뛰겠지만 기분은 나쁠지도"),
    (99,465,"이게 엘레베이터라고? 낑겨 죽는거 아니야?"),
    (166,447,"다시 내려가는 문인가?")
]

# event func
## button_ground
for event in button_Ground_List:
    eventfunc = FuncSetGround(mapManager, event[2], event[3])
    if(not event[4]):
        eventList.append(Button(pygame.Rect((event[0]*TILE_SIZE, event[1]*TILE_SIZE), (8,8)), spriteSheet_object, eventfunc.appendfunc, eventfunc.removefunc))
    else:
        eventList.append(Button(pygame.Rect((event[0]*TILE_SIZE, event[1]*TILE_SIZE), (8,8)), spriteSheet_object, eventfunc.removefunc, eventfunc.appendfunc))
        
## script event
for event in script_text_List:
    eventfunc = ScriptEvent(pygame.Rect((event[0]*TILE_SIZE, event[1]*TILE_SIZE),(8,8)), spriteSheet_object, event[2])
    scriptEventList.append(eventfunc)
    eventList.append(eventfunc)

# event image
event_image = pygame.Surface((TILE_MAPSIZE[0]*TILE_SIZE, TILE_MAPSIZE[1]*TILE_SIZE))
for event in eventList:
    event_image = event.event_image(event_image)

keyLeft = False
keyRight = False
keyLeft2 = False
keyRight2 = False

player_sponOK = True
player2_sponOK = True

camera_scroll = [player_spawn_x * TILE_SIZE-WINDOW_SIZE[0]/2, player_spawn_y * TILE_SIZE-WINDOW_SIZE[1]/2]

player_rect = pygame.Rect((player_spawn_x * TILE_SIZE, player_spawn_y * TILE_SIZE), (6,14))
player_movement = [0,0]
player_vspeed = 0
player_flytime = 0

player2_rect = pygame.Rect((player_spawn_x * TILE_SIZE+8, player_spawn_y * TILE_SIZE), (6,14))
player2_movement = [0,0]
player2_vspeed = 0
player2_flytime = 0

player_action = "stay"
player_frame = 0
player_frameSpeed = 1
player_frameTimer = 0
player_flip = False
player_animationMode = True
player_walkSoundToggle = False
player_walkSoundTimer = 0

player2_action = "stay"
player2_frame = 0
player2_frameSpeed = 1
player2_frameTimer = 0
player2_flip = False
player2_animationMode = True
player2_walkSoundToggle = False
player2_walkSoundTimer = 0

camera_scroll_standard = 1


while True:
    screen_scaled.fill(BACKGROUND_COLOR)
    
    if(camera_scroll_standard == 1):
        camera_scroll[0] += int((player_rect.x - camera_scroll[0] - WINDOW_SIZE[0] / 8 - 5) / 16)       # 카메라 이동
        camera_scroll[1] += int((player_rect.y - camera_scroll[1] - WINDOW_SIZE[1] / 8 - 2) / 16)
    else:
        camera_scroll[0] += int((player2_rect.x - camera_scroll[0] - WINDOW_SIZE[0] / 8 - 5) / 16)       # 카메라 이동
        camera_scroll[1] += int((player2_rect.y - camera_scroll[1] - WINDOW_SIZE[1] / 8 - 2) / 16)

    #screen_scaled.blit(backImage, (0,0))
    screen_scaled.blit(mapImage, (-camera_scroll[0], -camera_scroll[1]))
        

    #  플레이어 1 컨트롤
    player_movement = [0,0]
    if keyLeft:
        player_movement[0] -= PLAYER_ROWSPEED
    if keyRight:
        player_movement[0] += PLAYER_ROWSPEED
    player_movement[1] += player_vspeed

    player_vspeed += PLAYER_COLACCELERATE
    if player_vspeed > PLAYER_MAXCOLSPEED:
        player_vspeed = PLAYER_MAXCOLSPEED
    
    if player_movement[0] != 0:
        if player_flytime == 0:
            player_frame, player_action, player_frameSpeed, player_animationMode = change_player_action(
                player_frame, player_action, 'run', player_frameSpeed, 3, player_animationMode, True
            )
        
        if player_movement[0] > 0:
            player_flip = False
        else:
            player_flip = True
    else:
        if player_flytime == 0:
            player_frame, player_action, player_frameSpeed, player_animationMode = change_player_action(
                player_frame, player_action, 'stay', player_frameSpeed, 3, player_animationMode, True
                )

    player_rect, player_collision = move(player_rect, player2_rect, player_movement)
    if player_collision["bottom"]:
        player_vspeed = 0
        player_flytime = 0
    else:
        player_flytime += 1

    if player_collision["top"]:
        player_vspeed = 0
    
    
    player_frameTimer += 1
    if player_frameTimer >= player_frameSpeed:
        player_frame += 1
        player_frameTimer = 0

        if player_frame >= len(spr_player[player_action]):
            if player_animationMode == True:
                player_frame = 0
            else:
                player_frame -= 1
    
    screen_scaled.blit(pygame.transform.flip(spr_player[player_action][player_frame], player_flip, False)
                        , (player_rect.x - camera_scroll[0]-5, player_rect.y-camera_scroll[1]-2))

    #  플레이어 2 컨트롤
    player2_movement = [0,0]
    if keyLeft2:
        player2_movement[0] -= PLAYER_ROWSPEED
    if keyRight2:
        player2_movement[0] += PLAYER_ROWSPEED
    player2_movement[1] += player2_vspeed

    player2_vspeed += PLAYER_COLACCELERATE
    if player2_vspeed > PLAYER_MAXCOLSPEED:
        player2_vspeed = PLAYER_MAXCOLSPEED
    
    if player2_movement[0] != 0:
        if player2_flytime == 0:
            player2_frame, player2_action, player2_frameSpeed, player2_animationMode = change_player_action(
                player2_frame, player2_action, 'run', player2_frameSpeed, 3, player2_animationMode, True
            )
        
        if player2_movement[0] > 0:
            player2_flip = False
        else:
            player2_flip = True
    else:
        if player2_flytime == 0:
            player2_frame, player2_action, player2_frameSpeed, player2_animationMode = change_player_action(
                player2_frame, player2_action, 'stay', player2_frameSpeed, 3, player2_animationMode, True
                )

    player2_rect, player2_collision = move(player2_rect, player_rect, player2_movement)
    if player2_collision["bottom"]:
        player2_vspeed = 0
        player2_flytime = 0
    else:
        player2_flytime += 1

    if player2_collision["top"]:
        player2_vspeed = 0
    
    
    player2_frameTimer += 1
    if player2_frameTimer >= player2_frameSpeed:
        player2_frame += 1
        player2_frameTimer = 0

        if player2_frame >= len(spr_player2[player2_action]):
            if player2_animationMode == True:
                player2_frame = 0
            else:
                player2_frame -= 1

    screen_scaled.blit(pygame.transform.flip(spr_player2[player2_action][player2_frame], player2_flip, False)
                        , (player2_rect.x - camera_scroll[0]-5, player2_rect.y-camera_scroll[1]-2))
    
    #screen_scaled.blit(mapImage_front, (-camera_scroll[0], -camera_scroll[1]))

    # 이벤트 관리
    eventFlag = False
    for event in eventList:        
        nowFlag = event.perceive(player_rect, player2_rect)
        if(nowFlag):
            eventFlag = True
            event_image = event.event_image(event_image)
    event_image.set_colorkey((0,0,0))
    screen_scaled.blit(event_image,(-camera_scroll[0], -camera_scroll[1]))
    if(eventFlag):
        mapImage = mapManager.create_map_image()

    # 키 입력
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            #player1
            if event.key == K_a:
                keyLeft = True
            if event.key == K_d:
                keyRight = True
            if event.key == K_w and player_flytime < 6:
                player_vspeed = -3.5
                player_flytime += 1
                player_frame, player_action, player_frameSpeed,player_animationMode = change_player_action(
                    player_frame, player_action, "jump", player_frameSpeed, 6, player_animationMode, False
                )
            #player2
            if event.key == K_LEFT:
                keyLeft2 = True
            if event.key == K_RIGHT:
                keyRight2 = True
            if event.key == K_UP and player2_flytime < 6:
                player2_vspeed = -3.5
                player2_flytime += 1
                player2_frame, player2_action, player2_frameSpeed,player2_animationMode = change_player_action(
                    player2_frame, player2_action, "jump", player2_frameSpeed, 6, player2_animationMode, False
                )

            #public
            if event.key == K_q:
                if(camera_scroll_standard==1):
                    camera_scroll_standard=2
                else:
                    camera_scroll_standard=1

        if event.type == KEYUP:
            #player1
            if event.key == K_a:
                keyLeft = False
            if event.key == K_d:
                keyRight = False
            #player2
            if event.key == K_LEFT:
                keyLeft2 = False
            if event.key == K_RIGHT:
                keyRight2 = False

        if TESTMODE :
            if event.type == KEYDOWN:
                if(event.key == K_F3):
                    if(camera_scroll_standard==1):
                        print("player:",player_rect.x//8, player_rect.y//8+1)
                    else:
                        print("player:",player2_rect.x//8, player2_rect.y//8+1)
                if(event.key == K_F4):
                    print("mouse:",(camera_scroll[0]+pygame.mouse.get_pos()[0]//4)//8,(camera_scroll[1]+pygame.mouse.get_pos()[1]//4)//8)
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if camera_scroll_standard == 1 :
                    player_rect.x = camera_scroll[0]+pygame.mouse.get_pos()[0]//4
                    player_rect.y = camera_scroll[1]+pygame.mouse.get_pos()[1]//4
                if camera_scroll_standard == 2 :
                    player2_rect.x = camera_scroll[0]+pygame.mouse.get_pos()[0]//4
                    player2_rect.y = camera_scroll[1]+pygame.mouse.get_pos()[1]//4

    
    surf = pygame.transform.scale(screen_scaled, WINDOW_SIZE)
    screen.blit(surf,(0,0))
    
    # script text
    for script in scriptEventList:
        if(script.scriptText.is_show()):
            screen.blit(script.scriptText.image,(0,0))

    pygame.display.update()
    clock.tick(60)