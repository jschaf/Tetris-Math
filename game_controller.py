'''A controller class for the views.'''
from pygame.locals import *
import pygame

from equation import Equation
from text_view import TextView
from gui_view import GuiView
from board import Board

WINDOW_SIZE = (1024,768)

class GameController(object):
    '''Controller.'''

    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW_SIZE, 0, 8)
        self.board = Board(WINDOW_SIZE, self.screen)
        self.gui_view = GuiView(self.board, self.screen)
        self.text_view = TextView(self.board)
        self.running = True
        self.mode = "welcome"
        initial_eqn = Equation(0)
        self.board.current_eqn = initial_eqn
        self.gui_view.update_eqn(initial_eqn)
        self.text_view.update_eqn(initial_eqn)
              
    def generate_equation(self):
        '''Create a new equation to pass to the models.'''
        return Equation(0)
    
    def _update_eqn(self):
        if self.board.has_correct_guess():
            print('correct')
            new_equation = self.generate_equation()
            self.board.current_eqn = new_equation
            self.gui_view.update_eqn(new_equation)
            self.text_view.update_eqn(new_equation)
            self.board.correct_tally += 1
            self.board.problem_count += 1 
        else:
            print('incorrect: answer is ' + str(self.board.current_eqn.answer))
        self.board.current_input = []
        self.gui_view.refresh()
        
    def end_game(self):
        self.gui_view.clear_screen()
        self.mode = "summary"
        

    def update(self):
        '''This function provides a loop and variables to keep
        displaying math problems.'''
        
        self.check_quit_events()
        if self.mode == "running":
            self.board.update()
            self.check_running_events()
        elif self.mode == "summary":
            self.check_summary_events()
        elif self.mode == "welcome":
            self.check_welcome_events()
            
         
    def check_quit_events(self):
        quit_keys = [K_ESCAPE, K_q]

        if pygame.event.peek() in quit_keys:
            self.end_game()
            
    def check_summary_events(self):
        pass

    def check_welcome_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_1:
                    print "Dynamic version not yet implemented"
                elif event.key == K_2:
                    print "Multiplayer not yet implented"
                elif event.key == K_3:
                    self.mode = "running"
                
    def check_running_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                self._check_keydown(event)

            elif event.type is MOUSEBUTTONDOWN:
                self._check_mousedown(event)

    def _check_keydown(self, event):
        number_keys = [K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]

        # Generate a mapping of key events to its corresponding
        # number.
        number_key_dict = dict(zip(number_keys, range(10)))

        if event.key in number_keys:
            print(number_key_dict[event.key])
            self.board.current_input.append(number_key_dict[event.key])
            self.gui_view.refresh()

        elif event.key == K_RETURN:
            #compare, display, feedback
            self._update_eqn()                    

        else:
            # TODO: Have some sort of display to inform the user that
            # we need a number
            pass

    def _check_mousedown(self, event):
        new_equation = self.generate_equation()

        self.board.current_eqn = new_equation
        self.gui_view.update_eqn(new_equation)
        self.text_view.update_eqn(new_equation)

        self.board.problem_count += 1 
        
    def draw(self):
        '''Draw every model.'''
        self.gui_view.draw(self.mode)
        self.text_view.draw()
