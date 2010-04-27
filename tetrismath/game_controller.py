'''A controller class for the views.'''
from pygame.locals import *
import pygame

from equation import Equation
from text_view import TextView
from gui_view import GuiView
from board import Board
from pgu import gui
import sys

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
        self.gui_view.update_eqn(initial_eqn)
        self.text_view.update_eqn(initial_eqn)
        self.quit_keys = [K_ESCAPE, K_q]
        self.display_correct = False
        self.display_incorrect = False
         
              
    def generate_equation(self):
        '''Create a new equation to pass to the models.'''
        self.board.problem_count += 1     
        return Equation(0)
    
        
    def end_game(self):
#        self.gui_view.clear_screen()
        if self.mode == "summary":
            for e in pygame.event.get():
                if e.type == KEYDOWN and e.key in self.quit_keys:
                    self.running = False
        else:
            self.mode = "summary"
        

    def update(self):
        '''Perform the appropriate actions for each mode.'''
        if pygame.event.peek().type is QUIT:
            self.running = False  
#        self.check_quit_events()
        if self.mode == "single_player":
            self.board.mode = "falling"
            self.board.update()
            self.check_dynamic_events()
        elif self.mode == "multi_player":
            pass
        elif self.mode == "quiz":
            self.board.mode = "static"
            self.board.update()
            self.check_static_events()
        elif self.mode == "summary":
            self.check_summary_events()
        elif self.mode == "welcome":
            self.check_welcome_events()
            
    def initialize_game(self):
        self.mode = "welcome"
        self.display_correct = False
        self.display_incorrect = False
        self.board.correct_tally = 0
        self.board.problem_count = 0
        self.next_eqn()
         
    def check_quit_events(self):
        e = pygame.event.peek()
        if e.type == KEYDOWN and e.key in self.quit_keys:
            self.end_game()
            
    def check_summary_events(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key in self.quit_keys:
                    self.running = False
                elif e.key == K_RETURN:
                    self.initialize_game()


    def check_welcome_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in self.quit_keys:
                    self.mode = "summary"
                elif event.key == K_1:
                    self.mode = "single_player"
                elif event.key == K_2:
                    print "Multiplayer not yet implented"
                elif event.key == K_3:
                    self.run_quiz(None)
            else:
                sys.stdout.write(".")
                self.app.event(event)
                
    def check_dynamic_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                self._check_keydown(event)

#            elif event.type is MOUSEBUTTONDOWN:
#                self._check_mousedown(event)

    def check_static_events(self):
        if self.board.problem_count == 10:
            self.mode = "summary"
        else:
            for event in pygame.event.get():
                if event.type == KEYDOWN:                
                    self._check_keydown(event)

    def _check_keydown(self, event):
        number_keys = [K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]

        # Generate a mapping of key events to the corresponding
        # number.
        number_key_dict = dict(zip(number_keys, range(10)))

        if event.key in number_keys:
            self.board.current_input.append(number_key_dict[event.key]) 
        elif event.key == K_BACKSPACE and self.board.current_input.__len__() > 0:
            self.board.current_input.pop()

        elif event.key == K_RETURN:
            if self.mode == "quiz":
                self._update_static_eqn()
            elif self.mode == "single_player":
                self._update_dynamic_eqn()
            
        elif event.key in self.quit_keys:
            self.mode = "summary"                    

        else:
            # TODO: Have some sort of display to inform the user that
            # we need a number
            pass

    def _update_static_eqn(self):
        if self.display_correct or self.display_incorrect:
            self.next_eqn()
        else:
            if self.board.has_correct_guess():
                print('correct')
                self.display_correct = True
                self.board.correct_tally += 1
           
            else:
                print('incorrect: answer is ' + str(self.board.current_eqn.answer))
                self.display_incorrect = True
        
    def next_eqn(self):
        new_equation = self.generate_equation()
        self.board.current_eqn = new_equation
        self.gui_view.update_eqn(new_equation)
        self.text_view.update_eqn(new_equation)
        self.board.current_input = []
        self.display_correct = False
        self.display_incorrect = False
        
        
    def _update_dynamic_eqn(self):
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


    def _check_mousedown(self, event):
        new_equation = self.generate_equation()

        self.board.current_eqn = new_equation
        self.gui_view.update_eqn(new_equation)
        self.text_view.update_eqn(new_equation)

        self.board.problem_count += 1
        
    ''' arg necessary for call from button click '''
    def run_quiz(self, arg):
        self.initialize_game()
        self.mode = "quiz"
    
    def run_single_player(self, arg):
        self.mode = "single_player"
         
    def run_multi_player(self, arg):
        print "multi-player not implemented yet"
    
    def draw(self):
        '''Draw every model.'''
        self.gui_view.draw(self.mode)
        self.text_view.draw()
