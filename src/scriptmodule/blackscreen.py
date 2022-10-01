from time import time
import pygame
from pygame.locals import *
from time import time

class BlackScreen:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock

    def start(self, second):
        now = time()    
        while((time()-now)<second):
            for event in pygame.event.get():
                if event.type == QUIT:
                    return False
            self.screen.fill((0,0,0))
            pygame.display.update()
            self.clock.tick(60)
        return True