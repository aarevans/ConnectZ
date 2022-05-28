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

    def CreateBoard(this):
        board = [[0] * int(this.columns) for i in range(int(this.rows))]
        return board

    def DisplayBoard(this,board):
        for line in board:
            print (line)


    #return True or False value if move is legal or not.
    def LegalMoveCheck(this):
        #needs implementing
        return True

    #return True of False value if incomplete/impossible game scenario or not.
    def Valid(this):
        pass

    #updates game board based of player move, fills in the table from the bottom.
    def UpdateBoard(this,move,board,player):
        while True:
            for y in range(len(board[0])-1, -1, -1):
                if board[y][move-1] == 0:
                    board[y][move-1] = player
                    return board
                

    def WinCheck(this):
        pass


    