import pygame, sys, os
from funcs import *
from pygame.locals import *
import pygame.mixer



pygame.init()
pygame.mixer.init()

#
pygame.display.set_caption("stage4")
clock = pygame.time.Clock()

screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
screen_scaled = pygame.Surface((WINDOW_SIZE[0]/4,WINDOW_SIZE[1]/4))

camera_scroll = [8, 0]

spriteSheet_player = SpriteSheet("character.png", 16,16,8,8,12)
spriteSheet_ground = SpriteSheet("ground.png",8,8,48,8,6)
spriteSheet_object = SpriteSheet("spriteSheet2.png", 8,8,16,16,45)
spriteSheet_map1 = SpriteSheet("map1.png",8,8,16,16,87)

spr_player = {}
spr_player["stay"] = createSpriteSet(spriteSheet_player, [0])
spr_player['run'] = createSpriteSet(spriteSheet_player, 1, 8)
spr_player['jump'] = createSpriteSet(spriteSheet_player, [9, 10, 11])

mapImage = createMapImage(spriteSheet_ground)

keyLeft = False
keyRight = False

player_sponOK = True
player_spon_x = 8

player_rect = pygame.Rect((player_spon_x * 8, TILE_MAPSIZE[1]*4-14), (6,14))
player_movement = [0,0]
player_vspeed = 0
player_flytime = 0

player_action = "stay"
player_frame = 0
player_frameSpeed = 1
player_frameTimer = 0
player_flip = False
player_animationMode = True
player_walkSoundToggle = False
player_walkSoundTimer = 0


while True:
    screen_scaled.fill(BACKGROUND_COLOR)

    camera_scroll[0] += int((player_rect.x - camera_scroll[0] - WINDOW_SIZE[0] / 8 - 5) / 16)       # 카메라 이동
    camera_scroll[1] += int((player_rect.y - camera_scroll[1] - WINDOW_SIZE[1] / 8 - 2) / 16)

    #screen_scaled.blit(backImage, (0,0))
    screen_scaled.blit(mapImage, (-camera_scroll[0], -camera_scroll[1]))

    #  플레이어 컨트롤
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
            player_frame, player_action, player_frameSpeed, player_animationMode = change_playerAction(
                player_frame, player_action, 'run', player_frameSpeed, 3, player_animationMode, True
            )
        
        if player_movement[0] > 0:
            player_flip = False
        else:
            player_flip = True
    else:
        if player_flytime == 0:
            player_frame, player_action, player_frameSpeed, player_animationMode = change_playerAction(
                player_frame, player_action, 'stay', player_frameSpeed, 3, player_animationMode, True
                )

    player_rect, player_collision = move(player_rect, player_movement)
    if player_collision["bottom"]:
        player_vspeed = 0
        player_flytime = 0
    else:
        player_flytime += 1

    # 천장 부딪히면 바로 떨어짐
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
    
    #screen_scaled.blit(mapImage_front, (-camera_scroll[0], -camera_scroll[1]))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                keyLeft = True
            if event.key == K_d:
                keyRight = True
            if event.key == K_w and player_flytime < 6:
                player_vspeed = -3.5
                player_flytime += 1

                player_frame, player_action, player_frameSpeed,player_animationMode = change_playerAction(
                    player_frame, player_action, "jump", player_frameSpeed, 6, player_animationMode, False
                )
        if event.type == KEYUP:
            if event.key == K_a:
                keyLeft = False
            if event.key == K_d:
                keyRight = False
    
    surf = pygame.transform.scale(screen_scaled, WINDOW_SIZE)
    screen.blit(surf,(0,0))

    pygame.display.update()
    clock.tick(60)