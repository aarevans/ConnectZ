#modules imported
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
file = open((args.data+".txt"),"r")

#reading all test data into a string.
data = file.read()

#converting the string in to a list and removing \n escape characters
data = data.split("\n")

#Assigning board config values, p1 turns and p2 turns to appropriate structures.
p1_moves = []
p2_moves = []
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
while len(p1_moves) > 0 or len(p2_moves) > 0:
    if current_turn % 2 == 0:
        game_board = board.UpdateBoard(int(p1_moves[0]),game_board,"p1")
        p1_moves.remove(p1_moves[0])
    else:
        game_board = board.UpdateBoard(int(p2_moves[0]),game_board,"p2")
        p2_moves.remove(p2_moves[0])
    current_turn += 1

board.DisplayBoard(game_board)