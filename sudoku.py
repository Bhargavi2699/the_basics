from pprint import pprint
#recursion to solve a valid sudoku puzzle
def find_next_empty(puzzle):
    #finds the next row, col on the puzzle that is not filled yet --> represent it with -1
    #return row, col tuple (or (None, None) if there is None)
    
    #remember - we are using 0 indexing, i.e, 0 - 8 for our indices
    for r in range(9): #range is 0 - 8
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
            
    return None, None #if no spaces in the puzzle remain (-1)

def is_valid(puzzle, guess, row, col):
    #checks if guess is valid at that row/col, returns True or False accordingly
    #every index in our puzzle starts with row, so we start with that(lol)

    #let's start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    #cols are a bit more tricky
    col_vals = []
    for i in range(9):
        col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    #and then the square, this is kinda sorta tricky
    #we want to get where the 3x3 square starts, & iterate over the 3 values in row/col
    row_start = (row // 3) * 3 #1 // 3 = 0, 5 // 3 = 1...to find out which square it's in, and to get the actual index we * 3; 
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3): #since we want to iterate across 3 rows
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    #if we get here, True
    return True
                 

def solve_sudoku(puzzle):
    #solve sudoku using a backtracking technique
    #this is for a list of lists where each list is a row of the sudoku puzzle....thingy
    #returns whether a solution exists
    #remember that lists are mutable(changeable), so we need to mutate the puzzleto be the soln.(if it exists)

    #step 1: choose somewhaere on a puzzle to make a guess
    row, col = find_next_empty(puzzle)

    #step 1a: if no spaces are left, then we're done because only valid i/ps are allowed
    #it's enough to check the row alone, coz if row is None, then we filled it all
    if row is None:
        return True

    #step 2: if there's place remaining, enter a number from 1 - 9
    for guess in range(1, 10): #range is 1 - 9
        #step 3: check if it's a valid guess or not
        if is_valid(puzzle, guess, row, col): #since these 4 are the parameters we need to check for validity
            #step 3a: if this is valid, then place the pieces on the puzzle
            puzzle[row][col] = guess
            #now use recursion for this
            #step 4: recursively call the function
            if solve_sudoku(puzzle):
                return True
            
        #step 5: if not valid OR if our guess does not solve the puzzle, we need to backtrack and try a new number
        puzzle[row][col] = -1 #reset the guess

    #step 6: if none of the numbers work, that means this puzzle is UNSOLVABLE
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)




