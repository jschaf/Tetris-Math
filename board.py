'''A game board for equations.
'''


# Tetris Math prototype

# import necessary modules
import random

class Board(object):
    '''A board to hold the game state.  Equations start at the top
    (defined as 0) and progress down the screen at the rate defined by
    drop_speed.  When the equation hits the bottom or the stack of
    dead equations a new dead equation is created.  When 
    '''
    DEAD_EQN_HEIGHT = 10

    def __init__(self, width, height, surface):
        self.width = width
        self.height = height
        self.surface = surface
        self.dead_eqns = 0
        self.current_eqn = None
        self.current_eqn_position = 0
        self.drop_speed = 1
        self.problem_count = 0
        self.correct_tally = 0

    def increase_drop_speed(self):
        '''Increase the rate at which the equations fall.'''
        self.drop_speed += 1

    def update(self):
        '''Update the board state.'''
        self.current_eqn_position += self.drop_speed
        if ((self.height - self.dead_eqns * DEAD_EQN_HEIGHT)
            >= current_eqn_position):
            self.dead_eqns += 1
            self.kill_current_eqn()

    def kill_current_eqn(self):
        '''If the equation reaches the bottom of the dead equations
        then blow it up.'''
        pass



