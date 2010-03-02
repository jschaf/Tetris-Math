'''A controller class for the views.'''
from pygame.locals import *
import pygame

from equation import Equation
from text_view import TextView
from gui_view import GuiView

class GameController(object):
    '''Controller.'''

    def __init__(self, board):
        self.board = board
        self.gui_view = GuiView(board)
        self.text_view = TextView(board)
        self.running = True
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
        else:
            print('incorrect: answer is ' + str(self.board.current_eqn.answer))
        self.board.current_input = []
        self.gui_view.refresh()
        self.board.problem_count += 1 

    def update(self):
        '''This function provides a loop and variables to keep
        displaying math problems.'''
        

        for event in pygame.event.get():
            if event.type is QUIT:
                self.running = False
            
            if event.type == KEYDOWN:
                if event.key in self.number_keys:
                    key_num = self.number_key_dict[event.key]
                    self.board.current_input.append(key_num)
                    self.gui_view.refresh()
                if event.key == K_RETURN:
                    #compare, display, feedback
                    self._update_eqn()
                    
            if event.type is MOUSEBUTTONDOWN:
                new_equation = self.generate_equation()

                self.gui_view.update_eqn(new_equation)
                self.text_view.update_eqn(new_equation)
                
                self.board.problem_count += 1 

    def draw(self):
        '''Draw every model.'''
        self.gui_view.draw()
        self.text_view.draw()
