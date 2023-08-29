import random
import re #for regex functionality

#let's create a board object to represent the minesweeper game
#this is to say that, "create a new board object", or "dig here", or "render this game for this object"
class Board:
    def __init__(self, dim_size, num_bombs):
        #keep track of these parameters. They'll be helpful later
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #let's create the board
        #we'll create the use of a helper function
        self.board = self.make_new_board() #plant bombs
        self.assign_values_to_board()

        #initialize a set to keep track of which locations we've uncovered
        #we'll save (row, col) tuples into this set
        self.dug = set() #if we dig at(0, 0), then self.dug = {0, 0} 
    
    def make_new_board(self):
        #construct a new board based on dimensions and plant bombs
        #since it is 2D, we need to create a list of lists for this

        #generate a new board, first None and then fill based on dimension size, with dim_size no. of lists
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        #creates an array like the below one
        #[[None, None, ...., None],
        # [None, None, ...., None],
        # [.....             ....],
        # [None, NOne, ...., None]] --> represents a board

        #plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs: #while loop so we only increment when you actually get something that's not a bomb yet
            loc = random.randint(0, self.dim_size**2 - 1) #planting bombs in random locations and returns random integer N as a <= N <= b
            row = loc // self.dim_size #number of times dim_size goes into loc to tell us which row to be indexed in
            col = loc % self.dim_size #tells us what index in the row to look for in the column

            if board[row][col] == '*' : #'*' represents the bombs
                #this means we've actually planted a bomb in that location so keep going
                continue

            board[row][col] = '*' #plant the bomb
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        #now that we've planted the bombs, let's assign a number 0-8 for the empty spaces which represents how many
        #neighbouring bombs there are. Better to precompute these and save effort from checking later.
        for r in range(self.dim_size): #row
            for c in range(self.dim_size): #col
                if self.board[r][c] == '*': #we're not overriding this
                    continue
                self.board[r][c] = self.get_num_neighbouring_bombs(r, c)

    def get_num_neighbouring_bombs(self, row, col):
        #let's iterate through each of neighbouring positions and sum number of bombs, & make sure we don't go out of bounds
        #top left: (row - 1, col - 1)
        #top middle: (row - 1, col)
        #top right: (row - 1, col + 1)
        #left: (row, col - 1)
        #right: (row, col + 1)
        #bottom left: (row + 1, col - 1)
        #bottom middle: (row + 1, col)
        #bottom right: (row + 1, col + 1)

        num_neighbouring_bombs = 0 #going to be our counter
        for r in range(max(0, row - 1), min(self.dim_size - 1, (row + 1)) + 1): #since range function, we need to add 1 to cover it all
            for c in range(max(0, col - 1), min(self.dim_size - 1, (col + 1)) + 1): #since we are checking all around, we get all checks of a 3x3 grid
                if r == row and c == col:
                    #original location, don't check
                    continue
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1

        return num_neighbouring_bombs 

    def dig(self, row, col):
        #dig at that location
        #return True if successful dig, False if bomb dug

        #there're a few scenarios: 
        #1> hit a bomb --> GAME OVER
        #2> dig at a location where there are neighbouring bombs --> finish dig
        #3> dig at a location where there are no neighbouring bombs --> recursively dig neighbours!

        self.dug.add((row, col)) #use a tuple to actually keep a track of where we've dug 

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        #self.board[row][col] = 0
        for r in range(max(0, row - 1), min(self.dim_size - 1, row + 1) + 1): #since range function, we need to add 1 to cover it all
            for c in range(max(0, col - 1), min(self.dim_size - 1, col + 1) + 1): #since we are checking all around, we get all checks of a 3x3 grid
                if (r,c) in self.dug:
                    continue #don't dig where already dug(duh)
                self.dig(r, c)
        
        #if our initial dig didn't hit a bomb, then we "shouldn't" hit a bomb here
        return True

    def __str__(self):
        #if you call this "magic" function, like print on this object, it'll print whatever this fn. returns!
        #return the string that shows the board to player

        #first create a new array that reps. what the user should see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)] #just create an empty board
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '

        #put it all together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep

#play the game, 1st pass dimension size and no. of bombs
def play(dim_size = 10, num_bombs = 10):
    #Step 1: create the board and plant the bombs
    board = Board(dim_size, num_bombs) #goes through initialization function etc

    #Step 2: how the user the board and ask where they wanna dig/ go, like coordinates and stuff
    #Step 3a: if a bomb is chosen, show "Game Over!"
    #Step 3b: if location is not a bomb, then dig recursively until a square is atleast next to one
    #Step 4: keep repeating steps 2 & 3 until there're no more places to dig = VICTORY! : while loop maybe

    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:  #this is a set btw, & there are empty spaces to dig that're not bombs
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: ")) #split based on ',' & '(\\s)' - any white space & '*' is 0 or more of those
        row, col = int(user_input[0]), int(user_input[-1]) #figure out this statement later
        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid location, please try again! ")
            continue

        #if it's valid, we dig
        safe = board.dig(row, col) 
        if not safe:
            #we've dug a BOMB!!!
            break #GAME OVER

    #2 ways to end the loop, let's see which one
    if safe:
        print("CONGRATS!! YOU ARE VICTORIOUS!!")
    else:
        print("SORRY, GAME OVER!")
        
        #let's reveal the whole board
        board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == "__main__": #good practice, espec. if you want to run only the current code/file
    play()

        
        

    

