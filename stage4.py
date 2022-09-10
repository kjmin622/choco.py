import pygame, sys, os
from datafile import *
from pygame.locals import *
import pygame.mixer


pygame.init()
pygame.mixer.init()

#게임 컨트롤 변수
pygame.display.set_caption('stage4')                                      # 창 이름 설정
clock = pygame.time.Clock()

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
screen_scaled = pygame.Surface((WINDOW_SIZE[0] / 4, WINDOW_SIZE[1] / 4))        # 확대한 스크린

camera_scroll = [TILE_MAPSIZE[0] * 4, 0]              # 카메라 이동 좌표

# 리소스 불러오기
spriteSheet_player = SpriteSheet('character.png', 16, 16, 8, 8, 12)      # 플레이어 스프라이트 시트
spriteSheet_object = SpriteSheet('spriteSheet2.png', 8, 8, 16, 16, 45)      # 공통 오브젝트 스프라이트 시트
spriteSheet_map1 = SpriteSheet('map1.png', 8, 8, 16, 16, 87)         # 지형 1 스프라이트 시트

spr_player = {}     # 플레이어 스프라이트 세트
spr_player['stay'] = createSpriteSet(spriteSheet_player, [0])
spr_player['run'] = createSpriteSet(spriteSheet_player, 1, 8)
spr_player['jump'] = createSpriteSet(spriteSheet_player, [9, 10, 11])

spr_effect = {}     # 효과 스프라이트 세트
spr_effect['player_shot'] = createSpriteSet(spriteSheet_object, 37, 40)          
spr_effect['player_shotBoom'] = createSpriteSet(spriteSheet_object, 41, 44)

spr_enemy = {}      # 적 스프라이트 세트
spr_map_struct = {}     # 구조물 스프라이트 세트

spr_enemy['slime'] = createSpriteSet(spriteSheet_map1, 81, 83)          
spr_enemy['snake'] = createSpriteSet(spriteSheet_map1, 84, 86)

spr_map_struct['leaf'] = [55, 56]
spr_map_struct['flower'] = [57, 64]
spr_map_struct['obj'] = [65, 70]
spr_map_struct['sign'] = [71, 74]
spr_map_struct['gravestone'] = [75, 78]
spr_map_struct['skull'] = [79, 80]

createMapData()                                 # 맵 데이터 초기화
mapImage, mapImage_front = createMapImage(spriteSheet_map1, spr_map_struct) # 맵 이미지 생성
backImage = createBackImage(spriteSheet_object)         # 배경 이미지 생성

#효과음
sound_attack = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'attack.wav'))
sound_coin = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'coin.wav'))
sound_footstep0 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep0.wav'))
sound_footstep1 = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'footstep1.wav'))
sound_monster = pygame.mixer.Sound(os.path.join(DIR_SOUND, 'monster.wav'))

# 적 생성
"""
for i in range(8):
obj_snake = createObject(spr_enemy['snake'], (random.randrange(0, 960), 100), 'snake', self)
obj_snake = createObject(spr_enemy['slime'], (random.randrange(0, 960), 100), 'slime', self)
"""

# 플레이어 컨트롤 변수
keyLeft = False
keyRight = False

player_sponOK = True
player_spon_x = TILE_MAPSIZE[0] // 2 - 1


player_rect = pygame.Rect((player_spon_x * 8, TILE_MAPSIZE[1] * 4 - 14), (6, 14))  # 플레이어 히트박스
player_movement = [0, 0]            # 플레이어 프레임당 속도
player_vspeed = 0                   # 플레이어 y가속도
player_flytime = 0                  # 공중에 뜬 시간

player_action = 'stay'              # 플레이어 현재 행동
player_frame = 0                    # 플레이어 애니메이션 프레임
player_frameSpeed = 1               # 플레이어 애니메이션 속도(낮을 수록 빠름. max 1)
player_frameTimer = 0
player_flip = False                 # 플레이어 이미지 반전 여부 (False: RIGHT)
player_animationMode = True         # 애니메이션 모드 (False: 반복, True: 한번)
player_walkSoundToggle = False
player_walkSoundTimer = 0

player_attack_timer = 0             # 플레이어 공격 타이머
player_attack_speed = 15            # 플레이어 공격 속도

