"""The board for connect 4"""

import pygame
import sys
import numpy as np


class Board:
    """Sets up the board for the game"""

    def __init__(self):

        pygame.init()

        self.ROW_COUNT = 6
        self.COLUMN_COUNT = 7
        self.board = np.zeros((self.ROW_COUNT, self.COLUMN_COUNT))

    def create_board(self):
        return np.zeros((self.ROW_COUNT, self.COLUMN_COUNT))

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def valid_location(self, col):
        return self.board[self.ROW_COUNT - 1][col] == 0 if 0 <= col < self.COLUMN_COUNT else False

    def open_row(self, col):
        for r in range(self.ROW_COUNT):
            if self.board[r][col] == 0:
                return r

    def print_board(self):
        print(np.flip(self.board, 0))

    def winning_move(self, piece):
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT):
                if (
                    self.board[r][c] == piece
                    and self.board[r][c + 1] == piece
                    and self.board[r][c + 2] == piece
                    and self.board[r][c + 3] == piece
                ):
                    return True

        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT - 3):
                if (
                    self.board[r][c] == piece
                    and self.board[r + 1][c] == piece
                    and self.board[r + 2][c] == piece
                    and self.board[r + 3][c] == piece
                ):
                    return True

        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT - 3):
                if (
                    self.board[r][c] == piece
                    and self.board[r + 1][c + 1] == piece
                    and self.board[r + 2][c + 2] == piece
                    and self.board[r + 3][c + 3] == piece
                ):
                    return True

        for c in range(self.COLUMN_COUNT - 3):
            for r in range(3, self.ROW_COUNT):
                if (
                    self.board[r][c] == piece
                    and self.board[r - 1][c + 1] == piece
                    and self.board[r - 2][c + 2] == piece
                    and self.board[r - 3][c + 3] == piece
                ):
                    return True

        return False

    def draw_board(self, screen, SQUARESIZE, RADIUS):
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT):
                pygame.draw.rect(
                    screen,
                    (0, 0, 255),
                    (
                        c * SQUARESIZE,
                        r * SQUARESIZE + SQUARESIZE,
                        SQUARESIZE,
                        SQUARESIZE,
                    ),
                )
                pygame.draw.circle(
                    screen,
                    (0, 0, 0),
                    (
                        int(c * SQUARESIZE + SQUARESIZE / 2),
                        int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2),
                    ),
                    RADIUS,
                )

        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT):
                if self.board[r][c] == 1:
                    pygame.draw.circle(
                        screen,
                        (255, 0, 0),
                        (
                            int(c * SQUARESIZE + SQUARESIZE / 2),
                            screen.get_height() - int(r * SQUARESIZE + SQUARESIZE / 2),
                        ),
                        RADIUS,
                    )
                elif self.board[r][c] == 2:
                    pygame.draw.circle(
                        screen,
                        (255, 255, 0),
                        (
                            int(c * SQUARESIZE + SQUARESIZE / 2),
                            screen.get_height() - int(r * SQUARESIZE + SQUARESIZE / 2),
                        ),
                        RADIUS,
                    )
        pygame.display.update()
