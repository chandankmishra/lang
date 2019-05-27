def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()


# 
# Your previous Plain Text content is preserved below:
# 
# An 8-puzzle is an old game where we’re given a 3x3 board of tiles with the 9th tile missing. The tiles have a number on them 1 through 8, and each puzzle starts out shuffled. Tiles may slide into the empty space (horizontally or vertically), but no tile may be removed from the board.
# 
# 
# # +---+---+---+ 
# # | 1 | 2 | 3 |
# # +---+---+---+
# # | 8 |   | 5 |
# # +---+---+---+
# # | 4 | 7 | 6 |
# # +---+---+---+ 
# 
# 
# End state:
# # +---+---+---+ 
# # | 1 | 2 | 3 |
# # +---+---+---+
# # | 4 | 5 | 6 |
# # +---+---+---+
# # | 7 | 8 |   |
# # +---+---+---+
# 
# 

class Board:
    def __init__(self, arr):
        self.board = arr
        # for row in arr:
        #     self.board += row
        # self.size = len(self.board)
        # self.moves = [[1, 3], [], [], [], [1, 3, 5, 7], [], [], [], []]
        self.start_row = 0
        self.start_col = 0
        self.rows = len(arr)
        self.cols = len(arr[0])
        
        self.dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]] # up right down left 
        for row in range(self.rows):
            for col in range(self.cols):
                if arr[row][col] == None:
                    self.start_row = row
                    self.start_col = col
                    break
        self.end_str = "12345678X"

    def is_end_state(self, board):
        new_list = []
        for row in range(self.rows):
            for col in range(self.cols):
                new_list.append(board[row][col])
        new_str = ''.join(new_list)
        
        return new_str == self.end_str
        
        
    def is_valid(self, row, col):
        if not ( 0 <= row < self.rows and 0 <= col < self.cols):
            return False
        
        return True
    

    def move(self, row, col, direction):
        row_change, col_change = self.dirs[direction]
        new_row, new_col = row + row_change, col + col_change
        
        if not self.is_valid(new_row, new_col):
            return None
        
        new_board = []
        for row in self.board:
            new_board.append(list(row))
            
        new_board[row][col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[row][col]    
        return new_board
    
    def solve(self):
        
    
    
    
        
        
        
    
    
