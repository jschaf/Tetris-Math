'''A controller class for the views.'''
from pygame.locals import *
import pygame

from pgu import gui

from gui_view import *
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
        self.gui_view.end_game()
        
    def lose_game(self):
        self.change_mode('lose_mode')
        
    def win_game(self):
        self.change_mode('win_mode')
        
    def new_level(self):
        self.board.next_level()
        self.change_mode('message_mode')
        
        
    def update(self):
        '''Perform the appropriate actions for each mode.'''
        if pygame.event.peek(QUIT):
            self.exit_program()
        else:    
            if self.mode == "single_player" or self.mode == 'quiz':
                self._check_playing_events()
                self.board.update()               
            elif self.mode == "summary":
                self._check_summary_events()
            elif self.mode == 'message':
                self._check_message_events()
            elif self.mode == "pause":
                self._check_pause_events()
            elif self.mode == 'settings':
                self._check_settings_events()
            elif self.mode == "lose":
                self._check_lose_events()
            elif self.mode == "win":
                self._check_win_events()
            elif self.mode == "scores":
                self._check_scores_events()
            elif self.mode == "welcome":
                self._check_welcome_events()
            elif self.mode == 'multi_player':
                self._check_multi_player_events()
            elif self.mode == 'instructions':
                self._check_instructions_events()
         
    def _check_summary_events(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
#                if e.key == K_RETURN:
#                    self.change_mode('welcome_mode')
#                    return
                if e.key == K_1:
                    self.change_mode('quiz_mode')
                    return
                elif e.key == K_2:
                    self.change_mode('welcome_mode')
                    return
                elif e.key == K_3:
                    self.exit_program()
                    return
                elif e.key in self.quit_keys:
                    self.exit_program()
                    return

            if self.gui_view.app:
                self.gui_view.app.event(e)
                    
    def _check_message_events(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_RETURN:
                    self.return_to_mode('single_player_mode')
                    return

            if self.gui_view.app:
                self.gui_view.app.event(e)
                
    def _check_instructions_events(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_RETURN:
                    self.change_mode('single_player_mode')
                elif e.key in self.quit_keys:
                    self.change_mode('welcome_mode')

            if self.gui_view.app:
                self.gui_view.app.event(e)

    def _check_welcome_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in self.quit_keys:
                    self.exit_program()
                elif event.key == K_1:
                    self.change_mode('instructions_mode')
                elif event.key == K_2:
                    self.change_mode('multi_player_mode')
                elif event.key == K_3:
                    self.change_mode('quiz_mode')
                elif event.key == K_4:
                    self.change_mode('high_scores_mode')
                elif event.key == K_s:
                    self.change_mode('settings_mode')
#            else:
                # pass events to PGU
            if self.gui_view.app:
                self.gui_view.app.event(event)
                
    def _check_pause_events(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in self.quit_keys:
                    self.end_game()
                    return
                elif event.key == K_SPACE:
                    self.return_to_mode('single_player_mode')
                    return
            
            if self.gui_view.app:
                    self.gui_view.app.event(event)
                
    def _check_lose_events(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
#                if e.key == K_RETURN:
#                    self.change_mode('welcome_mode')
#                    return
                if e.key == K_1:
                    self.change_mode('single_player_mode')
                    return
                elif e.key == K_2:
                    self.change_mode('welcome_mode')
                    return
                elif e.key == K_3:
                    self.exit_program()
                    return
                elif e.key in self.quit_keys:
                    self.exit_program()
                    return
            
            if self.gui_view.app:
                    self.gui_view.app.event(e)

    def _check_win_events(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
#                if e.key == K_RETURN:
#                    self.change_mode('welcome_mode')
#                    return
                if e.key == K_1:
                    self.change_mode('single_player_mode')
                    return
                elif e.key == K_2:
                    self.change_mode('welcome_mode')
                    return
                elif e.key == K_3:
                    self.exit_program()
                    return
                elif e.key in self.quit_keys:
                    self.exit_program()
                    return
            
            if self.gui_view.app:
                    self.gui_view.app.event(e)

    def _check_scores_events(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_RETURN or e.key in self.quit_keys:
                    self.change_mode('welcome_mode')
                    return
            
            if self.gui_view.app:
                    self.gui_view.app.event(e)   
                
    def _check_settings_events(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_RETURN or e.key in self.quit_keys:
                    self.change_mode('welcome_mode')
            
            if self.gui_view.app:
                    self.gui_view.app.event(e)
                
    def _check_multi_player_events(self):
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                if e.key == K_RETURN or e.key in self.quit_keys:
                    self.change_mode('welcome_mode')
            
            if self.gui_view.app:
                    self.gui_view.app.event(e)
                

    def _check_playing_events(self):
        number_keys = [K_0, K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]
        number_key_dict = dict(zip(number_keys, range(10)))
        input_length = len(self.board.current_input)
        
        if self.board.mode == "game_over":
            self.end_game()
        elif self.board.mode == "lose":
            self.lose_game()
        elif self.board.mode == "win":
            self.win_game()        
        elif self.board.mode == "level_break":
            self.new_level()
        
        else:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # Clear message from screen
                    self.gui_view.message = None
                    # Only take user input if not displaying a message
                    if event.key in self.quit_keys:
                        self.end_game()
                    elif event.key == K_RETURN and input_length > 0:
                        self.board.check_ans()
                        
                    elif not (self.board.display_correct or self.board.display_incorrect):
                        # Only allows 3 digits of input
                        if event.key in number_keys and input_length < 3:
                            self.board.current_input.append(number_key_dict[event.key]) 
                        
                        elif event.key == K_BACKSPACE and input_length > 0:
                            self.board.current_input.pop()
                            
                        elif event.key == K_SPACE and self.mode == 'single_player':
                            self.change_mode('pause_mode')
                        # Won't display the message with backspace or extra digits                                                
                        elif event.key != K_BACKSPACE and input_length < 3:
                            self.gui_view.message = "Must input a number" 
      
      
    def change_mode(self, new_mode):
        if new_mode == 'single_player_mode':
            self.board = DynamicBoard(WINDOW_SIZE)
            self.gui_view = DynamicGui(self.board, self.screen, controller = self)
            pygame.mixer.music.load('alejandro.ogg')
            pygame.mixer.music.play(-1)
            self.mode = "single_player"

        elif new_mode == 'multi_player_mode':
            self.gui_view = MultiplayerGui(self.screen, controller = self)
            self.mode = 'multi_player'

        elif new_mode == 'quiz_mode':
            self.board = StaticBoard(WINDOW_SIZE)
            self.gui_view = StaticGui(self.board, self.screen, controller = self)
            self.mode = "quiz"
            
        elif new_mode == 'instructions_mode':
            self.gui_view = InstructionsGui(self.board, self.screen, controller = self)
            self.mode = 'instructions'
            
        elif new_mode == 'summary_mode':
            self.gui_view = SummaryGui(self.board, self.screen, controller = self)
            self.mode = 'summary'
            
        elif new_mode == 'message_mode':
            self.gui_view = MessageGui(self.board, self.screen, controller = self)
            self.mode = 'message'
            
        elif new_mode == 'welcome_mode':
            self.gui_view = WelcomeGui(self.screen, controller = self)
            self.mode = 'welcome'

        elif new_mode == 'high_scores_mode':
            self.gui_view = HighScoresGui(self.board, self.screen, controller = self)
            self.mode = 'scores'
            
        elif new_mode == 'pause_mode':
#            pygame.mixer.music.fadeout(1000)
            self.gui_view = PauseGui(self.screen, controller = self)
            self.mode = 'pause'
            
        elif new_mode == 'lose_mode':
            self.gui_view = LoseGui(self.board, self.screen, controller = self)
            self.mode = 'lose'
            
        elif new_mode == 'win_mode':
            self.gui_view = WinGui(self.board, self.screen, controller = self)
            self.mode = 'win'
            
        elif new_mode == 'settings_mode':
            self.gui_view = SettingsGui(self.screen, controller = self)
            self.mode = 'settings'    
            
#        else:
#            raise AttributeError

    def return_to_mode(self, mode):
        if mode == 'single_player_mode':
            self.gui_view = DynamicGui(self.board, self.screen, controller = self)
            self.mode = "single_player"
            
    
    def draw(self):
        '''Draw'''
        self.gui_view.draw()
        # self.text_view.draw()


    
