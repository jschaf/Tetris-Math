'''A view for the Pygame gui.'''


import pygame
from pygame import Color
from pygame.locals import *
from equation import int_from_digits

class GuiView(object):
    '''The primary gui view.'''
    
    white = (250,250,250)
    teal = (31,73,125)

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
        if mode == "welcome":
            self._draw_welcome()

        elif mode == "running":        
            self._draw_running()

        elif mode == "summary":
            summary_string = "You answered {0} of {1} problems correctly"
            text = self.font.render(summary_string.format(self.board.correct_tally, 
                                                          self.board.problem_count),
                                     1, (31,73,125), (250,250,250))
            self.surface.fill ((250, 250, 250))
            self.surface.blit(text, (130, 200))    
            
        self.screen.blit (self.surface, (0, 0))        
        pygame.display.flip()
    
    def _draw_welcome(self):
        welcome_msg = self.font.render("Welcome to Tetris Math", 1, (31,73,125), (250,250,250))
        instruction = self.font.render("Press a number from the options below:", 1, (31,73,125), (250,250,250))
        choice1 = self.font.render("1. Single Player", 1, (31,73,125), (250,250,250))
        choice2 = self.font.render("2. Multi Player", 1, (31,73,125), (250,250,250))
        choice3 = self.font.render("3. Practice Quiz", 1, (31,73,125), (250,250,250))
        self.surface.fill ((250, 250, 250))
        self.surface.blit(welcome_msg, (130, 200))
        self.surface.blit(instruction, (130, 240))
        self.surface.blit(choice1, (130, 270))
        self.surface.blit(choice2, (130, 300))
        self.surface.blit(choice3, (130, 330))

    def _draw_running(self):
        # if self.changed_eqn:
        if self.board.current_input:
            guess_num = int_from_digits(self.board.current_input)
            eqn_render = self.equation.render(guess=guess_num)
            print(eqn_render)
        else:
            eqn_render = self.equation.render()

        # (text, smoothed(1=true), text RGB color)    
        text = self.font.render(eqn_render, 1, (31,73,125), (250,250,250))

        # clear the board and copy the rendered message onto it
        self.changed_eqn = False

        self.surface.fill ((250, 250, 250))
        self.surface.blit(text, (30, self.board.current_eqn_position))

        text_rect = pygame.Rect(120, 190, 130, 40)
        border = pygame.draw.rect(self.surface, Color('red'), text_rect, 1)

    def clear_screen(self):
        self.surface.fill((250,250,250))
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()
