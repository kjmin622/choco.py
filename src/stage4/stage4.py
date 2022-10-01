import pygame, sys, os

from pygame.locals import *
import pygame.mixer

from src.data.constant import *
import src.data.globalvariable as g
from src.map.map import *
import src.data.eventdata as eventdata
import src.engine.sprite as sprite
import src.event.button as button
import src.event.script as script
import src.engine.move as move
import initial.init as initial

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE))
clock = pygame.time.Clock()

def init(screen,clock):
    return initial.stage4_init(screen,clock)

def main(param):
    screen=param['screen'];clock=param['clock'];screen_scaled=param['screen_scaled'];spriteSheet_player=param['spriteSheet_player'];spriteSheet_player2=param['spriteSheet_player2'];spriteSheet_ground=param['spriteSheet_ground'];spriteSheet_object=param['spriteSheet_object'];spr_player=param['spr_player'];spr_player2=param['spr_player2'];mapManager=param['mapManager'];player_spawn_x=param['player_spawn_x'];player_spawn_y=param['player_spawn_y'];mapImage=param['mapImage'];endpoint_list=param['endpoint_list'];eventList=param['eventList'];scriptEventList=param['scriptEventList'];event_image=param['event_image'];keyLeft=param['keyLeft'];keyRight=param['keyRight'];keyLeft2=param['keyLeft2'];keyRight2=param['keyRight2'];player_sponOK=param['player_sponOK'];player2_sponOK=param['player2_sponOK'];camera_scroll=param['camera_scroll'];player_rect=param['player_rect'];player_movement=param['player_movement'];player_vspeed=param['player_vspeed'];player_flytime=param['player_flytime'];player2_rect=param['player2_rect'];player2_movement=param['player2_movement'];player2_vspeed=param['player2_vspeed'];player2_flytime=param['player2_flytime'];player_action=param['player_action'];player_frame=param['player_frame'];player_frameSpeed=param['player_frameSpeed'];player_frameTimer=param['player_frameTimer'];player_flip=param['player_flip'];player_animationMode=param['player_animationMode'];player_walkSoundToggle=param['player_walkSoundToggle'];player_walkSoundTimer=param['player_walkSoundTimer'];player2_action=param['player2_action'];player2_frame=param['player2_frame'];player2_frameSpeed=param['player2_frameSpeed'];player2_frameTimer=param['player2_frameTimer'];player2_flip=param['player2_flip'];player2_animationMode=param['player2_animationMode'];player2_walkSoundToggle=param['player2_walkSoundToggle'];player2_walkSoundTimer=param['player2_walkSoundTimer'];camera_scroll_standard=param['camera_scroll_standard']
    
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
                player_frame, player_action, player_frameSpeed, player_animationMode = sprite.change_player_action(
                    player_frame, player_action, 'run', player_frameSpeed, 3, player_animationMode, True
                )
            
            if player_movement[0] > 0:
                player_flip = False
            else:
                player_flip = True
        else:
            if player_flytime == 0:
                player_frame, player_action, player_frameSpeed, player_animationMode = sprite.change_player_action(
                    player_frame, player_action, 'stay', player_frameSpeed, 3, player_animationMode, True
                    )

        player_rect, player_collision = move.move(player_rect, player2_rect, player_movement, g.g_mapdocumant)
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
                player2_frame, player2_action, player2_frameSpeed, player2_animationMode = sprite.change_player_action(
                    player2_frame, player2_action, 'run', player2_frameSpeed, 3, player2_animationMode, True
                )
            
            if player2_movement[0] > 0:
                player2_flip = False
            else:
                player2_flip = True
        else:
            if player2_flytime == 0:
                player2_frame, player2_action, player2_frameSpeed, player2_animationMode = sprite.change_player_action(
                    player2_frame, player2_action, 'stay', player2_frameSpeed, 3, player2_animationMode, True
                    )

        player2_rect, player2_collision = move.move(player2_rect, player_rect, player2_movement, g.g_mapdocumant)
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

        # 게임이 끝났는가?
        for event in endpoint_list:
            if event.colliderect(player_rect) or event.colliderect(player2_rect):
                return True

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
                    player_frame, player_action, player_frameSpeed,player_animationMode = sprite.change_player_action(
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
                    player2_frame, player2_action, player2_frameSpeed,player2_animationMode = sprite.change_player_action(
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

main(init(screen,clock))