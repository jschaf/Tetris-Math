# Tetris Math prototype

# import necessary modules
import pygame
from pygame.locals import *
import random

# defined so it can be a global variable used by 2 functions
correctTally = 0


# initialize the surface('board') and return it as a variable
# ---------------------------------------------------------------
# ttt : a properly initialized pyGame display variable
def initBoard(ttt):
    
    # set up the background surface
    background = pygame.Surface (ttt.get_size())
    background = background.convert()
    background.fill ((250, 250, 250))

    # return the board
    return background

# draws the problem in the window and also puts it on the command line
def drawProblem(ttt, board):

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

    ttt.blit (board, (0, 0))
    pygame.display.flip()

    global correctTally

    print str(a)+ " + " +str(b)+ " = "
    # ans = input()
    # if (a + b == ans):
    #     print "Correct!"
    #     correctTally += 1
    # else:
    #     print "Incorrect: "+str(a)+" + "+str(b)+" = "+str(a+b)

# This function provides a loop and variables to keep displaying math problems.
def doProblems(ttt, board):
    #global variable that tracks how many questions have been answered correctly
    global correctTally
    correctTally = 0
    
    # here is a good place to start implementing MVC at some point
    drawProblem(ttt, board) #start with a problem on the screen
    problemCount = 1
    while (problemCount < 10): #loop that waits for a click, then displays the next problem
        drawProblem(ttt,board)
        problemCount += 1
        # ??? this was for debugging, but when I commented it out, the gui wouldn't update with the command line
        for event in pygame.event.get():
            if (event.type == KEYUP) or (event.type == KEYDOWN):
                print event
            if event.type is MOUSEBUTTONDOWN:
                drawProblem(ttt, board)
                problemCount += 1    
  
    print "You answered " +str(correctTally)+"/"+str(problemCount)+ " correctly."


# --------------------------------------------------------------------
# initialize pygame and our window
pygame.init()
ttt = pygame.display.set_mode ((400, 450))
pygame.display.set_caption ('Tetris Math')

# surface where problems are displayed
board = initBoard(ttt)

# main event loop
running = True

while running:
    for event in pygame.event.get():
        if event.type is QUIT:
            running = False

        doProblems(ttt,board)
