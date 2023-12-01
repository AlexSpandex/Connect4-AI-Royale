"""Players vs Player file"""

import pygame
import sys
import math
from connect_4.board import Board
import connect_4.rgbcolors


class PlayerGame:
    """Sets up the player for the game"""

    def __init__(self, screen):
        pygame.init()

        self.board = Board()
        self.game_over = False
        self.turn = 0

        self.SQUARESIZE = 100
        self.width = self.board.COLUMN_COUNT * self.SQUARESIZE
        self.height = (self.board.ROW_COUNT + 1) * self.SQUARESIZE

        self.RADIUS = int(self.SQUARESIZE / 2 - 5)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(None, 36)

    def draw_board(self):
        """Calls the drawboard function from Board Class"""
        self.board.draw_board(self.screen, self.RADIUS)

    def draw_winner(self, winner):
        """Display the winning message"""
        text = self.font.render(f"{winner} wins!", True, connect_4.rgbcolors.black)
        text_rect = text.get_rect(center=(self.width // 2, self.SQUARESIZE // 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        # Wait for 3 seconds
        pygame.time.wait(3000)

    def reset_game(self):
        """When the game is over restart"""
        self.board = Board()
        self.game_over = False
        self.turn = 0

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # this moves the pieces when the mouse moves
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(
                        self.screen,
                        connect_4.rgbcolors.light_blue,
                        (0, 0, self.width, self.SQUARESIZE),
                    )
                    posx = event.pos[0]

                    if self.turn == 0:
                        pygame.draw.circle(
                            self.screen,
                            connect_4.rgbcolors.red,
                            (posx, int(self.SQUARESIZE / 2)),
                            self.RADIUS,
                        )
                    else:
                        pygame.draw.circle(
                            self.screen,
                            connect_4.rgbcolors.yellow,
                            (posx, int(self.SQUARESIZE / 2)),
                            self.RADIUS,
                        )

                pygame.display.update()

                # handles when the drop piece is dropped
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    col = int(math.floor(posx / self.SQUARESIZE))

                    if self.board.valid_location(col):
                        row = self.board.open_row(col)
                        self.board.drop_piece(row, col, self.turn + 1)

                        if self.board.winning_move(self.turn + 1):
                            self.game_over = True
                            self.draw_winner(f"Player {self.turn + 1}")
                            self.reset_game()

                        self.turn += 1
                        self.turn %= 2

                    # prints the board game onto the terminal
                    self.board.print_board()

            # Draw the board and update the display continuously
            self.draw_board()
            pygame.display.update()
