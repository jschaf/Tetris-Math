'''A game board for equations.
'''


# Tetris Math prototype

# import necessary modules
import random
from equation import int_from_digits

class Board(object):
    '''A board to hold the game state.  Equations start at the top
    (defined as 0) and progress down the screen at the rate defined by
    drop_speed.  When the equation hits the bottom or the stack of
    dead equations a new dead equation is created.  When
    '''
    DEAD_EQN_HEIGHT = 10

    def __init__(self, window_size, surface):
        self.width, self.height = window_size
        self.surface = surface
        self.current_eqn = None
        self.current_eqn_position = 0
        self.drop_rate = 2
        self.problem_count = 0
        self.correct_tally = 0
        self.current_input = []
        self.mode = "falling"
        self.explode_animation_frame = 0
        self.NUM_EXPLODE_FRAMES = 20
        self.DEAD_EQN_HEIGHT = 80
        self.dead_eqn_list = []
        self.kill_height = 80

    def increase_drop_speed(self):
        '''Increase the rate at which the equations fall.'''
        self.drop_speed += 1
        

    def has_correct_guess(self):
        '''Return if the current_input matches the answer.'''
        guess = int_from_digits(self.current_input)
        return self.current_eqn.answer == guess

    def update(self):
        '''Update the board state.'''
        if self.mode == 'exploding':
            if self.explode_animation_frame > self.NUM_EXPLODE_FRAMES:
                self.explode_animation_frame = 0
                self.mode = 'falling'
            else:
                self.explode_animation_frame += 1

        elif self.mode == 'falling':
            self.current_eqn_position += self.drop_rate
            '''
            Checks to see if equation equation hits the bottom
            If so, adds the equation to the list of dead equations and
            checks to see if the equations are past the top of the screen
            '''
            if ((self.height - self.kill_height) <= self.current_eqn_position):
                self.dead_eqn_list.append(self.current_eqn)
                self.kill_height = (len(self.dead_eqn_list)+1) * self.DEAD_EQN_HEIGHT
                if self.kill_height >= self.height:
                    self.mode = "game_over"
                else:
                    self.current_eqn = None

        
#        else:
#            raise Attribute_Error
    def kill_current_eqn(self):
        '''If the equation reaches the bottom of the dead equations
        then blow it up.'''
        



