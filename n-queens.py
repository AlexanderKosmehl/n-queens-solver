def printBoard(board):
    for row in range(N):
        for col in range(N):
            print(board[row][col], end=" ")
        print()


def isSafe(row, col, rowLookup, upward_diagonals, downward_diagonals):
    if (upward_diagonals[row + col] or
            downward_diagonals[row - col + (N - 1)] or
            rowLookup[row]):
        return False
    return True

def solveNQueens(board, col, row_lookup, upward_diagonals, downward_diagonals):
    # Attempt to place "N + 1"th queen -> board contains N-queens
    if(col >= N):
        return True

	# Start queen placement columnwise from left to right
    for row in range(N):
        if(not isSafe(row, col, row_lookup, upward_diagonals, downward_diagonals)):
            continue

        # Place Queen
        board[row][col] = 1
        row_lookup[row] = True
        upward_diagonals[row + col] = True
        downward_diagonals[row - col + (N - 1)] = True

        # Recursion-Step to next queen
        if(solveNQueens(board, col + 1, row_lookup, upward_diagonals, downward_diagonals)):
            return True

        # Backtrack -> Remove queen from board and lookups
        board[row][col] = 0
        row_lookup[row] = False
        upward_diagonals[row + col] = False
        downward_diagonals[row - col + (N - 1)] = False
	
	# No feasible solution for previous queen-placement
    return False


"""
N-Queen-Solver
"""
# Board-Size
N = 4

# Initialize Board
board = [[0 for _ in range(N)] for _ in range(N)]

# Array with filled rows
row_lookup = [False for _ in range(N)]

# Keep two arrays to tell us which diagonals are occupied
number_of_diagonals = 2 * N - 1
upward_diagonals = [False for _ in range(number_of_diagonals)]
downward_diagonals = [False for _ in range(number_of_diagonals)]

# If we get a feasible solution print it
if(solveNQueens(board, 0, row_lookup, upward_diagonals, downward_diagonals)):
    printBoard(board)
# Otherwise print ...
else:
    print("Solution does not exist")