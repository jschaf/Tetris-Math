'''A view for the Pygame gui.'''


import pygame
from pygame.locals import *

class GuiView(object):
    '''The primary gui view.'''

    def __init__(self, board):
        self.font = pygame.font.Font(None, 36)
        self.equation = None

        # set up the background surface
        self.surface = pygame.Surface(screen.get_size())
        self.surface = background.convert()
        self.surface.fill((250, 250, 250))


    def update_equation(self, equation):
        self.equation = equation
        
    # draws the problem in the window and also puts it on the command line
    def draw(self):

        # (text, smoothed(1=true), text RGB color)
        text = font.render(self.equation.render(), 1, (31,73,125))

        # clear the board and copy the rendered message onto it
        # (RGB color)
        board.fill ((250, 250, 250))
        board.blit(text, (130, 200)) #(x and y location)

        self.surface.blit (board, (0, 0))
        pygame.display.flip()

