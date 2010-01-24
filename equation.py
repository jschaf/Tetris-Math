'''Represent an equation.
'''

from random import choice, randint
from operator import add, sub, mul, floordiv

class Equation(object):
    '''Represent an equation.
    '''

    def __init__(self, difficulty):
        eqn_levels = {0 : (add, sub),
                      1 : (mul, floordiv),
                      2 : (pow,)}

        # Should use nice unicode symbols.
        eqn_represenations = {add : '+', sub : '-', mul : '*', floordiv : '/',
                             pow : '^'}


        self.eqn_function = choice(eqn_levels[difficulty])
        self.eqn_repr = eqn_represenations[self.eqn_function]

        # Should limit leftSide and rightSide to reasonable values for
        # different operators.
        self.left_side = randint(0, 10)
        self.right_side = randint(0, 10)
        self.answer = self.eqn_function(self.left_side, self.right_side)

    def render(self, with_answer=False):
        '''Return a string representation of the equation.'''
        render_string = '{0} {1} {2}'.format(self.left_side, self.eqn_repr,
                                            self.right_side)
        if with_answer:
            render_string += ' = {0}'.format(self.answer)
        return render_string

    def draw(self, with_answer=False):
        '''Draw the rendering of the equation.'''
        
        print('Drawing: ' + self.render(with_answer))
    
