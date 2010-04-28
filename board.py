'''A game board for equations.
'''
import random
from equation import int_from_digits, Equation

class Board(object):
    '''A board to hold the game state.  Equations start at the top
    (defined as 0) and progress down the screen at the rate defined by
    drop_speed.  When the equation hits the bottom or the stack of
    dead equations a new dead equation is created.  When
    '''
    def __init__(self, window_size):
        self.width, self.height = window_size
        self.dead_eqns = []
        self.current_eqn = Equation(0)
        self.problem_count = 0
        self.current_input = []
        self.correct_tally = 0
        
    def has_correct_guess(self):
        '''Return if the current_input matches the answer.'''
        guess = int_from_digits(self.current_input)
        return self.current_eqn.answer == guess

    def update(self):
        '''Update the board state.'''
        raise NotImplementedError

class StaticBoard(Board):
    def __init__(self, window_size):
        super(StaticBoard, self).__init__(window_size)

    def update(self):
        pass

class DynamicBoard(Board):
    def __init__(self, window_size):
        super(DynamicBoard, self).__init__(window_size)
        self.drop_speed = 3
        self.explode_animation_frame = 0
        self.NUM_EXPLODE_FRAMES = 20
        self.DEAD_EQN_HEIGHT = 10
        self.mode = "falling"

    def kill_current_eqn(self):
        '''If the equation reaches the bottom of the dead equations
        then blow it up.'''
        self.current_eqn.is_dead = True
        self.dead_eqns.append(self.current_eqn)
        self.problem_count += 1
        self.mode = "exploding"

    def increase_drop_speed(self):
        '''Increase the rate at which the equations fall.'''
        self.drop_speed += 1

    def update(self):
        '''Update the board state.'''
        if self.mode == 'exploding':
            if self.explode_animation_frame > self.NUM_EXPLODE_FRAMES:
                self.explode_animation_frame = 0
                self.mode = 'falling'
                self.current_eqn = Equation(0)
            else:
                self.explode_animation_frame += 1

        elif self.mode == 'falling':
            self.current_eqn.ypos += self.drop_speed

            dead_eqns_height = len(self.dead_eqns) * self.DEAD_EQN_HEIGHT

            if dead_eqns_height >= self.height:
                self.mode = 'game_over'
        

            if (self.height - dead_eqns_height) <= self.current_eqn.ypos:
                self.kill_current_eqn()

        else:
           raise Attribute_Error
