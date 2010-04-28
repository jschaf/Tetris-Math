'''Tetris Math by Joe Schafer and Monte Hoover
'''

import pygame
from pygame.locals import *
from game_controller import GameController

def main():
    
    pygame.init()
    screen = pygame.display.set_mode ((1024, 768), SWSURFACE)
    pygame.display.set_caption('Tetris Math')

    clock = pygame.time.Clock()
    MAX_FPS = 80
    controller = GameController(screen)

    while controller.running:
        controller.update()
        controller.draw()
        clock.tick(MAX_FPS)

if __name__ == '__main__':
    main()
