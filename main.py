import pygame, sys
from settings import *
from tiles import Tile
from level import Level

#region Pygame setup
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
#endregion

#region Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)
#endregion