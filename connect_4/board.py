"""These are the parts for the board"""

import pygame
import sys
import numpy as np
import connect_4.rgbcolors

ROW_COUNT = 6
COLUMN_COUNT = 7

class Board:
    pygame.init()

    def create_board():
        """Sets up the board layout"""
        board = np.zeros((ROW_COUNT, COLUMN_COUNT))
        return board

    def drop_piece(board, row, col, piece):
        """Drops the piece"""
        board[row][col] = piece

    def is_valid_location(board, col):
        """Checks for validation dropped"""
        return board[ROW_COUNT - 1][col] == 0

    def next_open_row(board, col):
        """Sets up the next row"""
        for row in range(ROW_COUNT):
            if board[row][col] == 0:
                return row

    def print_board(board):
        """Prints the board"""
        print(np.flip(board, 0))

    def winning_move(board, piece):
        """Checks for the win"""
        # Check horizontal locations for win
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if (
                    board[r][c] == piece
                    and board[r][c + 1] == piece
                    and board[r][c + 2] == piece
                    and board[r][c + 3] == piece
                ):
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if (
                    board[r][c] == piece
                    and board[r + 1][c] == piece
                    and board[r + 2][c] == piece
                    and board[r + 3][c] == piece
                ):
                    return True

        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if (
                    board[r][c] == piece
                    and board[r + 1][c + 1] == piece
                    and board[r + 2][c + 2] == piece
                    and board[r + 3][c + 3] == piece
                ):
                    return True

        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if (
                    board[r][c] == piece
                    and board[r - 1][c + 1] == piece
                    and board[r - 2][c + 2] == piece
                    and board[r - 3][c + 3] == piece
                ):
                    return True

    def draw_board(board):
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(
                    screen,
                    connect_4.rgbcolors.blue,
                    (
                        c * SQUARESIZE,
                        r * SQUARESIZE + SQUARESIZE,
                        SQUARESIZE,
                        SQUARESIZE,
                    ),
                )
                pygame.draw.circle(
                    screen,
                    connect_4.rgbcolors.black,
                    (
                        int(c * SQUARESIZE + SQUARESIZE / 2),
                        int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2),
                    ),
                    RADIUS,
                )

        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                if board[r][c] == 1:
                    pygame.draw.circle(
                        screen,
                        connect_4.rgbcolors.red,
                        (
                            int(c * SQUARESIZE + SQUARESIZE / 2),
                            height - int(r * SQUARESIZE + SQUARESIZE / 2),
                        ),
                        RADIUS,
                    )
                elif board[r][c] == 2:
                    pygame.draw.circle(
                        screen,
                        connect_4.rgbcolors.yellow,
                        (
                            int(c * SQUARESIZE + SQUARESIZE / 2),
                            height - int(r * SQUARESIZE + SQUARESIZE / 2),
                        ),
                        RADIUS,
                    )
        pygame.display.update()
    
class Play(Board):
    
    pygame.init()
    
    board = Board.create_board()
    game_over = False
    turn = 0
    
    SQUARESIZE = 100
    WIDTH = COLUMN_COUNT * SQUARESIZE
    HEIGHT = (ROW_COUNT + 1) * SQUARESIZE
    
    SIZE = (WIDTH, HEIGHT)
    
    RADIUS = int(SQUARESIZE/2 - 5)
    
    screen = pygame.display.set_mode((800, 600))
    Board.draw_board(board)
    pygame.display.update()
    
    font = pygame.font.Font(None, 36)
    
    while not game_over:

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
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            label = myfont.render("Player 1 wins!!", 1, RED)
                            screen.blit(label, (40,10))
                            game_over = True


                # # Ask for Player 2 Input
                else:				
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            label = myfont.render("Player 2 wins!!", 1, YELLOW)
                            screen.blit(label, (40,10))
                            game_over = True

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)