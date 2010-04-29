'''A view for the Pygame gui.'''


import pygame
from pygame import Color
from pygame.locals import *
from pgu import gui
from equation import int_from_digits

class GuiView(object):
    '''The primary gui view.'''
    
    def __init__(self, board, screen):
        self.font = pygame.font.Font(None, 52)
        self.board = board
        self.screen = screen
        self.surface = pygame.Surface(screen.get_size())
        self.surface = self.surface.convert()
        self.message = None
        self.teal = (31, 73, 125)
        self.red = (218, 31, 40)

    def _draw_current_eqn(self):
        if self.board.current_input:
            guess_num = int_from_digits(self.board.current_input)
            eqn_render = self.board.current_eqn.render(guess=guess_num)
        else:
            eqn_render = self.board.current_eqn.render()

        text = self.font.render(eqn_render, 1, self.teal)
        self.surface.blit(text, (self.board.eqn_xpos, self.board.eqn_ypos))
        text_rect = pygame.Rect(self.board.eqn_xpos - 25, self.board.eqn_ypos - 30, 200, 78)
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

        self._draw_current_eqn()
        prob_num = self.font.render(str(self.board.problem_count) + ".", 1, self.teal)
        self.surface.blit(prob_num, (self.board.eqn_xpos - 62, self.board.eqn_ypos))

        if self.board.display_correct:
            correct_text = self.font.render("Correct", 1, self.teal)
            self.surface.blit(correct_text, (130, 250))

        elif self.board.display_incorrect:
            incorrect_text = self.font.render("Incorrect. Answer is " + str(self.board.current_eqn.answer), 1, self.teal)
            self.surface.blit(incorrect_text, (130, 250))
        
        elif self.message:
            message_text = self.font.render(self.message, 1, self.teal)
            self.surface.blit(message_text, (130, 250))    
    
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
        
        self._draw_current_eqn()
        self._draw_dead_eqns()

    def _draw_dead_eqns(self):
        for i, eqn in enumerate(self.board.dead_eqns):
            eqn_string = eqn.render(with_answer=True)
            eqn_img = self.font.render(eqn_string, 1, self.red)
            img_pos = self.board.height - (i+1) * self.board.DEAD_EQN_HEIGHT
            self.surface.blit(eqn_img, (self.board.eqn_xpos, img_pos))

            # draw border
            text_rect = pygame.Rect(self.board.eqn_xpos - 25, img_pos - 30, 200, 78)
            pygame.draw.rect(self.surface, self.red, text_rect, 1)

    def _draw_exploding(self):
        self.surface.fill(Color('red'))

class SummaryGui(GuiView):
    def __init__(self, board, screen, controller):
        super(SummaryGui, self).__init__(board, screen)
        
        container = gui.Container(align=-1,valign=-1)
        container.add(self.summary_table(controller), 320, 300)
        self.app = gui.App()
        self.app.init(container)

    def draw(self):
#        summary_string = 'You answered %d of %d problems correctly'
#        formatted_string = summary_string % (self.board.correct_tally,
#                                             self.board.problem_count)
#        text = self.font.render(formatted_string,
#                                 1, (31, 73, 125), (250, 250, 250))
#        self.surface.fill ((250, 250, 250))
#        self.surface.blit(text, (130, 200))    
#        self.screen.blit(self.surface, (0, 0))
#        pygame.display.flip()

        self.surface.fill((250, 250, 250))
        self.app.paint(self.surface)        

        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()
        
    def summary_table(self, controller):
        fg = (31, 73, 125)
        summary_string = 'You answered %d of %d problems correctly'
        formatted_string = summary_string % (self.board.correct_tally,
                                                 self.board.problem_count)
        table = gui.Table()
        table.tr()
        table.td(gui.Label(formatted_string, color=fg, cls="h1"), colspan=2)
#        table.tr()
#        table.td(gui.Label(""))
#        table.tr()
#        table.td(gui.Label("Choose from the following options: ", color=fg), colspan=2)
#        table.tr()
#        table.td(gui.Label(""))
#        table.tr()
#        button = gui.Button("1. Single Player", width=150)
#        button.connect(gui.CLICK, controller.change_mode, 'single_player_mode')
#        table.td(button)
#        table.tr()
#        table.td(gui.Label(""))
#        table.tr()
#        button = gui.Button("2. Multi-Player", width=150)
#        button.connect(gui.CLICK, controller.change_mode, 'multi_player_mode')
#        table.td(button)
#        table.tr()
#        table.td(gui.Label(""))        
#        table.tr()
#        button = gui.Button("3. Practice Quiz", width=150)
#        button.connect(gui.CLICK, controller.change_mode, 'quiz_mode')
#        table.td(button)
        return table

class MessageGui(GuiView):
    def __init__(self, board, screen, controller):
        super(MessageGui, self).__init__(board, screen)
        
        container = gui.Container(align=-1,valign=-1)
        container.add(self.summary_table(controller), 320, 300)
        self.app = gui.App()
        self.app.init(container)

    def draw(self):
#        summary_string = 'You answered %d of %d problems correctly'
#        formatted_string = summary_string % (self.board.correct_tally,
#                                             self.board.problem_count)
#        text = self.font.render(formatted_string,
#                                 1, (31, 73, 125), (250, 250, 250))
#        self.surface.fill ((250, 250, 250))
#        self.surface.blit(text, (130, 200))    
#        self.screen.blit(self.surface, (0, 0))
#        pygame.display.flip()

        self.surface.fill((250, 250, 250))
        self.app.paint(self.surface)        

        self.screen.blit(self.surface, (0, 0))
        pygame.display.flip()
        
    def summary_table(self, controller):
        fg = (31, 73, 125)
        
        table = gui.Table()
        table.tr()
        table.td(gui.Label('Congratulations, you just completed Level ' + str(self.board.level - 1), color=fg, cls="h1"), colspan=2)
        table.tr()
        table.td(gui.Label(""))
        table.tr()
        table.td(gui.Label("Hit Enter to continue to Level " + str(self.board.level), color=fg), colspan=2)
#        table.tr()
#        table.td(gui.Label(""))
#        table.tr()
#        button = gui.Button("1. Single Player", width=150)
#        button.connect(gui.CLICK, controller.change_mode, 'single_player_mode')
#        table.td(button)
#        table.tr()
#        table.td(gui.Label(""))
#        table.tr()
#        button = gui.Button("2. Multi-Player", width=150)
#        button.connect(gui.CLICK, controller.change_mode, 'multi_player_mode')
#        table.td(button)
#        table.tr()
#        table.td(gui.Label(""))        
#        table.tr()
#        button = gui.Button("3. Practice Quiz", width=150)
#        button.connect(gui.CLICK, controller.change_mode, 'quiz_mode')
#        table.td(button)
        return table
        
class WelcomeGui(object):
    def __init__(self, screen, controller):
        self.screen = screen
        self.surface = pygame.Surface(screen.get_size())
        self.surface = self.surface.convert()

        container = gui.Container(align=-1,valign=-1)
        container.add(welcome_table(controller), 360, 280)
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
#    table.tr()
#    button = gui.Button("2. Multi-Player", width=150)
#    button.connect(gui.CLICK, controller.change_mode, 'multi_player_mode')
#    table.td(button)
#    table.tr()
#    table.td(gui.Label(""))        
    table.tr()
    button = gui.Button("3. Practice Quiz", width=150)
    button.connect(gui.CLICK, controller.change_mode, 'quiz_mode')
    table.td(button)
    return table
