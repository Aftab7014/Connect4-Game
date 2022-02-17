import numpy as np

def create_board():
    board = np.zeros((6,7))
    return board

# initialize board
board = create_board()

game_over = False
turn = 0 # whose turn is it? player 0 or 1?

while not game_over:
    #Player 0 input
    print(f"Player {turn}, Make your Selection(0-6):")
    turn += 1
    turn = turn % 2
    