# 배경음 실행
pygame.mixer.music.load(os.path.join(DIR_SOUND, 'background.wav'))
pygame.mixer.music.play(loops = -1)

# 메인 루프
while True:
    screen_scaled.fill(BACKGROUND_COLOR)            # 화면 초기화

    camera_scroll[0] += int((player_rect.x - camera_scroll[0] - WINDOW_SIZE[0] / 8 - 5) / 16)       # 카메라 이동
    camera_scroll[1] += int((player_rect.y - camera_scroll[1] - WINDOW_SIZE[1] / 8 - 2) / 16)

    screen_scaled.blit(backImage, (0, 0))                                   # 배경 드로우
    screen_scaled.blit(mapImage, (-camera_scroll[0], -camera_scroll[1]))    # 맵 드로우

    # 플레이어 컨트롤
    if player_attack_timer < player_attack_speed:
        player_attack_timer += 1
    player_movement = [0, 0]                       # 플레이어 이동
    if keyLeft:
        player_movement[0] -= 2
    if keyRight:
        player_movement[0] += 2
    player_movement[1] += player_vspeed

    player_vspeed += 0.2
    if player_vspeed > 3:
        player_vspeed = 3

    if player_movement[0] != 0:                  # 플레이어 걷기 애니메이션 처리 및 방향 전환
        if player_flytime == 0:
            player_frame, player_action, player_frameSpeed, player_animationMode = change_playerAction(
                player_frame, player_action, 'run', player_frameSpeed, 3, player_animationMode, True)

            player_walkSoundTimer += 1

            if player_walkSoundTimer > 1:
                player_walkSoundTimer = 0

                if player_walkSoundToggle:
                    player_walkSoundToggle = False
                    sound_footstep0.play()
                else:
                    player_walkSoundToggle = True
                    sound_footstep1.play()
        if player_movement[0] > 0:
            player_flip = False
        else:
            player_flip = True
    else:
        player_walkSoundTimer = 0

        if player_flytime == 0:
            player_frame, player_action, player_frameSpeed, player_animationMode = change_playerAction(
                player_frame, player_action, 'stay', player_frameSpeed, 3, player_animationMode, True)

    player_rect, player_collision = move(player_rect, player_movement)

    if player_collision['bottom']:
        player_vspeed = 0
        player_flytime = 0
    else:
        player_flytime += 1

    player_frameTimer += 1                          # 플레이어 애니메이션 타이머
    if player_frameTimer >= player_frameSpeed:
        player_frame +=1
        player_frameTimer = 0

        if player_frame >= len(spr_player[player_action]):
            if player_animationMode == True:
                player_frame = 0
            else:
                player_frame -= 1

    screen_scaled.blit(pygame.transform.flip(spr_player[player_action][player_frame], player_flip, False)
                        , (player_rect.x - camera_scroll[0] - 5, player_rect.y - camera_scroll[1] - 2))      # 플레이어 드로우

    for obj in objects:         # 오브젝트 이벤트 처리
        if obj.destroy:
            obj.destroy_self()
        else:
            obj.events()
            obj.draw()
            obj.physics_after()

    screen_scaled.blit(mapImage_front, (-camera_scroll[0], -camera_scroll[1]))    # 프론트 맵 드로우

    # 이벤트 컨트롤
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                keyLeft = True
            if event.key == K_RIGHT:
                keyRight = True
            if event.key == K_UP and player_flytime < 6:    # 점프
                player_vspeed = -3.5
                player_flytime += 1
            
                player_frame, player_action, player_frameSpeed, player_animationMode = change_playerAction(
                    player_frame, player_action, 'jump', player_frameSpeed, 6, player_animationMode, False)
            if event.key == K_SPACE and player_attack_timer >= player_attack_speed:        # 공격
                player_attack_timer = 0
                player_shot = createObject(spr_effect['player_shot'], (player_rect.x, player_rect.y + 2), 'player_shot')
                player_shot.direction = player_flip
                sound_attack.play()
        if event.type == KEYUP:
            if event.key == K_LEFT:
                keyLeft = False
            if event.key == K_RIGHT:
                keyRight = False

    surf = pygame.transform.scale(screen_scaled, WINDOW_SIZE)       # 창 배율 적용
    screen.blit(surf, (0, 0))

    pygame.display.update()
    clock.tick(60)