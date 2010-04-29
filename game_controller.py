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
        self.running = True
        self.mode = "welcome"
        self.quit_keys = [K_ESCAPE, K_q]
        
#    def generate_equation(self):
#        '''Create a new equation to pass to the models.'''
#        self.board.problem_count += 1     
#        return Equation(0)
        
    def exit_program(self):
        self.running = False

    def end_game(self):
        pygame.mixer.music.fadeout(1000)
        self.change_mode('summary_mode')
        
    def update(self):
        '''Perform the appropriate actions for each mode.'''
        if pygame.event.peek().type is QUIT:
            self.exit_program()
        else:    
            if self.mode == "single_player":
                self._check_single_player_events()
                self.board.update()
            elif self.mode == "quiz":
                self._check_quiz_events()
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
                    self.change_mode('welcome_mode')

    def _check_welcome_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in self.quit_keys:
                    self.exit_program()
                elif event.key == K_1:
                    self.change_mode('single_player_mode')
                elif event.key == K_2:
                    self.change_mode('multi_player_mode')
                elif event.key == K_3:
                    self.change_mode('quiz_mode')
            else:
                # pass events to PGU
                self.gui_view.app.event(event)
                
    # TODO: cut down on repeated code by creating an event checker class        
    def _check_single_player_events(self):
        number_keys = [K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]
        number_key_dict = dict(zip(number_keys, range(10)))
        
        if self.board.mode == "game_over":
            self.end_game()
        
        else:   
            for event in pygame.event.get():
                if event.type == KEYDOWN:
    
                    if event.key in self.quit_keys:
                        self.change_mode('summary_mode')
    
                    if event.key in number_keys:
                        self.board.current_input.append(number_key_dict[event.key]) 
    
                    elif event.key == K_BACKSPACE and len(self.board.current_input) > 0:
                        self.board.current_input.pop()
    
                    elif event.key == K_RETURN:
                        self._update_single_player()
    
                    else:
                        # TODO: Have some sort of display to inform the user that
                        # we need a number
                        pass
                
    def _check_quiz_events(self):
        number_keys = [K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]
        number_key_dict = dict(zip(number_keys, range(10)))
        input_length = len(self.board.current_input)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # Clear message from screen
                self.gui_view.message = None
                # Only take user input if not displaying a message
                if event.key in self.quit_keys:
                    self.change_mode('summary_mode')
                    
                elif event.key == K_RETURN and input_length > 0:
                    self._update_quiz()
                    
                elif not (self.board.display_correct or self.board.display_incorrect):
                    # Only allows 3 digits of input
                    if event.key in number_keys and input_length < 3:
                        self.board.current_input.append(number_key_dict[event.key]) 
                    
                    elif event.key == K_BACKSPACE and input_length > 0:
                        self.board.current_input.pop()
                    # Won't display the message with backspace or extra digits                                                
                    elif event.key != K_BACKSPACE and input_length < 3:
                        self.gui_view.message = "Must input a number" 
                

    def _update_single_player(self):
        if self.board.has_correct_guess():
            print('correct')
            self.board.correct_tally += 1
        else:
            print('incorrect: answer is ' + str(self.board.current_eqn.answer))
            self.board.display_incorrect = True

        new_equation = self.generate_equation()
        self.board.current_eqn = new_equation
        self.board.current_input = []
        
    def _update_quiz(self):
        if self.board.display_correct or self.board.display_incorrect:
            if self.board.problem_count == 10:
                self.change_mode('summary_mode')                  
            else:    
                self._next_eqn()
        else:
            if self.board.has_correct_guess():
                self.board.display_correct = True
                self.board.correct_tally += 1
           
            else:
                self.board.display_incorrect = True
                

    def change_mode(self, new_mode):
        if new_mode == 'single_player_mode':
            self.board = DynamicBoard(WINDOW_SIZE)
            self.gui_view = DynamicGui(self.board, self.screen)
            self.init_single_player()
            self.mode = "single_player"

        elif new_mode == 'multi_player_mode':
            print("Multi-player not implemented yet")

        elif new_mode == 'quiz_mode':
            self.board = StaticBoard(WINDOW_SIZE)
            self.gui_view = StaticGui(self.board, self.screen)
            self.mode = "quiz"
            
        elif new_mode == 'summary_mode':
            self.gui_view = SummaryGui(self.board, self.screen)
            self.mode = 'summary'
            
        elif new_mode == 'welcome_mode':
            self.gui_view = WelcomeGui(self.screen, controller = self)
            self.mode = 'welcome'    
            
        else:
            raise AttributeError
        

        
    def init_single_player(self):
        pass
    
    def draw(self):
        '''Draw'''
        self.gui_view.draw()
        # self.text_view.draw()


    