import pygame

class Enemy():
    """
    장애물 관련 클래스

    시나리오//
    장애물 랜덤 생성 
    -> 장애물 리스트에 추가 
    -> 로직 돌아가는 while문 안에서 장애물 리스트 순환하며 장애물 이동, 이미지 출력, 충돌 처리 등
    -> 화면에서 사라질 시 장애물 리스트에서 삭제

    @Attributes:
        sprite (list(pygame.Surface)): 장애물의 이미지 리스트
        rect (pygame.Rect): 장애물의 위치와 크기
        speed (tuple(int,int)): 장애물의 이동 속도
        collided (bool): 충돌 여부
        _sprite_now (int): 현재 이미지 인덱스
        _sprite_max_index (int): 이미지 리스트의 최대 인덱스

    @Args:
        sprite (list(pygame.Surface)): 장애물의 이미지 리스트
        rect (pygame.Rect): 장애물의 위치와 크기를 담은 사각형
        speed (tuple(int,int)): 장애물의 이동 속도
    """
    def __init__(self, sprite, rect, speed):
        self.sprite = sprite
        self.rect = rect
        self.speed = speed
        self.collided = False
        self._sprite_now = 0
        self._sprite_max_index = len(self.sprite) - 1
    
    def get_location(self):
        return (self.rect.x, self.rect.y)
    
    def get_size(self):
        return (self.rect.width, self.rect.height)

    def get_now_sprite(self):
        return self.sprite[self._sprite_now]
    
    def next_sprite(self):
        self._sprite_now += 1
        if self._sprite_now > self._sprite_max_index:
            self._sprite_now = 0
    
    def move(self):
        # Write your code here
        pass

    def is_nonvisiable(self):
        # Write your code here
        pass

    def is_collide(self, rect):
        """
            충돌 여부를 반환하는 메소드
            이 객체가 이미 충돌했을 경우엔 실행 없이 False 반환.

            @Args:
                rect (pygame.Rect): 플레이어의 rect 객체
        """
        if not self.collided:
            collide = rect.colliderect(self.rect)
            if collide:
                self.collided = True
                return True
        return False
    


