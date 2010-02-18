'''A view for the command line.'''

import equation

class TextView(object):
    '''A view primarily to aid in debugging.'''

    def __init__(self, board):
        self.equation = equation.Equation(0)


    def draw(self):
        print(self.equation.render())

    def update_equation(self, equation):
        self.equation = equation

