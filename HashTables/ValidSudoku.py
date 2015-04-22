"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated. 
"""
import pprint
pp = pprint.PrettyPrinter()
board1 = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
pp.pprint(board1)

def isValidSudoku(board):
    #Check each string first (horizontal)

    for line in board:
        num_dict = {}
        for element in line:
            try:
                num_dict[element] += 1
            except KeyError:
                num_dict[element] = 1
    return num_dict
print(isValidSudoku(board1))
