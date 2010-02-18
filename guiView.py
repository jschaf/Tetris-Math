'''A view for the Pygame gui.'''


import pygame
from pygame.locals import *
import equation

class GuiView(object):
    '''The primary gui view.'''

    def __init__(self, board):
        self.font = pygame.font.Font(None, 36)
        self.equation = equation.Equation(0)
        
        self.screen = pygame.display.set_mode((400,450))
        self.font = pygame.font.Font(None, 36)

        # set up the background surface
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.surface.fill((250, 250, 250))


    def update_equation(self, equation):
        self.equation = equation
        
    # draws the problem in the window and also puts it on the command line
    def draw(self):

        # (text, smoothed(1=true), text RGB color)
        text = self.font.render(self.equation.render(), 1, (31,73,125))

        # clear the board and copy the rendered message onto it
        # (RGB color)
        self.surface.fill ((250, 250, 250))
        self.surface.blit(text, (130, 200)) #(x and y location)

        self.surface.blit (self.surface, (0, 0))
        pygame.display.flip()

