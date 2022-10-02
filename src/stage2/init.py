import os
import pygame

def stage2_init(screen, clock):
    screen = screen
    clock = clock
    vec = pygame.math.Vector2 #2 for two dimensional

    # 디스플레이 및 게임 화면 설정값
    HEIGHT = 768
    WIDTH = 1024
    BORDER_RIGHT = 768
    BORDER_LEFT = 256
    FPS = 60

    # 물리 인자값
    ACC = 0.6
    FRIC = -0.12

    # 게임 내부 상수값
    GEN_LIMIT = 7
    PLATFORM_GAP = 50
    PLATFORM_SIZE = 80
    ARRIVE = False
    STAGE_CLEAR = False

    # 게임 내부 변수값
    is_right = False
    is_left = False
    is_clear = False
    start_time = 0

    # 색깔 코드값
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GROUND_COLOR = (147, 171, 248)
    PLATFORM_COLOR = (255, 255, 100)

    # 경로 모음
    DIR_PATH = os.path.dirname(__file__)
    BG1_IMAGE = os.path.join(DIR_PATH, "bg_image/bg1.jpeg")
    BG2_IMAGE = os.path.join(DIR_PATH, "bg_image/bg2.jpg")
    SPRITE_IMAGE = os.path.join(DIR_PATH, "character")
    JUMP_SOUND_PATH = os.path.join(DIR_PATH, "sound/Jump.wav")
    BG_SOUND_PATH = os.path.join(DIR_PATH, "sound/bg.mp3")

    # 사운드
    JUMP_SOUND = pygame.mixer.Sound(JUMP_SOUND_PATH)
    BG_SOUND = pygame.mixer.Sound(BG_SOUND_PATH)

    #폰트
    FONT = os.path.join(DIR_PATH, "font/Sunflower-Medium.ttf")


    return {'screen':screen, 'clock':clock,'vec':vec, 'HEIGHT':HEIGHT, 'WIDTH':WIDTH, 'BORDER_RIGHT':BORDER_RIGHT, 'BORDER_LEFT':BORDER_LEFT, 'FPS':FPS, 'ACC':ACC, 'FRIC':FRIC, 'GEN_LIMIT':GEN_LIMIT, 'PLATFORM_GAP':PLATFORM_GAP, 'PLATFORM_SIZE':PLATFORM_SIZE, 'ARRIVE':ARRIVE, 'STAGE_CLEAR':STAGE_CLEAR, 'is_right':is_right, 'is_left':is_left, 'is_clear':is_clear, 'start_time':start_time, 'WHITE':WHITE, 'BLACK':BLACK, 'RED':RED, 'GROUND_COLOR':GROUND_COLOR, 'PLATFORM_COLOR':PLATFORM_COLOR, 'DIR_PATH':DIR_PATH, 'BG1_IMAGE':BG1_IMAGE, 'BG2_IMAGE':BG2_IMAGE, 'SPRITE_IMAGE':SPRITE_IMAGE, 'JUMP_SOUND_PATH':JUMP_SOUND_PATH, 'JUMP_SOUND':JUMP_SOUND, 'FONT':FONT, 'BG_SOUND':BG_SOUND}