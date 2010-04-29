'''A controller class for the views.'''
from pygame.locals import *
import pygame

from pgu import gui

from gui_view import WelcomeGui, StaticGui, DynamicGui, SummaryGui, MessageGui
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
        
    def new_level(self):
        self.board.next_level()
        self.change_mode('message_mode')
        
        
    def update(self):
        '''Perform the appropriate actions for each mode.'''
        if pygame.event.peek().type is QUIT:
            self.exit_program()
        else:    
            if self.mode == "playing":
                self._check_playing_events()
                self.board.update()
            elif self.mode == "summary":
                self._check_summary_events()
            elif self.mode == 'message':
                self._check_message_events()
            elif self.mode == "welcome":
                self._check_welcome_events()
         
    def _check_summary_events(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key in self.quit_keys:
                    self.exit_program()
                elif e.key == K_RETURN:
                    self.change_mode('welcome_mode')
                    
    def _check_message_events(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_RETURN:
                    self.return_to_mode('single_player_mode')

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
                

    def _check_playing_events(self):
        number_keys = [K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]
        number_key_dict = dict(zip(number_keys, range(10)))
        input_length = len(self.board.current_input)
        
        if self.board.mode == "game_over":
            self.end_game()        
        elif self.board.mode == "level_break":
            print self.board.mode
            self.new_level()
        
        else:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Clear message from screen
                    self.gui_view.message = None
                    # Only take user input if not displaying a message
                    if event.key in self.quit_keys:
                        self.change_mode('summary_mode')
                        
                    elif event.key == K_RETURN and input_length > 0:
                        print 1
                        self.board.check_ans()
                        
                    elif not (self.board.display_correct or self.board.display_incorrect):
                        # Only allows 3 digits of input
                        if event.key in number_keys and input_length < 3:
                            self.board.current_input.append(number_key_dict[event.key]) 
                        
                        elif event.key == K_BACKSPACE and input_length > 0:
                            self.board.current_input.pop()
                        # Won't display the message with backspace or extra digits                                                
                        elif event.key != K_BACKSPACE and input_length < 3:
                            self.gui_view.message = "Must input a number" 
      
      
    def change_mode(self, new_mode):
        if new_mode == 'single_player_mode':
            self.board = DynamicBoard(WINDOW_SIZE)
            self.gui_view = DynamicGui(self.board, self.screen)
            pygame.mixer.music.load('alejandro.ogg')
            pygame.mixer.music.play(-1)
            self.mode = "playing"

        elif new_mode == 'multi_player_mode':
            print("Multi-player not implemented yet")

        elif new_mode == 'quiz_mode':
            self.board = StaticBoard(WINDOW_SIZE)
            self.gui_view = StaticGui(self.board, self.screen)
            self.mode = "playing"
            
        elif new_mode == 'summary_mode':
            self.gui_view = SummaryGui(self.board, self.screen, controller = self)
            self.mode = 'summary'
            
        elif new_mode == 'message_mode':
            self.gui_view = MessageGui(self.board, self.screen, controller = self)
            self.mode = 'message'
            
        elif new_mode == 'welcome_mode':
            self.gui_view = WelcomeGui(self.screen, controller = self)
            self.mode = 'welcome'    
            
        else:
            raise AttributeError

    def return_to_mode(self, mode):
        if mode == 'single_player_mode':
            self.gui_view = DynamicGui(self.board, self.screen)
            self.mode = "playing"
            
    
    def draw(self):
        '''Draw'''
        self.gui_view.draw()
        # self.text_view.draw()


    