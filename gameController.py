'''A controller class for the views.'''
from pygame.locals import *
import pygame

import board
import equation
import textView
import guiView

class GameController(object):
    '''Controller.'''

    def __init__(self, board):
        self.board = board
        self.gui_view = guiView.GuiView(board)
        self.text_view = textView.TextView(board)

    def generate_equation(self):
        '''Create a new equation to pass to the models.'''
        return equation.Equation(0);
    

    def update(self, board):
        '''This function provides a loop and variables to keep
        displaying math problems.'''
        

        for event in pygame.event.get():
            if event.type is QUIT:
                running = False
            if event.type == KEYUP:
                print(event)
            if event.type is MOUSEBUTTONDOWN:
                new_equation = self.generate_equation()

                self.gui_view.update_equation(new_equation)
                self.text_view.update_equation(new_equation)
                
                self.board.problem_count += 1 


        # if (a + b == ans):
        #     print "Correct!"
        #     correctTally += 1
        # else:
        #     print "Incorrect: "+str(a)+" + "+str(b)+" = "+str(a+b)

        # print "You answered " +str(selcorrect_tally)+"/"+str(problem_count)+ " correctly."

    def draw(self):
        '''Draw every model.'''
        self.gui_view.draw()
        self.text_view.draw()
