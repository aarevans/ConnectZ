# ConnectZ

Technical challenge for an interiew.

1.1 Background
This programming challenge is based on the classic game of Connect Four. In a game of Connect Four, two players take turns to drop coloured 
counters into a vertical frame. The first player to achieve a horizontal, vertical or diagonal line of four or more counters of their own colour 
wins the game. Games can also result in a draw if the frame fills up with counters before either player can complete a line of four or more counters.


1.2 Challenge
Your goal is to implement a game checker program for Connect Z. In Connect Z the concept of the traditional game of Connect Four is generalized to 
include playing frames of any size and a target lines of any length. When provided with a data file that describes a game of Connect Z your
checker program should determine if that game was won, drawn or contains an error of some kind. The format of the data files and expected output is 
described in detail below.

1.6 Output specification
•	The output of the program should be a single integer printed to standard out.
•	The integer is a code which describes the input.
•	Output codes 0 - 3 are for valid game files.
•	Output codes 4 - 9 represent errors.

The codes are defined as follows:

0	     Draw	This happens when every possible space in the frame was filled with a counter, but neither player achieved a line of the required length.!

1	     Win for player 1	The first player achieved a line of the required length.

2	    Win for player 2	The second player achieved a line of the required length.

3	    Incomplete	The file conforms to the format and contains only legal moves, but the game is neither won nor drawn by either player and there are remaining available moves in the frame. Note that a file with only a dimensions line constitues an incomplete game.

4	    Illegal continue	All moves are valid in all other respects but the game has already been won on a previous turn so continued play is considered an illegal move.

5	    Illegal row	The file conforms to the format and all moves are for legal columns but the move is for a column that is already full due to previous moves.

6	    Illegal column	The file conforms to the format but contains a move for a column that is out side the dimensions of the board. i.e. the column selected is greater than X

7	    Illegal game	The file conforms to the format but the dimensions describe a game that can never bÍ won.

8    Invalid file	The file is opened but does not conform the format.

9	    File error	The file can not be found, opened or read for some reason.
