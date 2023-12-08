"""The board for connect 4"""

import pygame
import numpy as np
import connect_4.rgbcolors


class Board:
    """Sets up the board for the game"""

    def __init__(self):
        """initialize the board with default values"""
        self.row_count = 6
        self.column_count = 7
        self.board = self.create_board()

        self.square_size = 100
        self.width = self.column_count * self.square_size
        self.height = (self.row_count + 1) * self.square_size

    def create_board(self):
        """Creating the board layout"""
        return np.zeros((self.row_count, self.column_count))

    def drop_piece(self, row, col, piece):
        """Handles when a piece is dropped"""
        self.board[row][col] = piece

    def valid_location(self, col):
        """Checks for a valid location if a piece is dropped"""
        return (
            isinstance(col, int)
            and 0 <= col < self.column_count
            and self.board[self.row_count - 1, col] == 0
        )

    def open_row(self, col):
        """Checks for the next open row"""
        for row in range(self.row_count):
            ex = (self.board[row][col] == 0).all()
            if ex:
                return row
        return None

    def print_board(self):
        """Prints the board on the terminal"""
        print(np.flip(self.board, 0))
        print("")

    def winning_move(self, piece):
        """Checks for the winning piece"""
        # checks for horizontal
        for column in range(self.column_count - 3):
            for row in range(self.row_count):
                if (
                    self.board[row][column] == piece
                    and self.board[row][column + 1] == piece
                    and self.board[row][column + 2] == piece
                    and self.board[row][column + 3] == piece
                ):
                    return True

        # checks for vertical
        for column in range(self.column_count):
            for row in range(self.row_count - 3):
                if (
                    self.board[row][column] == piece
                    and self.board[row + 1][column] == piece
                    and self.board[row + 2][column] == piece
                    and self.board[row + 3][column] == piece
                ):
                    return True

        # checks for right diagnol
        for column in range(self.column_count - 3):
            for row in range(self.row_count - 3):
                if (
                    self.board[row][column] == piece
                    and self.board[row + 1][column + 1] == piece
                    and self.board[row + 2][column + 2] == piece
                    and self.board[row + 3][column + 3] == piece
                ):
                    return True

        # checks for left diagnol
        for column in range(self.column_count - 3):
            for row in range(3, self.row_count):
                if (
                    self.board[row][column] == piece
                    and self.board[row - 1][column + 1] == piece
                    and self.board[row - 2][column + 2] == piece
                    and self.board[row - 3][column + 3] == piece
                ):
                    return True

        # No winning condition found
        return None

    def check_draw(self):
        """checking if the game is a draw"""
        return np.all(self.board != 0) and not self.winning_move(1) and not self.winning_move(2)

    def draw_board(self, screen, radius):
        """Draws the board on screen"""
        # board drawing
        for column in range(self.column_count):
            for row in range(self.row_count):
                pygame.draw.rect(
                    screen,
                    connect_4.rgbcolors.blue,
                    (
                        column * self.square_size,
                        row * self.square_size + self.square_size,
                        self.square_size,
                        self.square_size,
                    ),
                )
                pygame.draw.circle(
                    screen,
                    connect_4.rgbcolors.light_blue,
                    (
                        int(column * self.square_size + self.square_size / 2),
                        int(
                            row * self.square_size
                            + self.square_size
                            + self.square_size / 2
                        ),
                    ),
                    radius,
                )

        # player pieces
        for column in range(self.column_count):
            for row in range(self.row_count):
                if self.board[row][column] == 1:
                    pygame.draw.circle(
                        screen,
                        connect_4.rgbcolors.red,
                        (
                            int(column * self.square_size + self.square_size / 2),
                            screen.get_height()
                            - int(row * self.square_size + self.square_size / 2),
                        ),
                        radius,
                    )
                elif self.board[row][column] == 2:
                    pygame.draw.circle(
                        screen,
                        connect_4.rgbcolors.yellow,
                        (
                            int(column * self.square_size + self.square_size / 2),
                            screen.get_height()
                            - int(row * self.square_size + self.square_size / 2),
                        ),
                        radius,
                    )
                elif self.board[row][column] == 3:
                    pygame.draw.circle(
                        screen,
                        connect_4.rgbcolors.orange,
                        (
                            int(column * self.square_size + self.square_size / 2),
                            screen.get_height()
                            - int(row * self.square_size + self.square_size / 2),
                        ),
                        radius,
                    )
        # check for draw
        if self.check_draw():
            font = pygame.font.Font(None, 36)
            text = font.render("Draw!", True, connect_4.rgbcolors.white)
            screen.blit(text, (self.width // 2 - 50, 10))

        pygame.display.update()
