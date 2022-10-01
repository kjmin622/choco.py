import os
from constant import *
import pygame

class Side:
    def __init__(self,objectlist,image,path = None):
        self.objectlist = objectlist
        self.image = pygame.image.load(os.path.join(DIR_IMAGE,image))
        self.path = path

def turn_right(now):
    next = now + 1
    if next == 4:
        next = 0
    return next
def turn_left(now):
    before = now - 1
    if before == -1:
        before = 3
    return before