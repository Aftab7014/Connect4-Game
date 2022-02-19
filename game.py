import numpy as np

ROW_COUNT = 6
COL_COUNT = 7
open_rows = [0]*COL_COUNT

def is_valid_location(board, row, col):
    return board[row][col] == 0

def get_next_open_row(board, col):
    if col >= COL_COUNT:
        return
    curr_row = open_rows[col]
    if curr_row < ROW_COUNT:
        open_rows[col] = curr_row + 1
        return curr_row
    return -1

def drop_piece(r, c, piece):
    board[r][c] = piece

def create_board():
    board = np.zeros((6,7))
    return board

def print_board(board):
    print(np.flip(board,0))
# initialize board
board = create_board()
print_board(board)
game_over = False
turn = 0 # whose turn is it? player 0 or 1?

while not game_over:
    #Player 0 input
    print(f"Player {turn}, Make your Selection(0-6):")
    col = int(input())
    row = get_next_open_row(board, col);
    if row>=0 and is_valid_location(board, row, col):
        drop_piece(row, col, 1)
    print_board(board)
    turn += 1
    turn = turn % 2






