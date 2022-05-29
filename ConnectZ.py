##modules imported
import argparse
import sys

#classes imported
from GameBoard import *

# ***Start of arg code***
#generate a parser object from argparse 
parser = argparse.ArgumentParser()

#assign command line arg as data
parser.add_argument("data")

#handle error message if no arg given and exits with message
if len(sys.argv)==1:
    print("connectz.py: Provide one input file")
    sys.exit(1)

#stores arg in args namespace.
args=parser.parse_args()

# ***End of arg code***

# ***Start of handling test data code***
#rconcatenate the file extension to the file name and then open in read mode.
#exception handling catches if file cannot be found
try:
    file = open((args.data+".txt"),"r")
except IOError:
    print(9)
    sys.exit()

#reading all test data into a string.
data = file.read()

#converting the string in to a list and removing \n escape characters
data = data.split("\n")

#Assigning board config values, p1 turns and p2 turns to appropriate structures.
p1_moves = []
p2_moves = []

#catches invalid files with board config but no moves.
if len(data) == 1:
    print(8)
    sys.exit()

#assigns each move to relevant lists, assuming that p1 goes first.
for x in range(len(data)):
    if x == 0:
        board_config = data[x]
    elif x % 2 == 1:
        p1_moves.append(data[x])
    else:
        p2_moves.append(data[x])

# ***End of handling test data code.***

#create a new board object from the Board class
board = Board(board_config)

#using the CreateBoard() method on the board object a new 2d list is generated and returned for the 
#game board using the board_config dimensions.
game_board = board.CreateBoard()


#turn based system using MOD to see if its p1 or p2 turn and then removing moves once used from move lists.
#when there are no turns left for either player the loop finishes and game ends.
current_turn = 0
turn_limit = int(board.columns) * int(board.rows)

#ensures that the game only plays while there are moves remaining
while len(p1_moves) > 0 or len(p2_moves) > 0:

    #p1 goes first
    if current_turn % 2 == 0:
        
        #checks that the next move is within row/column limits and that the column is not full
        if board.LegalColumn(p1_moves[0]) == True and board.FullColumn(game_board,p1_moves[0]) == True:
            game_board = board.UpdateBoard(int(p1_moves[0]),game_board,"p1")
            p1_moves.remove(p1_moves[0]) #remove the move that has just been used
            #only gives a p1 win if all moves have been used (otherwise continue error given)
            if board.WinCheck(game_board) == True and len(p2_moves)==0 and len(p1_moves)==0:
                print(1) 
                sys.exit()
            #continue code output and game finished
            elif board.WinCheck(game_board) == True:
                print(4)
                sys.exit()
        #outputs correct code is move is not within column boundaries.
        elif board.LegalColumn(p2_moves[0]) == False:
            print(6)
            sys.exit()
        #outputs correct code is column is full
        else:
            print(5)
            sys.exit()

    #p2 code mirrors p1 code above
    elif current_turn % 2 == 1:
        if board.LegalColumn(p2_moves[0]) == True and board.FullColumn(game_board,p2_moves[0]) == True:
            game_board = board.UpdateBoard(int(p2_moves[0]),game_board,"p2")
            p2_moves.remove(p2_moves[0])
            if board.WinCheck(game_board) == True and len(p2_moves)==0 and len(p1_moves)==0:
                print(2)
                sys.exit()
            elif board.WinCheck(game_board) == True:
                print(4)
                sys.exit()
        elif board.LegalColumn(p2_moves[0]) == False:
            print(6)
            sys.exit()
        else:
            print(5)
            sys.exit() 

    #increment the current turn after each turn.
    current_turn += 1

#handles draws
if current_turn == turn_limit:
    print(0)
    sys.exit()
#handles incomplete game
elif current_turn < turn_limit:
    print(3)
    sys.exit()

    