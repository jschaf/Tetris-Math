'''A controller class for the views.'''
from pygame.locals import *
import pygame

from equation import Equation
from text_view import TextView
from gui_view import GuiView
from board import Board
from pgu import gui
import sys
from board import DynamicBoard
from board import StaticBoard
from game_controller import WINDOW_SIZE

WINDOW_SIZE = (1024,768)

class GameController(object):
    '''Controller.'''

    def __init__(self, screen):
        self.screen = screen
        self.board = Board(WINDOW_SIZE, self.screen)
        self.app = gui.App()
        self.gui_view = GuiView(self.board, self.screen, self, self.app)
        self.text_view = TextView(self.board)
        self.running = True
        self.mode = "welcome"
        initial_eqn = Equation(0)
        self.board.current_eqn = initial_eqn
        self.quit_keys = [K_ESCAPE, K_q]
        self.display_correct = False
        self.display_incorrect = False
              
    def generate_equation(self):
        '''Create a new equation to pass to the models.'''
        self.board.problem_count += 1     
        return Equation(0)
        
    def end_game(self):
        if self.mode == "summary":
            self.running = False
        else:
            self.mode = "summary"
        
    def update(self):
        '''Perform the appropriate actions for each mode.'''
        # TODO: need to run through all events because quit might be
        # masked.
        self._check_events()
        if self.mode == "playing":
            self.board.update()
        elif self.mode == "summary":
            self.check_summary_events()
        elif self.mode == "welcome":
            self.check_welcome_events()
         
    def check_summary_events(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key in self.quit_keys:
                    self.running = False
                elif e.key == K_RETURN:
                    pass        # was init_game

    def check_welcome_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in self.quit_keys:
                    self.end_game()
                elif event.key == K_1:
                    self.run_single_player()
                elif event.key == K_2:
                    self.run_multi_player
                elif event.key == K_3:
                    self.run_quiz(None)
            else:
                print(".")
                self.app.event(event)
                
    def _check_events(self):
        number_keys = [K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]
        number_key_dict = dict(zip(number_keys, range(10)))

        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key in self.quit_keys:
                    self.end_game()

                if event.key in number_keys:
                    self.board.current_input.append(number_key_dict[event.key]) 

                elif event.key == K_BACKSPACE and len(self.board.current_input) > 0:
                    self.board.current_input.pop()

                elif event.key == K_RETURN:
                    self._update_eqn()

                else:
                    # TODO: Have some sort of display to inform the user that
                    # we need a number
                    pass

    def _update_eqn(self):
        if self.board.has_correct_guess():
            print('correct')
            self.board.correct_tally += 1
            self.board.problem_count += 1 
        else:
            print('incorrect: answer is ' + str(self.board.current_eqn.answer))
            self.display_incorrect = True

        new_equation = self.generate_equation()
        self.board.current_eqn = new_equation
        self.board.current_input = []

    # arg necessary for call from button click
    def run_quiz(self, arg):
        self.board = StaticBoard(WINDOW_SIZE)
        self.mode = "playing"
    
    def run_single_player(self, arg=None):
        self.board = DynamicBoard(WINDOW_SIZE)
        self.mode = "playing"

    def run_multi_player(self, arg=None):
        print("Multi-player not implemented yet")
        # self.mode = "playing"

    def draw(self):
        '''Draw every model.'''
        self.gui_view.draw(self.mode)
        self.text_view.draw()
