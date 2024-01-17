import random
import re

class Board():
    def __init__(self,size,no_of_bombs):
        self.dim_size=size
        self.no_of_bombs=no_of_bombs
        self.board=self.make_new_board()
        self.assign_values_to_bombs()

        #history of all the dug holes
        self.dug=set()

    def make_new_board(self):
        board=[[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]

        #plant the bombs
        bombs_planted=0
        while bombs_planted<self.no_of_bombs:
            loc=random.randint(0,self.dim_size**2-1)
            row = loc//self.dim_size
            col = loc%self.dim_size

            if board[row][col] == '*': #'*' is a bomb
                continue

            board[row][col] = '*' #plant the bomb
            bombs_planted+=1

        return board
    
    def assign_values_to_bombs(self):

        for r in range(self.dim_size):
            for c in range(self.dim_size):

                if self.board[r][c] == '*':
                    continue

                self.board[r][c] = self.get_no_neighbor_bombs(r,c)

    def get_no_neighbor_bombs(self,row,col):

        #[1 2 3
        # 4 5 6
        #  7 8 9] 5 is our cuurent loc. we are going to search for all other locations
        no_neighbor_bombs=0
        for r in range(max(0,row-1), min(self.dim_size-1,row+2)):
            for c in range(max(0,col-1), min(self.dim_size-1,col+2)):
                if r==row and c==col:
                    continue
                if self.board[r][c] == '*':
                    no_neighbor_bombs+=1

        return no_neighbor_bombs

    def dig(self,row,column):

        self.dug.add((row,column))

        if self.board[row][column] == '*':
            return False #you hit a bomb
        
        elif self.board[row][column]>0:
            return True
        
        #self.board[row][column]==0

        for r in range(max(0,row-1), min(self.dim_size-1,row+2)):
            for c in range(max(0,column-1), min(self.dim_size-1,column+2)):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)

        return True
    
    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        show_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    show_board[row][col] = str(self.board[row][col])
                else:
                    show_board[row][col] = ' '
        
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], show_board)
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
            cells.append(format % str(col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(show_board)):
            row = show_board[i]
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



#Play the game
def play(size=10, no_of_bombs=10):
    #1. create the board and plant the bombs
    #2. show the board to a player and ask where to dig
    #3.a. if location is a bomb, game over!
    #3.b. if not, deep recursively until every square is at least to a bomb
    #4. repeat steps 2 and 3 until there are no place to dig -> victory!
    board=Board(size,no_of_bombs)
    result=True

    while len(board.dug)<board.dim_size**2-no_of_bombs:
        print(board)
        Input=re.split(',(\\s)*',input('Enter the location to dig :'))
        row,col=int(Input[0]),int(Input[-1])
        if row<0 or row>=board.dim_size or col<0 or col>=board.dim_size:
            print('Invalid Location❌. Try again')
            continue
        
        result=board.dig(row,col)
        if not result:
            break

    if result:
        print('Congratulation!!!You Won🚀')

    else:
        print('You Lost😢 Try again')

    board.dug=[(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
    print(board)


# board=Board(10,20)
# print(board.assign_values_to_bombs())

if __name__=='__main__':
    play()