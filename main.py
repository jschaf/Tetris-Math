'''Tetris Math by Joe Schafer and Monte Hoover
'''

import pygame
from pygame.locals import *
from pygame.color import THECOLORS

import equation

def main():
    WINDOW_SIZE = (640,480)
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 8)
    pygame.display.set_caption('Tetris Math')

if __name__ == '__main__':
    main()
