'''Tetris Math by Joe Schafer and Monte Hoover
'''

import pygame
from game_controller import GameController

def main():
    
    pygame.init()
    pygame.display.set_caption('Tetris Math')

    controller = GameController()

    controller.running = True

    while controller.running:        
        controller.update()
        controller.draw()
            
if __name__ == '__main__':
    main()
