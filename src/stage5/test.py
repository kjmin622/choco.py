import stage5
import pygame

pad_size = (1024,768)

pygame.init()
screen = pygame.display.set_mode(pad_size)
clock = pygame.time.Clock()
stage5.main(stage5.init(screen,clock))
