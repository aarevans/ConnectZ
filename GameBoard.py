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
    def LegalRow(this,board,move):
        for count in range (len(board[0])-1):
            if board[count][int(move)-1] == 0:
                #print(board[count][int(move)-1])
                return True

    def LegalColumn(this,move):
        if move > this.columns:
            return False
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
        p1_point_count = 0
        p2_point_count = 0
        
        #checks for win condition along rows.
        while True:
            for count in range(len(board[0])):
                for item in board[count]:
                    if item == "p1":
                        p1_point_count += 1
                        if p1_point_count == int(this.target):
                            return True
                    elif item == "p2":
                        p2_point_count += 1
                        if p2_point_count == int(this.target):
                            return True
                p1_point_count = 0
                p2_point_count = 0
            
            #checks for win condition in columns
            for count in range (len(board[0])):
                for count2 in range(len(board)):
                    if board[count2][count] == "p1":
                        p1_point_count += 1
                        if p1_point_count == int(this.target):
                            return True
                    elif board[count2][count] == "p2":
                        p2_point_count += 1
                        if p2_point_count == int(this.target):
                            return True
                p1_point_count = 0
                p2_point_count = 0

            #return false value if no win condition found
            return False