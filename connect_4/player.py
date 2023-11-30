"""Players vs Player file"""

import pygame
import sys
import math
from connect_4.board import Board


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

        self.size = (800, 600)
        self.RADIUS = int(self.SQUARESIZE / 2 - 5)

        self.screen = screen
        self.font = pygame.font.Font(None, 36)


    def draw_board(self):
        self.screen.fill((40, 40, 40))  # Fill background color

        for c in range(self.board.COLUMN_COUNT):
            for r in range(self.board.ROW_COUNT):
                pygame.draw.rect(
                    self.screen,
                    (0, 0, 255),
                    (c * self.SQUARESIZE, r * self.SQUARESIZE + self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE),
                )
                pygame.draw.circle(
                    self.screen,
                    (173, 216, 230),
                    (int(c * self.SQUARESIZE + self.SQUARESIZE / 2), int(r * self.SQUARESIZE + self.SQUARESIZE + self.SQUARESIZE / 2)),
                    self.RADIUS,
                )

        for c in range(self.board.COLUMN_COUNT):
            for r in range(self.board.ROW_COUNT):
                if self.board.board[r][c] == 1:
                    pygame.draw.circle(
                        self.screen,
                        (255, 0, 0),
                        (int(c * self.SQUARESIZE + self.SQUARESIZE / 2), self.screen.get_height() - int(r * self.SQUARESIZE + self.SQUARESIZE / 2)),
                        self.RADIUS,
                    )
                elif self.board.board[r][c] == 2:
                    pygame.draw.circle(
                        self.screen,
                        (255, 255, 0),
                        (int(c * self.SQUARESIZE + self.SQUARESIZE / 2), self.screen.get_height() - int(r * self.SQUARESIZE + self.SQUARESIZE / 2)),
                        self.RADIUS,
                    )

        pygame.display.update()

    def reset_game(self):
        self.board = Board()
        self.game_over = False
        self.turn = 0

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    # Draw the background only once
                    pygame.draw.rect(self.screen, (173, 216, 230), (0, 0, self.width, self.SQUARESIZE))

                    posx = event.pos[0]
                    if self.turn == 0:
                        pygame.draw.circle(
                            self.screen,
                            (255, 0, 0),
                            (posx, int(self.SQUARESIZE / 2)),
                            self.RADIUS,
                        )
                    else:
                        pygame.draw.circle(
                            self.screen,
                            (255, 255, 0),
                            (posx, int(self.SQUARESIZE / 2)),
                            self.RADIUS,
                        )

                    pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(
                        self.screen, (173, 216, 230), (0, 0, self.width, self.SQUARESIZE)
                    )
                    posx = event.pos[0]
                    col = int(math.floor(posx / self.SQUARESIZE))

                    if self.board.valid_location(col):
                        row = self.board.open_row(col)
                        self.board.drop_piece(row, col, self.turn + 1)

                        if self.board.winning_move(self.turn + 1):
                            self.game_over = True
                            self.last_win_time = pygame.time.get_ticks()
                            pygame.time.wait(1000)  # Wait for 1 second
                            self.reset_game()

                    self.turn += 1
                    self.turn %= 2

                # Draw the board and update the display continuously
                self.draw_board()

                # Show winning message for 1 second
                current_time = pygame.time.get_ticks()
                if self.game_over and current_time - self.last_win_time < 1000:
                    winner = "Player 1" if self.turn == 0 else "Player 2"
                    print(f"{winner} wins!")  # Modify or remove this line as needed
                    pygame.time.wait(1000)  # Wait for 1 second
                    self.reset_game()

                pygame.display.update()