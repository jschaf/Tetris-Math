'''Tetris Math by Joe Schafer and Monte Hoover
'''

import pygame
from pygame.locals import *
from pygame.color import THECOLORS

import equation
import board
import gameController

def main():
    WINDOW_SIZE = (640,480)
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 8)
    pygame.display.set_caption('Tetris Math')

    board_model = board.Board(640, 480, screen)
    controller = gameController.GameController(board_model)

    running = True

    while running:
        controller.update(board_model)
        controller.draw()

if __name__ == '__main__':
    main()
