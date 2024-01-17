
def find_next_empty(puzzle):
    #find the next row,col in the puzzle which are not filled yet
    # we are considering a 9 by 9 grid
    # we access a location by (row,col) 
    # each empty square is represented by -1

    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==-1:
                return (r,c)
    return (None,None) #No more empty spaces

def is_valid(puzzle,guess,row,col):
    #return True if it is valid, otherwise False

    row_val=puzzle[row]
    if guess in row_val:
        return False
    
    col_val=[puzzle[i][col] for i in range(9)]
    if guess in col_val:
        return False
    
    row_start=(row//3)*3
    col_start=(col//3)*3

    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[r][c]==guess:
                return False
    return True



def solve(puzzle):
    row,col=find_next_empty(puzzle)

    if row == None:
        return True
    #if there is an empty space, guess a number between 1-9

    for guess in range(1,10):
        #check if this is a valid guess

        if is_valid(puzzle,guess,row,col):
            puzzle[row][col]=guess

            if solve(puzzle):
                return True
            
        puzzle[row][col]=-1 #if the guess is wrong, reset the value

    return False #when the puzzle is unsolvable


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
    print(solve(example_board))
    print(example_board)