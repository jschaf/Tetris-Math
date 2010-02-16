'''A view for the command line.'''

class TextView(object):
    '''A view primarily to aid in debugging.'''

    def __init__(self, board):
        self.equation = None


    def draw(self):
        print(equation.render())

    def update_equation(self, equation):
        self.equation = equation

