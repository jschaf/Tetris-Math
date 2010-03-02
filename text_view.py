'''A view for the command line.'''

class TextView(object):
    '''A view primarily to aid in debugging.'''

    def __init__(self, board):
        self.equation = None
        self.changed_eqn = False

    def update_eqn(self, new_eqn):
        self.equation = new_eqn
        self.changed_eqn = True
        
    def draw(self):
        if self.changed_eqn:
            print(self.equation.render())
            self.changed_eqn = False

