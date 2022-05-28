class Board:
    #Constructor
    def __init__(this,board_config):
        this.columns, this.rows, this.target = board_config.split(" ")

    def CreateBoard(this):
        board = [[0] * int(this.columns) for i in range(int(this.rows))]
        return board

    def LegalMoveCheck(this):
        pass

    def UpdateBoard(this,move,board,player):
        scenario = 1
        while scenario <= this.columns:
            for y in range(len(board[0])-1, -1, -1):
                if board[move-1][y] == 0:
                    board[move-1][y] = player
                    return board
        else:
            print("Something has gone wrong")

    def WinCheck(this):
        pass


    