'''A controller class for the views.'''
from pygame.locals import *
import pygame

from pgu import gui

from gui_view import WelcomeGui, StaticGui, DynamicGui, SummaryGui
from board import DynamicBoard, StaticBoard
from equation import Equation
WINDOW_SIZE = (1024, 768)

class GameController(object):
    '''Controller.'''
    def __init__(self, screen):
        self.screen = screen
        self.board = DynamicBoard(WINDOW_SIZE)
        self.gui_view = WelcomeGui(self.screen, controller=self)
        self.app = self.gui_view.app
        self.running = True
        self.mode = "welcome"
        self.quit_keys = [K_ESCAPE, K_q]
        
    def generate_equation(self):
        '''Create a new equation to pass to the models.'''
        self.board.problem_count += 1     
        return Equation(0)
        
    def end_game(self):
        if self.mode == "summary":
            pygame.mixer.music.fadeout(1000)
            self.running = False
        else:
            self.mode = "summary"
        
    def update(self):
        '''Perform the appropriate actions for each mode.'''
        # TODO: need to run through all events because quit might be
        # masked.
        if self.mode == "playing":
            self._check_playing_events()
            self.board.update()
        elif self.mode == "summary":
            self._check_summary_events()
        elif self.mode == "welcome":
            self._check_welcome_events()
         
    def _check_summary_events(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key in self.quit_keys:
                    self.running = False
                elif e.key == K_RETURN:
                    pass        # was init_game

    def _check_welcome_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in self.quit_keys:
                    self.end_game()
                elif event.key == K_1:
                    self.run_single_player()
                elif event.key == K_2:
                    self.run_multi_player
                elif event.key == K_3:
                    self.run_quiz()
            else:
                # pass events to PGU
                self.app.event(event)
                
    def _check_playing_events(self):
        number_keys = [K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]
        number_key_dict = dict(zip(number_keys, range(10)))

        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key in self.quit_keys:
                    self.change_mode('summary_mode')

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

    def change_mode(self, new_mode):
        if new_mode == 'single_player_mode':
            self.board = DynamicBoard(WINDOW_SIZE)
            self.gui_view = DynamicGui(self.board, self.screen)
            self.mode = "playing"

        elif new_mode == 'multi_player_mode':
            print("Multi-player not implemented yet")

        elif new_mode == 'quiz_mode':
            self.board = StaticBoard(WINDOW_SIZE)
            self.gui_view = StaticGui(self.board, self.screen)
            self.mode = "playing"
            
        elif new_mode == 'summary_mode':
            self.gui_view = SummaryGui(self.board, self.screen)
            self.mode = 'summary'
        else:
            raise AttributeError

    def draw(self):
        '''Draw'''
        self.gui_view.draw()
        # self.text_view.draw()
