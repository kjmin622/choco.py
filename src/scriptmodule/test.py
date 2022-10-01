import os, sys, pygame
from pygame.locals import *
import pygame.mixer
import script
import stage_start1
import stage_start2
import stage1_2
import stage2_3
import stage_end
import blackscreen
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

blackscreens = blackscreen.BlackScreen(screen, clock)

stage_start1.main(stage_start1.init(screen,clock))
blackscreens.start(1.5)
stage_start2.main(stage_start2.init(screen,clock))
blackscreens.start(1.5)
stage1_2.main(stage1_2.init(screen,clock))
blackscreens.start(1.5)
stage2_3.main(stage2_3.init(screen,clock))
blackscreens.start(1.5)
stage_end.main(stage_end.init(screen,clock))
blackscreens.start(15)
