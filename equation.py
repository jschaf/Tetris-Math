'''Represent an equation.
'''

from random import choice, randint
from operator import add, sub, mul, floordiv

def int_from_digits(nums):
    '''Given a list of ints, return the corresponding integer'''
    if not nums:
        return None
    else:
        return int(''.join([str(n) for n in nums]))
    
class Equation(object):
    '''Represent an equation.

    TODO:  Fine grained difficulty for negative numbers.
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
        self.is_killed = False
        # Should limit leftSide and rightSide to reasonable values for
        # different operators.  Also make sure division is even.
        self.left_side = randint(0, 10)
        if self.eqn_function == sub:
            self.right_side = randint(0, self.left_side)
        else:
            self.right_side = randint(0, 10)
        self.answer = self.eqn_function(self.left_side, self.right_side)
    
   
    def render(self, guess=None, with_answer=False):
        '''Return a string representation of the equation.'''
        render_string = '{0} {1} {2} = '.format(self.left_side, self.eqn_repr,
                                                self.right_side)
        if guess is not None:
            render_string += str(guess)
        elif with_answer:
            render_string += str(self.answer)
        return render_string
