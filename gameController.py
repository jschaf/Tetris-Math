'''A controller class for the views.'''

import pygame

import board
import equation
import textView
import guiView

class GameController(object):
    '''Controller.'''

    def __init__(self, board):
        self.board = board
        self.gui_view = guiView(board)
        self.text_view = textView(board)

    def generate_equation():
        '''Create a new equation to pass to the models.'''
        return Equation(0);
    

    def update(board):
        '''This function provides a loop and variables to keep
        displaying math problems.'''
        new_equation = generate_equation()

        gui_view.update_equation(new_equation)
        text_view.update_equation(new_equation)

        for event in pygame.event.get():
            if event.type is QUIT:
                running = False
            if event.type == KEYUP:
                print(event)
            if event.type is MOUSEBUTTONDOWN:
                drawProblem(ttt, board)
                problem_count += 1    


        # if (a + b == ans):
        #     print "Correct!"
        #     correctTally += 1
        # else:
        #     print "Incorrect: "+str(a)+" + "+str(b)+" = "+str(a+b)

        # print "You answered " +str(selcorrect_tally)+"/"+str(problem_count)+ " correctly."

    def draw(self):
        '''Draw every model.'''
        gui_view.draw()
        text_view.draw()
