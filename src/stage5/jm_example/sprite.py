import pygame, os
from constant import *

class SpriteSheet:
    """
        스프라이트 관련 클래스
        
        스프라이트 이미지를 불러와서 잘라 리스트에 저장함

        @Attributes:
            spr (list(pygame.Surface)): 스프라이트 이미지 리스트
            width (int): 스프라이트 이미지의 가로 크기
            height (int): 스프라이트 이미지의 세로 크기
        @Args:
            filename (str): 스프라이트 이미지 파일 이름
            width (int): 스프라이트 이미지의 가로 크기
            height (int): 스프라이트 이미지의 세로 크기
            max_row (int): 스프라이트 이미지의 가로 개수
            max_col (int): 스프라이트 이미지의 세로 개수   
            max_index (int): 스프라이트 이미지의 총 개수
    """

    def __init__(self, filename, width, height, max_row, max_col, max_index):
        baseImage = pygame.image.load(os.path.join(DIR_IMAGE,filename)).convert()
        self.spr = []
        self.width = width
        self.height = height

        for i in range(max_index):
            image = pygame.Surface((width,height))
            image.blit(baseImage, (0,0), ((i%max_row)*width, (i//max_col)*height,width,height))
            image.set_colorkey((0,0,0))
            self.spr.append(image)

def create_sprite_set(sprite_sheet, index_list):
    """
        SpriteSheet 클래스에 저장된 이미지의 특정 범위로 스프라이트 이미지 리스트를 만드는 함수

        @Args:
            sprite_sheet (SpriteSheet): SpriteSheet 클래스
            index_list (list(int)): 스프라이트 이미지 리스트의 인덱스 범위
        @Returns:
            list(pygame.Surface): 스프라이트 이미지 리스트
    """
    spr = []
    for index in index_list:
        spr.append(sprite_sheet.spr[index])
    
    return spr