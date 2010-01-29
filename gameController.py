'''A controller class for the views.'''

import board
import equation
import textView
import guiView

class GameController(object):
    '''Controller.'''

    def __init__(self):
        self.gui = guiView(board)
        self.terminal = textView(board)

    def generate_equation(self):
        '''Create a new equation to pass to the models.'''
        pass
