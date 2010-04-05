'''Tetris Math by Joe Schafer and Monte Hoover
'''

import pygame
from game_controller import GameController

def main():
    
    pygame.init()
    pygame.display.set_caption('Tetris Math')

    clock = pygame.time.Clock()
    MAX_FPS = 40
    controller = GameController()
    
    controller.running = True

    while controller.running:
        controller.update()
        controller.draw()
        clock.tick(MAX_FPS)

if __name__ == '__main__':
    main()
