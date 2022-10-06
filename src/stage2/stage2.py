import pygame
from pygame.locals import *
import os
import sys
import random
import init

def stage2_init(screen,clock):
    return init.stage2_init(screen,clock)

def stage2_main(param):
    # 스테이지에 필요한 초기 값들을 stage2_init을 통해 생성하고 딕셔너리 형태로 받음
    screen=param['screen']; clock=param['clock']; vec=param['vec']; HEIGHT=param['HEIGHT']; WIDTH=param['WIDTH']; 
    BORDER_RIGHT=param['BORDER_RIGHT']; BORDER_LEFT=param['BORDER_LEFT']; FPS=param['FPS']; ACC=param['ACC']; FRIC=param['FRIC']; 
    is_arrive=param['is_arrive']; is_stage_clear=param['is_stage_clear']; is_right=param['is_right']; is_left=param['is_left'];
    GROUND_COLOR=param['GROUND_COLOR']; PLATFORM_COLOR=param['PLATFORM_COLOR']; SPRITE_IMAGE=param['SPRITE_IMAGE'];
    JUMP_SOUND=param['JUMP_SOUND']; BG_SOUND=param['BG_SOUND']; 
    main_font_30=param['main_font_30']; main_font_50=param['main_font_50']; bg2=param['bg2']; bg=param['bg']

    # 게임 스프라이트 시트를 게임 내부에서 사용할 수 있도록 자르는 클래스
    class SpriteSheet:

        # 파일이름, 캐릭터의 가로 크기, 캐릭터의 새로 크기, 최대 행의 크기, 최대 열의 크기, 마지막 캐릭터의 인덱스
        def __init__(self, filename, width, height, max_row, max_col, max_index):
            baseImage = pygame.image.load(os.path.join(SPRITE_IMAGE, filename)).convert()
            self.spr = []
            self.width = width
            self.height = height

            # 스프라이트 시트의 각 인덱스에 자른 이미지 저장
            for i in range(max_index):
                image = pygame.Surface((width, height))
                image.blit(baseImage, (0, 0), 
                        ((i % max_row) * width, (i // max_col) * height, width, height))
                image.set_colorkey((0, 0, 0))
                img = pygame.transform.scale(image, (64, 64))
                self.spr.append(img)


    # 게임 캐릭터의 기본 설정 클래스
    class Player(pygame.sprite.Sprite):

        # 게임 캐릭터 기본 설정 메서드
        def __init__(self):
            super().__init__() 

            # 게임 캐릭터 이미지 가져오기
            self.origin = SpriteSheet('character_new.png', 16, 16, 8, 8, 12)
            self.player_idle = self.origin.spr[0]
            self.player_right = self.origin.spr

            # 게임 캐릭터 기본 이미지, 중심 위치 설정
            self.rect = self.player_idle.get_rect()
            self.rect.center = (WIDTH / 2, HEIGHT - 16)
            self.surf = self.origin.spr[0]

            # 게임 캐릭터 - 왼쪽 모습 애니메이션 생성
            self.player_left = []
            for i in self.origin.spr:
                self.player_left.append(pygame.transform.flip(i, True, False))

            # 게임 캐릭터 위치, 속도, 가속도 등 인스턴스 변수 생성
            self.pos = vec((WIDTH / 2, HEIGHT - 16))
            self.vel = vec(0,0)
            self.acc = vec(0,0)
            self.jumping = False
            self.score = 0
            self.walk_cnt = 0


        # 캐릭터 움직임과 관련된 메서드
        def move(self):
            
            # 캐릭터 에니메이션을 위한 카운터
            if self.walk_cnt > 10:
                self.walk_cnt = 0

            # 캐릭터 기본 가속도
            self.acc = vec(0,0.5)
        
            # 키보드 좌우 방향키 감지 후 가속도 반영
            if is_right:
                self.surf = self.player_right[self.walk_cnt]
                self.walk_cnt += 1
                self.acc.x = ACC
            elif is_left:
                self.surf = self.player_left[self.walk_cnt]
                self.walk_cnt += 1
                self.acc.x = -ACC
            else:
                self.surf = self.player_idle

            # 마찰력 반영         
            self.acc.x += self.vel.x * FRIC
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc
            
            # 캐릭터가 범위를 좌우 범위를 넘어갈때 처리
            if self.pos.x > WIDTH:
                self.pos.x = WIDTH
            if self.pos.x < 0:
                self.pos.x = 0
                
            self.rect.midbottom = self.pos
    
    
        # 캐릭터 점프 메서드
        def jump(self): 
            hits = pygame.sprite.spritecollide(self, platforms, False)
            # 발판을 닫고 점프 상태가 아닐때만 점프, 이렇게 안하면 공중에서 계속 점프함
            if hits and not self.jumping:
                JUMP_SOUND.play()
                self.jumping = True
                self.vel.y = -20
        
        # 빠르게 원래 상태로 돌아오기 위한 메서드
        def cancel_jump(self):
            if self.jumping:
                if self.vel.y < -3:
                    self.vel.y = -3
    
        # 캐릭터가 발판에 닿았을때 멈추도록 하는 메서드
        def update(self):
            hits = pygame.sprite.spritecollide(self ,platforms, False)
            if self.vel.y > 0:        
                if hits:
                    if self.pos.y < hits[0].rect.bottom:
                        if hits[0].point == True:   
                            hits[0].point = False   
                            self.score += 1          
                        self.pos.y = hits[0].rect.top +1
                        self.vel.y = 0
                        self.jumping = False
    
    # 발판 생성과 움직임에 관한 클래스
    class Platform(pygame.sprite.Sprite):
        # 첫 화면 발판 랜덤 생성 
        def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((random.randint(80, 120), 12))
            self.surf.fill((PLATFORM_COLOR))
            self.rect = self.surf.get_rect(center = (random.randint(BORDER_LEFT + 60, BORDER_RIGHT - 60),
                                                    random.randint(150, HEIGHT - 100)))
            self.speed = random.randint(-1, 1)
            
            self.point = True   
            self.moving = True
            
        
        # 발판 움직임 함수
        def move(self):
            if self.moving == True:  
                self.rect.move_ip(self.speed,0)
                if self.speed > 0 and self.rect.right > BORDER_RIGHT:
                    self.speed = -self.speed
                if self.speed < 0 and self.rect.left < BORDER_LEFT:
                    self.speed = -self.speed


    # 발판 생성할때 겹치는 것 없이 생성하기 위한 함수
    def check(Platform, groupies):
        if pygame.sprite.spritecollideany(Platform,groupies):
            return True
        else:
            for entity in groupies:
                if entity == Platform:
                    continue
                if (abs(Platform.rect.top - entity.rect.top) < 50):
                    return True
            C = False

    # 첫 화면 이후의 발판 랜덤 생성
    def plat_gen():
        while len(platforms) < 7:
            p  = Platform()      
            C = True
            
            while C:
                p = Platform()
                p.rect.center = (random.randrange(BORDER_LEFT + 60, BORDER_RIGHT - 60),
                                random.randrange(-150 , -10))
                
                C = check(p, platforms)
            platforms.add(p)
            all_sprites.add(p)

    # 백그라운드 음악 재생
    BG_SOUND.play(-1)

    # 발판과 플레이어 인스턴스화 후 세부값 설정        
    PT1 = Platform()
    P1 = Player()
    
    PT1.surf = pygame.Surface((WIDTH, 20))
    PT1.surf.fill((GROUND_COLOR))
    PT1.rect = PT1.surf.get_rect(center = (WIDTH / 2, HEIGHT - 10))
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(PT1)
    all_sprites.add(P1)
    
    platforms = pygame.sprite.Group()
    platforms.add(PT1)

    PT1.moving = False
    PT1.point = False

    # 첫 화면에 보이는 발판 생성
    for x in range(random.randint(4,5)):
        C = True
        pl = Platform()
        while C:
            pl = Platform()
            C = check(pl, platforms)
        platforms.add(pl)
        all_sprites.add(pl)
    
    # 키보드 입력 부분 
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    is_right = True
                    is_left = False
                if event.key == pygame.K_LEFT:
                    is_right = False
                    is_left = True
                if event.key == pygame.K_SPACE:
                    P1.jump()
                if event.key == pygame.K_RETURN and is_arrive == True:
                    return True

            if event.type == pygame.KEYUP:   
                if event.key == pygame.K_RIGHT:
                    is_right = False
                    is_left = False
                if event.key == pygame.K_LEFT:
                    is_right = False
                    is_left = False
                if event.key == pygame.K_SPACE:
                    P1.cancel_jump()


        # 화면 아래보다 내려가면 게임오버
        if P1.rect.top > HEIGHT:
            BG_SOUND.stop()
            stage2_main(param)
            return True
             
            
        # 화면 움직임과 발판 회수
        if P1.rect.top <= HEIGHT / 2 and is_arrive != True:
            P1.pos.y += abs(P1.vel.y)
            for plat in platforms:
                plat.rect.y += abs(P1.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()

        # 목표지점 도달 시 도착 플레그 세우기
        if P1.score >= 20:
            is_arrive = True

        # 맨 위로 올라갔을떄 화면 맨 아래로 이동
        if P1.rect.top < 0:
            P1.pos = vec((P1.pos[0], 750))

        # 플레이어가 목표지점에 도달하지 않았을때 발판 생성
        if is_arrive == False:
            plat_gen()

        # 플레이어가 목표지점 도착시 발판을 없애고, 도착 지점 발판을 생성함
        if P1.rect.top < 0 and is_arrive == True:
            BG_SOUND.stop()
            bg = bg2
            for plat in platforms:
                plat.kill()

            p = Platform()
            p.surf = pygame.Surface((512, 12))
            p.rect = p.surf.get_rect(center = (512, 620))
            p.moving = False

            platforms.add(p)
            all_sprites.add(p)

        # 스테이지 클리어 여부를 체크            
        if bg == bg2 and P1.vel[1] == 0:
            is_stage_clear = True

    
        # 발판, 점수, 캐릭터를 화면에 그리는 부분
        screen.blit(bg, (0, 0))   

        # 클리어 시 클리어 문구를 띄우고 다음 행동을 안내
        if is_stage_clear:
            g  = main_font_50.render("클리어", True, (255,255,255))   
            screen.blit(g, (370, 150))

            g  = main_font_30.render("엔터키를 눌러 다음으로 이동", True, (255,255,255))   
            screen.blit(g, (370, 210))  
        
        # 모든 스프라이트를 갱신하는 부분
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
            entity.move()
        
        P1.update()

        # 화면에 업데이트된 것을 반영하는 부분
        pygame.display.update()

        # 화면 프레임 설정
        clock.tick(FPS)






