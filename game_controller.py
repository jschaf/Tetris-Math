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
        self.mode = "running"
        initial_eqn = Equation(0)
        self.board.current_eqn = initial_eqn
        self.gui_view.update_eqn(initial_eqn)
        self.text_view.update_eqn(initial_eqn)
        self.number_keys = [K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]
        self.number_key_dict = dict(zip(self.number_keys, range(10)))
              
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
            self.check_running_events()
        elif self.mode == "summary":
            self.check_summary_events()
         
    def check_quit_events(self):
        if pygame.event.peek().type is QUIT:
            self.running = False   
            
    def check_summary_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # TODO: Use buttons "are you sure"
                if event.key in [K_ESCAPE, K_q]:
                    self.running = False
                
    def check_running_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in [K_ESCAPE, K_q]:
                    self.end_game()
                elif event.key in self.number_keys:
                    self.board.current_input.append(self.number_key_dict[event.key])
                    self.gui_view.refresh()
                elif event.key == K_RETURN:
                    #compare, display, feedback
                    self._update_eqn()                    
            elif event.type is MOUSEBUTTONDOWN:
                new_equation = self.generate_equation()
                
                self.board.current_eqn = new_equation
                self.gui_view.update_eqn(new_equation)
                self.text_view.update_eqn(new_equation)
                
                self.board.problem_count += 1 

    def draw(self):
        '''Draw every model.'''
        self.gui_view.draw(self.mode)
        self.text_view.draw()
