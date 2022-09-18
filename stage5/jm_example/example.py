
import pygame
from sprite import *
from enemy import *

def example():
    """
        enemy 중심으로 생각한 예시 코드
        그냥 이렇게 구현하면 좋겠다 하면서 바로바로 떠오른 생각 정리한거라 
        생각해보고 더 좋은 방법 있으면 그걸로 가는게 맞음요!
    """

    # ...
    screen = "게임 스크린"
    # ...
    player_rect = "플레이어 rect 객체"
    # ...

    # enemy 스프라이트 시트 클래스 생성
    enemy_sprite_sheet = SpriteSheet("경로", 32, 32, 4, 4, 16)
    # ...

    # enemy1에게 적용할 sprite set
    enemy1_sprite = create_sprite_set(enemy_sprite_sheet, [0,1,2,3])
    # enemy2에게 적용할 sprite set
    enemy2_sprite = create_sprite_set(enemy_sprite_sheet, [4,5,6,7])
    # ...

    # enemy들을 담을 리스트
    enemy_list = []
    # ...

    while(True):
        # ...
        if("특정 조건문"):
            # ...
            enemy_list.append(
                Enemy(enemy1_sprite, pygame.rect.Rect(("특정 범위의 랜덤 (int)x","특정 범위의 랜덤 (int)y"),(32,32),(0,5)))
            )
        # ...
        if("특정 조건문"):
            # ...
            enemy_list.append(
                Enemy(enemy2_sprite, pygame.rect.Rect(("특정 범위의 랜덤 (int)x","특정 범위의 랜덤 (int)y"),(32,32),(0,10)))
            )
        # ...
        for enemy in enemy_list:
            enemy.move("장애물 x축 속도","장애물 y축 속도")
            # ...
            if(enemy.is_collide(player_rect)):
                pass # 플레이어가 객체에 충돌했을 때의 처리
            # ...
            if(enemy.is_nonvisiable()):
                enemy_list.remove(enemy)
            else:
                screen.blit(enemy.get_now_sprite(), enemy.get_location())
        # ...
        