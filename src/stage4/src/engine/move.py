import pygame, os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from data.constant import *


# 바닥과 충돌 검사 함수
def collision_floor(rect, mapdocumant):
    hit_list = []
    for (row,col) in mapdocumant["tile"]:
        floor_rect = pygame.rect.Rect((row * TILE_SIZE, col * TILE_SIZE), (TILE_SIZE, TILE_SIZE))
        if rect.colliderect(floor_rect):
            hit_list.append(floor_rect)

    return hit_list

def collision_object(rect1, rect2):
    if(rect1.colliderect(rect2)):
        return True
    return False

# 오브젝트 이동
def move(rect, otherRect, movement, mapdocumant):
    collision_types = {'top': False, 'bottom': False, "right": False, "left": False}
    rect.x += movement[0]
    hit_list = collision_floor(rect,mapdocumant)
    if(collision_object(rect, otherRect)):
        hit_list.append(otherRect)

    for tile in hit_list:
        org_left = rect.left
        org_right = rect.right
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types["left"] = True
    
    rect.y += movement[1]
    hit_list = collision_floor(rect,mapdocumant)
    if(collision_object(rect, otherRect)):
        hit_list.append(otherRect)

    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types["bottom"] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types["top"] = True
    
    return rect, collision_types