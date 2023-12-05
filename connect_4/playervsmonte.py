# Player 1 = red
# Player 2 = yellow

"""Players vs Monte file"""

import math
import sys
import pygame
from connect_4.board import Board
from connect_4.sounds import Sounds
from monte.tree_creation_try_1 import MonteCarloTreeNode
import connect_4.rgbcolors


class PlayerAIGame:
    """Sets up the player for the game"""

    def __init__(self, screen):
        """
        initialize the PlayerAIGame instance.

        Parameters:
        - screen (pygame.Surface): the pygame screen for rendering.
        """
        pygame.init()

        # initialize the game components
        self.board = Board()

        # game state variables
        self.game_over = False
        self.turn = 0

        # player 1 (Human)
        self.player = 0
        self.player_piece = 1

        # player 2 (AI)
        self.ai_player = 1
        self.ai_piece = 2

        # board dimensions
        self.width = self.board.column_count * self.board.square_size
        self.height = (self.board.row_count + 1) * self.board.square_size

        # radius for drawing game pieces
        self.radius = int(self.board.square_size / 2 - 5)

        # pygame screen and font
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def draw_board(self):
        """calls the drawboard function from Board Class"""
        self.board.draw_board(self.screen, self.radius)

    def draw_winner(self, winner):
        """display the winning message with color coding"""
        if winner == f"Player {self.player_piece}":
            text_color = connect_4.rgbcolors.red
        elif winner == f"Player {self.ai_piece}":
            text_color = connect_4.rgbcolors.yellow
        else:
            text_color = connect_4.rgbcolors.black  # Default color

        # display winning message on the screen
        text = self.font.render(f"{winner} wins!", True, text_color)
        text_rect = text.get_rect(center=(self.width // 2, self.board.square_size // 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        # Wait for 3 seconds
        pygame.time.wait(3000)

    def reset_game(self):
        """
        resets the game by initializing a new Board and AlphaBeta instance.
        """
        self.board = Board()
        self.game_over = False
        self.turn = 0

    def switch_turn(self):
        """switches the turn between players."""
        self.turn += 1
        self.turn %= 2

    def handle_mouse_motion(self, event):
        """
        handles mouse events (e.g., motion, button click).
        """

        # highlight the column where the player can drop a piece
        pygame.draw.rect(
            self.screen,
            connect_4.rgbcolors.light_blue,
            (0, 0, self.width, self.board.square_size),
        )
        posx = event.pos[0]

        # draw the player's piece on the highlighted column
        if self.turn == self.player:
            pygame.draw.circle(
                self.screen,
                connect_4.rgbcolors.red,
                (posx, int(self.board.square_size / 2)),
                self.radius,
            )
        pygame.display.update()

    def handle_mouse_button_down(self, event):
        """handles mouse motion event"""
        if self.turn == self.player:
            posx = event.pos[0]
            col = int(math.floor(posx / self.board.square_size))

            if self.board.valid_location(col):
                row = self.board.open_row(col)
                self.board.drop_piece(row, col, self.player_piece)

                if self.board.winning_move(self.player_piece):
                    self.game_over = True

                self.switch_turn()
                self.draw_board()

    def handle_mouse_event(self, event):
        """handles mouse events (e.g., motion, button click)."""
        if event.type == pygame.MOUSEMOTION:
            self.handle_mouse_motion(event)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_button_down(event)

    def handle_monte_carlo_ai(self):
        """handles the AI player's move using the monte carlo algorithm"""
        if self.turn == self.ai_player:
            state = self.board.board.tolist()[::-1]
            action = MonteCarloTreeNode.monte_carlo_tree_search(state, 1000, 1)
            row, col = MonteCarloTreeNode.get_coordinates(state, action.state)

            if self.board.valid_location(col):
                row = self.board.open_row(col)
                self.board.drop_piece(row, col, self.ai_piece)

                if self.board.winning_move(self.ai_piece):
                    self.game_over = True

                self.draw_board()

                self.turn += 1
                self.turn %= 2

    def run(self):
        """this handles the game logic"""

        # initialize game sounds
        Sounds.stop()
        Sounds.game_music()

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.handle_mouse_event(event)
            self.handle_monte_carlo_ai()

            # Display winning message after the game is over
            if self.board.winning_move(self.player_piece):
                self.draw_winner(f"Player {self.player_piece}")
                self.reset_game()

            elif self.board.winning_move(self.ai_piece):
                self.draw_winner(f"Player {self.ai_piece}")
                self.reset_game()

            # Draw the board and update the display continuously
            self.draw_board()
            pygame.display.update()
