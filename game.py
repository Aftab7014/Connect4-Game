import numpy as np
import pygame
import sys
import math
import time


BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COL_COUNT = 7
open_rows = [0]*COL_COUNT

def create_board():
    board = np.zeros((ROW_COUNT,COL_COUNT))
    return board

def drop_piece(r, c, piece):
    board[r][c] = piece

def is_valid_location(board, col):
    # if last row is having zero at col, then it's valid.
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    if col >= COL_COUNT:
        return
    curr_row = open_rows[col]
    if curr_row < ROW_COUNT:
        open_rows[col] = curr_row + 1
        return curr_row
    return -1

def print_board(board):
    print(np.flip(board,0))

def winning_move(board, piece):
    # check horizontal location to win
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] == piece:
                return True

    # Check vertical location to win
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COL_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COL_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            # position and dimension of the rectangle (in order*)
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            # pygame.display.update()
            # time.sleep(4)
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()

# initialize board
board = create_board()
print_board(board)
game_over = False
turn = 0 # whose turn is it? player 0 or 1?

#initalize pygame
pygame.init()

#define our screen size
SQUARESIZE = 100

#define width and height of board
width = COL_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)
RADIUS = int(SQUARESIZE/2 - 5)
screen = pygame.display.set_mode(size)

#Calling function draw_board again
draw_board(board)
pygame.display.update()

# Forn and size used from system fonts, used for displaying message to winner.
myfont = pygame.font.SysFont("monospace", 75)

while not game_over:
    # get all events in the queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            #print(event.pos)
            # Ask for Player {turn+1} Input
            posx = event.pos[0]
            col = int(math.floor(posx/SQUARESIZE))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(row, col, turn+1)

                if winning_move(board, turn+1):
                    label = myfont.render("Player 2 wins!!", 1, YELLOW) if turn else myfont.render("Player 1 wins!!", 1, RED)
                    screen.blit(label, (40,10))
                    game_over = True

            print_board(board)
            draw_board(board)

            turn += 1
            turn = turn % 2

            if game_over:
                pygame.time.wait(3000)
