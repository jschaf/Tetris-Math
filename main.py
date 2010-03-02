'''Tetris Math by Joe Schafer and Monte Hoover
'''

import pygame
from pygame.locals import *

import board
import gameController

def main():
    WINDOW_SIZE = (640,480)
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE, 0, 8)
    pygame.display.set_caption('Tetris Math')

    board_model = board.Board(640, 480, screen)
    controller = gameController.GameController(board_model)

    controller.running = True

    while controller.running:        
        controller.update()
        controller.draw()
            
if __name__ == '__main__':
    main()
