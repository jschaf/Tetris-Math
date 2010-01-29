'''A game board for equations.
'''


# Tetris Math prototype

# import necessary modules
import pygame
from pygame.locals import *
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


# draws the problem in the window and also puts it on the command line
    def draw(board):

        a = random.randint(1, 10)
        b = random.randint(1, 10)

        problem = str(a) + " + " + str(b) + " ="

        # render the problem
        font = pygame.font.Font(None, 36) #font height 36 px
        # (text, smoothed(1=true), text RGB color)
        text = font.render(problem, 1, (31,73,125))

        # clear the board and copy the rendered message onto it
        # (RGB color)
        board.fill ((250, 250, 250))
        board.blit(text, (130, 200)) #(x and y location)

        self.surface.blit (board, (0, 0))
        pygame.display.flip()

        global correctTally

        print str(a)+ " + " +str(b)+ " = "
        ans = input()
        if (a + b == ans):
            print "Correct!"
            correctTally += 1
        else:
            print "Incorrect: "+str(a)+" + "+str(b)+" = "+str(a+b)

    def doProblems(ttt, board):
        '''This function provides a loop and variables to keep
        displaying math problems.'''

        # here is a good place to start implementing MVC at some point
        drawProblem(ttt, board) #start with a problem on the screen
        problem_count = 1
        while (problem_count < 10): #loop that waits for a click, then displays the next problem
            drawProblem(ttt,board)
            problem_count += 1

            # ??? this was for debugging, but when I commented it out,
            # the gui wouldn't update with the command line
            for event in pygame.event.get():
                if (event.type == KEYUP) or (event.type == KEYDOWN):
                    print event
                if event.type is MOUSEBUTTONDOWN:
                    drawProblem(ttt, board)
                    problem_count += 1    

        print "You answered " +str(selcorrect_tally)+"/"+str(problem_count)+ " correctly."
