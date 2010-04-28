'''Tetris Math by Joe Schafer and Monte Hoover
'''
import logging
import pygame
from pygame.locals import *
from game_controller import GameController

LOG_FILENAME = "tetrisMath.log"
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG)
def main():

    
    pygame.init()
    screen = pygame.display.set_mode ((1024, 768), SWSURFACE)
    pygame.display.set_caption('Tetris Math')

    clock = pygame.time.Clock()
    MAX_FPS = 80
    controller = GameController(screen)

    try:
        while controller.running:
                controller.update()
                controller.draw()
                clock.tick(MAX_FPS)
    except:
        traceback.print_exc(file=(open(LOG_FILENAME, "a")))
    finally:
        exit(1)
if __name__ == '__main__':
    main()
