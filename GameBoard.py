import sys

class Board:
    #Constructor
    def __init__(this,board_config):
        #catches files with invalid format
        try:
            this.columns, this.rows, this.target = board_config.split(" ")
        except ValueError:
            print(8)
            sys.exit()

        if int(this.columns) < int(this.target) and int(this.rows) < int(this.target):
            print(7)
            sys.exit()
        
    #creates a new board 2dlist using the board_config values
    def CreateBoard(this):
        board = [[0] * int(this.columns) for i in range(int(this.rows))]
        return board

    #for testing delete before sending.
    def DisplayBoard(this,board):
        for line in board:
            print (line)


    #return True or False value if move is legal or not.
    def FullColumn(this,board,move):
        for count in range (len(board[0])-1):
            if board[count][int(move)-1] == 0:
                return True
            else:
                print(5)
                sys.exit()

    def LegalColumn(this,move):
        if int(move) > int(this.columns):
            return False
        else:
            return True
        
    #return True of False value if incomplete/impossible game scenario or not.
    def Impossible(this):
        if this.columns > this.target:
            return False
        elif this.rows > this.target:
            return False
        return True
        

    #updates game board based of player move, fills in the table from the bottom.
    def UpdateBoard(this,move,board,player):
        while True:
            for y in range(len(board[0])-1, -1, -1):
                if board[y][move-1] == 0:
                    board[y][move-1] = player
                    return board
                

    #method to return true or false depending on whether a win condition has been met.
    def WinCheck(this,board):
        #to begin the board needs to be analsed
        max_col = len(board[0])
        max_row = len(board)
        #empty 2dlists created to store all possible columns, rows, forward diagonals and backwards diagonals
        cols = [[] for _ in range(max_col)]
        rows = [[] for _ in range(max_row)]
        fdiag = [[] for _ in range(max_row + max_col - 1)]
        bdiag = [[] for _ in range(len(fdiag))]
        min_bdiag =- max_row + 1

        #appropriate values appended to the above made 2d lists
        for x in range(max_col):
            for y in range(max_row):
                cols[x].append(board[y][x])
                rows[y].append(board[y][x])
                fdiag[x+y].append(board[y][x])
                bdiag[x-y-min_bdiag].append(board[y][x])

        p1_point_count = 0
        p2_point_count = 0        

        while True: 
            #Columns analsed for win conditions.
            for col in cols:
                for element in col:
                    if element == "p1":
                        p1_point_count += 1
                        if p1_point_count == int(this.target):
                            return True   
                p1_point_count = 0
            
            for col in cols:
                for element in col:
                    if element == "p2":
                        p2_point_count += 1
                        if p2_point_count == int(this.target):
                            return True    
                p2_point_count = 0
           
            #Rows analsed for win conditions.
            for row in rows:
                for element in row:
                    if element == "p1":
                        p1_point_count += 1
                        if p1_point_count == int(this.target):
                            return True
                p1_point_count = 0
            
            for row in rows:
                for element in row:
                    if element == "p2":
                        p2_point_count += 1
                        if p2_point_count == int(this.target):
                            return True
                p2_point_count = 0

            #forward diagonals analsed for win conditions.
            for diag in fdiag:
                for element in diag:
                    if element == "p1":
                        p1_point_count += 1
                        if p1_point_count == int(this.target):
                            return True
                p1_point_count = 0

            for diag in fdiag:
                for element in diag:
                    if element == "p2":
                        p2_point_count += 1
                        if p2_point_count == int(this.target):
                            return True
                p2_point_count = 0

            #backwards diagonals analsed for win conditions.
            for diag in bdiag:
                for element in diag:
                    if element == "p1":
                        p1_point_count += 1
                        if p1_point_count == int(this.target):
                            return True
                p1_point_count = 0

            for diag in bdiag:
                for element in diag:
                    if element == "p2":
                        p2_point_count += 1
                        if p2_point_count == int(this.target):
                            return True
                p2_point_count = 0
            
            #False value returned if no win condition found.
            return False