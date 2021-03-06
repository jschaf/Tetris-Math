'''A game board for equations.
'''
import random
from equation import int_from_digits, Equation

class Board(object):
    '''A board to hold the game state.  Equations start at the top
    (defined as 0) and progress down the screen at the rate defined by
    drop_speed.  When the equation hits the bottom or the stack of
    dead equations a new dead equation is created.  When
    '''
    def __init__(self, window_size):
        self.width, self.height = window_size
        self.dead_eqns = []
        self.current_eqn = Equation(0)
        self.problem_count = 1
        self.current_input = []
        self.correct_tally = 0
        self.eqn_xpos, self.eqn_ypos = (0,0)
        self.display_correct = False
        self.display_incorrect = False
        
    def next_eqn(self):
        self.current_eqn = Equation(0)
        self.problem_count += 1
        self.current_input = []
        self.display_correct = False
        self.display_incorrect = False
        
    def has_correct_guess(self):
        '''Return if the current_input matches the answer.'''
        guess = int_from_digits(self.current_input)
        return self.current_eqn.answer == guess

    def check_ans(self):
        pass

    def update(self):
        '''Update the board state.'''
        raise NotImplementedError

class StaticBoard(Board):
    def __init__(self, window_size):
        super(StaticBoard, self).__init__(window_size)
        self.eqn_xpos, self.eqn_ypos = (130, 200)
        self.mode = "static"
        
    def check_ans(self):
        if self.display_correct or self.display_incorrect:
            if self.problem_count == 10:
                self.mode = "game_over"
            else:    
                self.next_eqn()
        else:
            if self.has_correct_guess():
                self.display_correct = True
                self.correct_tally += 1
           
            else:
                self.display_incorrect = True

    def update(self):
        pass

class DynamicBoard(Board):
    def __init__(self, window_size):
        super(DynamicBoard, self).__init__(window_size)
        self.drop_speed = 2
        self.explode_animation_frame = 0
        self.NUM_EXPLODE_FRAMES = 20
        self.DEAD_EQN_HEIGHT = 80
        self.kill_height = 80
        self.eqn_xpos, self.eqn_ypos = (130, 0)
        self.mode = "falling"
        self.level =  1
        self.consecutive = 0
        
    def next_eqn(self):
        super(DynamicBoard, self).next_eqn()
        self.eqn_ypos = 0
        
    def next_level(self):        
        self.level += 1
        self.drop_speed += 0.5
        self.correct_tally = 0
        self.consecutive = 0
        self.dead_eqns = []
        self.mode = 'falling'
        print self.mode

    def kill_current_eqn(self):
        '''If the equation reaches the bottom of the dead equations
        then blow it up.'''
#        self.current_eqn.is_dead = True
        self.dead_eqns.append(self.current_eqn)
        self.kill_height = (len(self.dead_eqns)+1) * self.DEAD_EQN_HEIGHT
#        self.problem_count += 1
#        self.mode = "exploding"

    def remove_dead(self):
        if len(self.dead_eqns) > 0:
            del self.dead_eqns[0]

    def increase_drop_speed(self):
        '''Increase the rate at which the equations fall.'''
        self.drop_speed += 1
        
    def check_ans(self):
        if self.has_correct_guess():
            self.correct_tally += 1
            self.consecutive += 1
            if self.correct_tally == 15:
                self.mode = 'level_break'
            elif self.consecutive == 4:
                self.remove_dead()
                self.consecutive = 0           
        else:
            self.kill_current_eqn()
            self.consecutive = 0
            
        self.next_eqn()

    def update(self):
        '''Update the board state.'''
        if self.mode == 'exploding':
            if self.explode_animation_frame > self.NUM_EXPLODE_FRAMES:
                self.explode_animation_frame = 0
                self.mode = 'falling'
                self.current_eqn = Equation(0)
            else:
                self.explode_animation_frame += 1

        elif self.mode == 'falling':
            self.eqn_ypos += self.drop_speed
            
            if ((self.height - self.kill_height) <= self.eqn_ypos):
                self.kill_current_eqn()                
                
                if self.kill_height >= self.height:
                    self.mode = "game_over"
                else:
                    self.next_eqn()

