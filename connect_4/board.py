"""The board for connect 4"""

import pygame
import numpy as np
import connect_4.rgbcolors


class Board:
    """Sets up the board for the game"""

    def __init__(self):
        pygame.init()

        self.ROW_COUNT = 6
        self.COLUMN_COUNT = 7
        self.board = np.zeros((self.ROW_COUNT, self.COLUMN_COUNT))

        self.SQUARESIZE = 100
        self.width = self.COLUMN_COUNT * self.SQUARESIZE
        self.height = (self.ROW_COUNT + 1) * self.SQUARESIZE

    def create_board(self):
        """Creating the board layout"""
        return np.zeros((self.ROW_COUNT, self.COLUMN_COUNT))

    def drop_piece(self, row, col, piece):
        """Handles when a piece is dropped"""
        self.board[row][col] = piece

    def valid_location(self, col):
        """Checks for a valid location if a piece is dropped"""
        return isinstance(col, int) and 0 <= col < self.COLUMN_COUNT and self.board[self.ROW_COUNT - 1, col] == 0
        # return 0 <= col < self.COLUMN_COUNT and self.board[self.ROW_COUNT - 1][col] == 0

    def open_row(self, col):
        """Checks for the next open row"""
        for r in range(self.ROW_COUNT):
            ex = (self.board[r][col] == 0).all()
            if ex:
                return r

    def print_board(self):
        """Prints the board on the terminal"""
        print(np.flip(self.board, 0))
        print("")

    def winning_move(self, piece):
        """Checks for the winning piece"""

        # checks for horizontal
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT):
                if (
                    self.board[r][c] == piece
                    and self.board[r][c + 1] == piece
                    and self.board[r][c + 2] == piece
                    and self.board[r][c + 3] == piece
                ):
                    return True

        # checks for vertical
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT - 3):
                if (
                    self.board[r][c] == piece
                    and self.board[r + 1][c] == piece
                    and self.board[r + 2][c] == piece
                    and self.board[r + 3][c] == piece
                ):
                    return True

        # checks for right diagnol
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(self.ROW_COUNT - 3):
                if (
                    self.board[r][c] == piece
                    and self.board[r + 1][c + 1] == piece
                    and self.board[r + 2][c + 2] == piece
                    and self.board[r + 3][c + 3] == piece
                ):
                    return True

        # checks for left diagnol
        for c in range(self.COLUMN_COUNT - 3):
            for r in range(3, self.ROW_COUNT):
                if (
                    self.board[r][c] == piece
                    and self.board[r - 1][c + 1] == piece
                    and self.board[r - 2][c + 2] == piece
                    and self.board[r - 3][c + 3] == piece
                ):
                    return True

    def draw_board(self, screen, RADIUS):
        """Draws the board on screen"""
        # board drawing
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT):
                pygame.draw.rect(
                    screen,
                    connect_4.rgbcolors.blue,
                    (
                        c * self.SQUARESIZE,
                        r * self.SQUARESIZE + self.SQUARESIZE,
                        self.SQUARESIZE,
                        self.SQUARESIZE,
                    ),
                )
                pygame.draw.circle(
                    screen,
                    connect_4.rgbcolors.light_blue,
                    (
                        int(c * self.SQUARESIZE + self.SQUARESIZE / 2),
                        int(
                            r * self.SQUARESIZE + self.SQUARESIZE + self.SQUARESIZE / 2
                        ),
                    ),
                    RADIUS,
                )

        # player pieces
        for c in range(self.COLUMN_COUNT):
            for r in range(self.ROW_COUNT):
                if self.board[r][c] == 1:
                    pygame.draw.circle(
                        screen,
                        connect_4.rgbcolors.red,
                        (
                            int(c * self.SQUARESIZE + self.SQUARESIZE / 2),
                            screen.get_height()
                            - int(r * self.SQUARESIZE + self.SQUARESIZE / 2),
                        ),
                        RADIUS,
                    )
                elif self.board[r][c] == 2:
                    pygame.draw.circle(
                        screen,
                        connect_4.rgbcolors.yellow,
                        (
                            int(c * self.SQUARESIZE + self.SQUARESIZE / 2),
                            screen.get_height()
                            - int(r * self.SQUARESIZE + self.SQUARESIZE / 2),
                        ),
                        RADIUS,
                    )
        pygame.display.update()
