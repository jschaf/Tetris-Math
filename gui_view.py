'''A view for the Pygame gui.'''


import pygame
from pygame import Color
from pygame.locals import *
from pgu import gui
from equation import int_from_digits

class GuiView(object):
    '''The primary gui view.'''
    
    def __init__(self, board, screen):
        self.font = pygame.font.Font(None, 36)
        self.board = board
        self.screen = screen
        self.surface = pygame.Surface(screen.get_size())
        self.surface = self.surface.convert()
        self.teal = (31, 73, 125)
        self.red = (218, 31, 40)

    def _draw_current_eqn(self, position):
        if self.board.current_input:
            guess_num = int_from_digits(self.board.current_input)
            eqn_render = self.board.current_eqn.render(guess=guess_num)
        else:
            eqn_render = self.board.current_eqn.render()

        text = self.font.render(eqn_render, 1, self.teal)
        self.surface.blit(text, position)
        text_rect = pygame.Rect(5, self.board.current_eqn.ypos - 30, 175, 78)
        pygame.draw.rect(self.surface, self.red, text_rect, 1)
        
    def draw(self, mode):
        raise NotImplementedError

                
class StaticGui(GuiView):
    def __init__(self, board, screen):
        super(StaticGui, self).__init__(board, screen)

    def draw(self):
        # TODO: Clear only the part of the screen that the equation
        # occupied.
        self.surface.fill ((250, 250, 250))

        self._draw_current_eqn(position=(130, 200))

#        if self.controller.display_correct:
#            correct_text = self.font.render("Correct", 1, self.teal)
#            self.surface.blit(correct_text, (130, 240))
#
#        elif self.controller.display_incorrect:
#            incorrect_text = self.font.render("Incorrect. Answer is " + str(self.board.current_eqn.answer), 1, self.teal)
#            self.surface.blit(incorrect_text, (130, 240))    
        
        text_rect = pygame.Rect(15, 180, 175, 60)
        border = pygame.draw.rect(self.surface, self.red, text_rect, 1)

        self.screen.blit (self.surface, (0, 0))
        pygame.display.flip()

class DynamicGui(GuiView):
    def __init__(self, board, screen):
        super(DynamicGui, self).__init__(board, screen)

    def draw(self):
        if self.board.mode == 'falling':
            self._draw_falling()
        elif self.board.mode == 'exploding':
            self._draw_exploding()
        self.screen.blit (self.surface, (0, 0))
        pygame.display.flip()
        
    def _draw_falling(self):
        # TODO: Clear only the part of the screen that the equation
        # occupied.
        self.surface.fill ((250, 250, 250))
        
        self._draw_current_eqn(position=(30, self.board.current_eqn.ypos))
        self._draw_dead_eqns()

    def _draw_dead_eqns(self):
        for i, eqn in enumerate(self.board.dead_eqns):
            eqn_string = eqn.render(with_answer=True)
            eqn_img = self.font.render(eqn_string, 1, self.red)
            img_pos = self.board.height - i * 30
            self.surface.blit(eqn_img, (30, img_pos))

            # draw border
            text_rect = pygame.Rect(5, img_pos - 30, 175, 78)
            pygame.draw.rect(self.surface, self.red, text_rect, 1)

    def _draw_exploding(self):
        self.surface.fill(Color('red'))

class SummaryGui(GuiView):
    def __init__(self, board, screen):
        super(SummaryGui, self).__init__(board, screen)

    def draw(self):
        summary_string = 'You answered {0} of {1} problems correctly'
        formatted_string = summary_string.format(self.board.correct_tally,
                                                 self.board.problem_count)
        text = self.font.render(formatted_string,
                                 1, (31, 73, 125), (250, 250, 250))
        self.surface.fill ((250, 250, 250))
        self.surface.blit(text, (130, 200))    
        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()
        
class WelcomeGui(object):
    def __init__(self, screen, controller):
        self.screen = screen
        self.surface = pygame.Surface(screen.get_size())
        self.surface = self.surface.convert()

        container = gui.Container(align=-1,valign=-1)
        container.add(welcome_table(controller), 400, 320)
        self.app = gui.App()
        self.app.init(container)

    def draw(self):
        self.surface.fill((250, 250, 250))
        self.app.paint(self.surface)        

        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()

def welcome_table(controller):
    fg = (31, 73, 125)
    table = gui.Table()
    table.tr()
    table.td(gui.Label("Welcome to Tetris Math", color=fg, cls="h1"), colspan=2)
    table.tr()
    table.td(gui.Label(""))
    table.tr()
    table.td(gui.Label("Choose from the following options: ", color=fg), colspan=2)
    table.tr()
    table.td(gui.Label(""))
    table.tr()
    button = gui.Button("1. Single Player", width=150)
    button.connect(gui.CLICK, controller.change_mode, 'single_player_mode')
    table.td(button)
    table.tr()
    table.td(gui.Label(""))
    table.tr()
    button = gui.Button("2. Multi-Player", width=150)
    button.connect(gui.CLICK, controller.change_mode, 'multi_player_mode')
    table.td(button)
    table.tr()
    table.td(gui.Label(""))        
    table.tr()
    button = gui.Button("3. Practice Quiz", width=150)
    button.connect(gui.CLICK, controller.change_mode, 'quiz_mode')
    table.td(button)
    return table
