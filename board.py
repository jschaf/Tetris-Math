'''A game board for equations.
'''

class Board(object):
    '''A board to hold the game state.
    '''

    def __init__(self):
        self.dead_eqns = 0
        self.current_eqn = None

    def update(self):
        '''Update the board state.'''
        pass
    
    def draw(self):
        '''Draw the board.
        '''
        pass
