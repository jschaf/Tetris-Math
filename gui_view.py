'''A view for the Pygame gui.'''


import pygame
from pygame import Color
from pygame.locals import *
from equation import int_from_digits

class GuiView(object):
    '''The primary gui view.'''

    def __init__(self, board, screen):
        self.font = pygame.font.Font(None, 36)
        self.equation = None
        self.board = board
        self.screen = screen
        self.changed_eqn = True
        # set up the background surface
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.surface.fill((250, 250, 250))
                
    def update_eqn(self, new_eqn):
        self.equation = new_eqn
        self.changed_eqn = True
        
    def refresh(self):
        self.changed_eqn = True
        
    # draws the problem in the window and also puts it on the command line
    def draw(self, mode):
        if mode == "running":        
            if self.changed_eqn:
                self.changed_eqn = False
                # (text, smoothed(1=true), text RGB color)
                if self.board.current_input:
                    guess_num = int_from_digits(self.board.current_input)
                    eqn_render = self.equation.render(guess=guess_num)
                else:
                    eqn_render = self.equation.render()
                    
                text = self.font.render(eqn_render, 1, (31,73,125), (250,250,250))
                
                # clear the board and copy the rendered message onto it
                # (RGB color)
                self.surface.fill ((250, 250, 250))
                self.surface.blit(text, (130, 200)) #(x and y location)
                
                text_rect = pygame.Rect(120, 190, 130, 40)
                border = pygame.draw.rect(self.surface, Color('red'), text_rect, 1)
        elif mode == "summary":
            summary_string = "Summary:\nYou answered {0} of {1} problems correctly"
            text = self.font.render(summary_string.format(self.board.correct_tally, 
                                                          self.board.problem_count),
                                     1, (31,73,125), (250,250,250))
            self.surface.fill ((250, 250, 250))
            self.surface.blit(text, (130, 200))    
            
        self.screen.blit (self.surface, (0, 0))        
        pygame.display.flip()
    
    
    def clear_screen(self):
        self.surface.fill((250,250,250))
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()
