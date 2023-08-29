#command line version of tic tac toe with various types of players human - h, computer - c
#h vs h; h vs c; c vs c; h as c etc
#player and game are 2 seperate classes
#therefore we can say who's playing 'x' and who's playing 'o'
import math
import random

#base player class
class Player:
    #initialize it with the letter it's going to represent
    def __init__(self, letter):
        #letter is 'x' or 'o'
        self.letter = letter

    #players should have a next move given a game
    def get_move(self, game):
        pass

#inheritance from base class, super class is player
class RandomComputerPlayer(Player):
    #need to initialize super class
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #choose a random valid spot on the board that's empty
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        #keep iterating until we reach a valid square
        valid_square = False
        val = None
        while not valid_square:
        #user should not get confused by whose turn it actually is
            square = input(self.letter + "\'s turn. Input move (0-8): ")
            #we're going to check that this is a correct value by trying to cast - 
            #it to an integer, and if it's not then we say it's invalid - 
            #if that spot is not available on the board, we also say it's invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True #if successful, then Yay!!
            except ValueError:
                print('Invalid square. Try again.')
        return val

#creating a computer okayer that literally cannot lose or atleast has only a tie.   
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    #where all the magic is going to happen
    def get_move(self, game):
        #if all the places are available, a random spot will be taken
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            #get the square off the minimax algorithm - which is recursive
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, state, player): #every iteratation of minimax, a rep/screenshot is being taken 
        max_player = self.letter 
        other_player = '0' if player == 'X' else 'X' #human player - us, the letter which is left out for us

        #first we want to check if the previous move is the winner
        #this is the base case, for recursion, we always need one to see where we are at the end
        if state.current_winner == other_player:
            #we should return the position the score because we need to keep track of the score
            #for minimax to work, so we're going to return it in a dictionary
            return {'position' : None,
                    'score' : 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * 
                        (state.num_empty_squares() + 1)                    
                    }
        
        elif not state.num_empty_squares(): #no empty squares
            return {'position' : None, 
                    'score' : 0}
        
        if player == max_player:
            best = {'position' : None,   #saves best position to move and score
                    'score' : -math.inf} #each score should maximize(be large)
        else:
            best = {'position' : None,
                    'score' : math.inf} #each score should minimize
            
        for possible_move in state.available_moves():
            #step 1 : make a move, try that spot
            state.make_move(possible_move, player)

            #step 2 : recurse using minimax to simulate a gameafter making that move
            sim_score = self.minimax(state, other_player) #now, we alternate players

            #step 3 : undo the move for future iterations
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move #otherwise it gets messed up in the recursion

            #step 4 : update the dictionary, based on the score
            if player == max_player: #trying to maximize max player
                if sim_score['score'] > best['score']:
                    best = sim_score #replace best
            else: #but minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score #replace best

        return best



        

        






