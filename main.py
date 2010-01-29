'''Tetris Math by Joe Schafer and Monte Hoover
'''

import pygame
from pygame.locals import *
from pygame.color import THECOLORS

import equation
import board

def main():
    WINDOW_SIZE = (640,480)
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE, flags=0, depth=8)
    pygame.display.set_caption('Tetris Math')

    # set up the background surface
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    board = Board(*WINDOW_SIZE, background)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type is QUIT:
                running = False

            doProblems(screen, board)

if __name__ == '__main__':
    main()
