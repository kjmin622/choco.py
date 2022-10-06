import os
import pygame

def stage2_init(screen, clock):
    # 게임에 공통적으로 쓰이는 클래스 가져오기
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

    # 게임 내부 변수값
    is_right = False
    is_left = False
    is_clear = False
    is_arrive = False
    is_stage_clear = False

    # 색깔 코드값
    GROUND_COLOR = (147, 171, 248)
    PLATFORM_COLOR = (255, 255, 100)

    # 경로 모음
    DIR_PATH = os.path.dirname(__file__)
    DIR_SOUND = os.path.join(DIR_PATH, "sound")
    DIR_FONT = os.path.join(DIR_PATH, "font")
    DIR_IMAGE = os.path.join(DIR_PATH, "bg_image")
    BG1_IMAGE = os.path.join(DIR_IMAGE, "bg1.jpeg")
    BG2_IMAGE = os.path.join(DIR_IMAGE, "bg2.jpg")
    SPRITE_IMAGE = os.path.join(DIR_PATH, "character")
    JUMP_SOUND_PATH = os.path.join(DIR_SOUND, "Jump.wav")
    BG_SOUND_PATH = os.path.join(DIR_SOUND, "BG.wav")

    # 사운드
    JUMP_SOUND = pygame.mixer.Sound(JUMP_SOUND_PATH)
    BG_SOUND = pygame.mixer.Sound(BG_SOUND_PATH)

    #폰트
    FONT = os.path.join(DIR_FONT, "Sunflower-Medium.ttf")
    main_font_30 = pygame.font.Font(FONT ,30)
    main_font_50 = pygame.font.Font(FONT ,50)
    
    # 게임 백그라운드 이미지 로드 및 기본 백그라운드 이미지 설정
    bg1 = pygame.image.load(BG1_IMAGE)
    bg2 = pygame.image.load(BG2_IMAGE)
    bg = bg1

    return {'screen':screen, 'clock':clock,'vec':vec, 'HEIGHT':HEIGHT, 'WIDTH':WIDTH, 'BORDER_RIGHT':BORDER_RIGHT, 'BORDER_LEFT':BORDER_LEFT, 'FPS':FPS, 'ACC':ACC, 
    'FRIC':FRIC, 'is_arrive':is_arrive, 'is_stage_clear':is_stage_clear, 'is_right':is_right,'is_left':is_left, 'is_clear':is_clear, 'GROUND_COLOR':GROUND_COLOR, 
    'PLATFORM_COLOR':PLATFORM_COLOR, 'DIR_PATH':DIR_PATH, 'BG1_IMAGE':BG1_IMAGE, 'BG2_IMAGE':BG2_IMAGE, 'SPRITE_IMAGE':SPRITE_IMAGE, 'JUMP_SOUND':JUMP_SOUND, 
    'FONT':FONT, 'BG_SOUND':BG_SOUND, 'main_font_30':main_font_30, 'main_font_50':main_font_50,'bg2':bg2, 'bg':bg}




