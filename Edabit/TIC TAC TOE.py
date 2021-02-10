"""
Given a 3x3 matrix of a completed tic-tac-toe game, 
create a function that returns whether the game is a win for "X", "O", or a "Draw", 
where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.

Examples
tic_tac_toe([
  ["X", "O", "X"],
  ["O", "X",  "O"],
  ["O", "X",  "X"]
]) ➞ "X"

tic_tac_toe([
  ["O", "O", "O"],
  ["O", "X", "X"],
  ["E", "X", "X"]
]) ➞ "O"

tic_tac_toe([
  ["X", "X", "O"],
  ["O", "O", "X"],
  ["X", "X", "O"]
]) ➞ "Draw"

Notes:
Make sure that if O wins, you return the letter "O" and 
not the integer 0 (zero) and if it's a draw, 
make sure you return the capitalised word "Draw". 
If you return "X" or "O", make sure they're capitalised too.
"""

# Hard coded way or way without using Numpy array functions
def tic_tac_toe(array):
    conditions_X = [(array[0][0]==array[1][1]==array[2][2]=="X"),
                    (array[0][2]==array[1][1]==array[2][0]=="X"),
                    (array[0][0]==array[1][0]==array[2][0]=="X"),
                    (array[0][1]==array[1][1]==array[2][1]=="X"),
                    (array[0][2]==array[1][2]==array[2][2]=="X")]
    
    conditions_O = [(array[0][0]==array[1][1]==array[2][2]=="O"),
                    (array[0][2]==array[1][1]==array[2][0]=="O"),
                    (array[0][0]==array[1][0]==array[2][0]=="O"),
                    (array[0][1]==array[1][1]==array[2][1]=="O"),
                    (array[0][2]==array[1][2]==array[2][2]=="O")]
    
    try:
        for i in range(3):
            if array[i]==list("X"*3) or any(conditions_X):
                return "X"
            elif array[i]==list("O"*3) or any(conditions_O):
                return "O"
            else:
                continue
        return "Draw"
    except IndexError:
        return "Only 3x3 matrix is allowed !"

print(tic_tac_toe([ ['X', 'O', 'X'], \
                    ['O', 'X', 'O'], \
                    ['O', 'X', 'O']]))
