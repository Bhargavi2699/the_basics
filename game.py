import math
import time
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #9 because 3x3 board, we will assign an index to each space 
        self.current_winner = None #to check if there is any winner in the game
        
    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]: #splitting it into rows
            print('| ' + ' | '.join(row) + ' |') #join them in the string where the seperator is the vertical line

    @staticmethod #doesn't relate to any specific board, we do not have to pass in a 'self' 
    def print_board_nums():
        #print out which numbers corresponsd to which spot
        #0 | 1 | 2 - tells us what numbers correspond to  what box
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    #see what moves are available to be made
    def available_moves(self):
        #another way to write this, condensing below for loop into 1 line
        return [i for i, spot in enumerate(self.board) if spot == ' '] 
        
        #one way to write this
        #return []
        # moves = []
        # for (i, spot) in enumerate(self.board): #essentially creating a list and assign tuples that have index, value at index
            #['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            #we are going to go into each of these tuples
            #first item to i and second to spot
            # if spot == ' ': #checking if the space is empty
            #     moves.append(i)
            # return moves

    def empty_squares(self):
        return ' ' in self.board #return boolean values
        
    def num_empty_squares(self):
        return self.board.count(' ')
        
        #defining function to actually make a move
    def make_move(self, square, letter):
        #if the move the player makes is valid, then move to appropriate square and assign it to letter
        #it becomes True then, else it's False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    #create function to actually check for a winner
    def winner(self, square, letter):
        #winner is when there's a sequence of 3 in a row. We do need to check it though
        #first let's check row
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3] #going to be a list of items in the row that we selected
        if all([spot == letter for spot in row]): #basically checks if all is True, else returns False
            return True
        
        #check column
        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)] #add column index, we get every single value in the row
        if all([spot == letter for spot in column]): #basically checks if all is True, else returns False
            return True
        
        #check diagonal
        #check with squares of even number [0, 2, 4, 6, 8]
        #these are the only moves possible to win in a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]): #basically checks if all is True, else returns False
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]): #basically checks if all is True, else returns False
                return True
            
        #if all the above checks fail
        return False
        
def play(game, x_player, o_player, print_game = True): 
    #returns the winner if there is one(the letter) or None
    #print_game if True, prints out all the steps
    #if c vs c, then no need to print out the game, we can toggle to False
    if print_game:
        game.print_board_nums()

    letter = 'X' #starting letter....for now I guess
    #iterate when we have empty squares
    #we don't have to worry about winner because we'll return to it later -
    #this will break the loop

    while game.empty_squares():
        #get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #defining function to actually make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}.")
                game.print_board() #printing the board
                print(' ')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter #ends loop and exits game
                
            #after we make our move, we need to assign alternate letter
            letter = 'O' if letter == 'X' else 'X'

            #basically the above statement means:
            # if letter == 'X':
            #     letter = 'O'
            # else:
            #     letter = 'X'

        #tiny break to make things easier
        if print_game:
            time.sleep(0.8)

    if print_game:
            print("It's a tie!")

if __name__ == "__main__":
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(1000):
        x_player = RandomComputerPlayer('X')
        o_player = GeniusComputerPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game = False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1
    
    print(f"After 1000 iterations, we see {x_wins} X wins, {o_wins} O wins, and {ties} ties.")
        
        










