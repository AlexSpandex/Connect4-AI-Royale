# Player 1 Alpha = red
# Player 2 Monte = yellow

"""AlphaBeta vs Monte-Carlo file"""

import sys
import pygame
from connect_4.board import Board
from connect_4.sounds import Sounds
from alphabeta.alphabeta import AlphaBeta
from monte.tree_creation_try_1 import MonteCarloTreeNode
from connect_4.leaderboard_data import LeaderboardData
import connect_4.rgbcolors


class Ai:
    """Sets up the AI for the game"""

    def __init__(self, screen):
        """
        initialize the AI instance.

        Parameters:
        - screen (pygame.Surface): the pygame screen for rendering.
        """
        pygame.init()
        
        # initialize the game components
        self.board = Board()
        self.ai_alpha = AlphaBeta(self.board)

        # game state variables
        self.game_over = False
        self.turn = 0

        # player 1 (AI)(alpha)
        self.ai_player_1 = 0
        self.ai_player_1_piece = 3

        # player 2 (AI)(monte)
        self.ai_player_2 = 1
        self.ai_player_2_piece = 2

        # board dimensions
        self.width = self.board.column_count * self.board.square_size
        self.height = (self.board.row_count + 1) * self.board.square_size

        # radius for drawing game pieces
        self.radius = int(self.board.square_size / 2 - 5)

        # pygame screen and font
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        
        # initializing leaderboard class for win lose count
        self.leaderboard = LeaderboardData()

    def draw_board(self):
            """calls the drawboard function from Board Class"""
            self.board.draw_board(self.screen, self.radius)

    def draw_winner(self, winner):
        """display the winning message with color coding"""
        if winner == f"Player {self.ai_player_1_piece}":
            text_color = connect_4.rgbcolors.orange
        elif winner == f"Player {self.ai_player_2_piece}":
            text_color = connect_4.rgbcolors.yellow
        else:
            text_color = connect_4.rgbcolors.black  # Default color

        # display winning message on the screen
        text = self.font.render(f"{winner} wins!", True, text_color)
        text_rect = text.get_rect(center=(self.width // 2, self.board.square_size // 2))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        
        if winner == f"Player {self.ai_player_1_piece}":
                self.leaderboard.update_leaderboard("AlphaBeta", "MonteCarlo")
        elif winner == f"Player {self.ai_player_2_piece}":
            self.leaderboard.update_leaderboard("MonteCarlo", "AlphaBeta")
            
        self.leaderboard.save_leaderboard()
        # Wait for 3 seconds
        pygame.time.wait(3000)

    def reset_game(self):
        """
        resets the game by initializing a new Board and AlphaBeta instance.
        """
        self.board = Board()
        self.ai_alpha = AlphaBeta(self.board)
        self.game_over = False
        self.turn = 0
        
         # Display current wins and losses
        self.leaderboard.display_leaderboard()

        # Clear the winner message from the screen
        self.screen.fill(connect_4.rgbcolors.light_blue)
        self.draw_board()
        pygame.display.update()

    def switch_turn(self):
        """switches the turn between players."""
        self.turn += 1
        self.turn %= 2


    def handle_alpha_beta_ai(self):
        """handles the AI player's move using the Alpha-Beta Pruning algorithm"""
        if self.turn == self.ai_player_1:
            ai_move = self.ai_alpha.get_best_move()
            ai_row = self.board.open_row(ai_move)

            if self.board.valid_location(ai_move):
                self.board.drop_piece(ai_row, ai_move, self.ai_player_1_piece)

                if self.board.winning_move(self.ai_player_1_piece):
                    self.game_over = True

                self.switch_turn()
                self.draw_board()

    def handle_monte_carlo_ai(self):
        """handles the AI player's move using the monte carlo algorithm"""
        if self.turn == self.ai_player_2:
            state = self.board.board.tolist()[::-1]
            action = MonteCarloTreeNode.monte_carlo_tree_search(state, 1000, 1)

            # Check if action is not None
            if action is not None:
                row, col = MonteCarloTreeNode.get_coordinates(state, action.state)

                if self.board.valid_location(col):
                    row = self.board.open_row(col)
                    self.board.drop_piece(row, col, self.ai_player_2_piece)

                    if self.board.winning_move(self.ai_player_2_piece):
                        self.game_over = True

                    self.switch_turn()
                    self.draw_board()

    def run(self):
        """This handles the game logic"""

        # initialize game sounds
        Sounds.stop()
        Sounds.battle_music()
        # draws a border to now show background image
        pygame.draw.rect(self.screen, connect_4.rgbcolors.light_blue, (0,0, self.width, self.board.square_size))


        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE or event.type == pygame.QUIT:
                    print("ESC button pressed-Exiting...")
                    pygame.quit()
                    sys.exit()

            # AI moves and game logic
            self.handle_alpha_beta_ai()
            pygame.time.delay(500)  # Introduce a small delay between AI moves
            self.handle_monte_carlo_ai()

            # Check for a winner or draw
            if self.board.winning_move(self.ai_player_1_piece) or self.board.winning_move(self.ai_player_2_piece):
                winner = f"Player {self.ai_player_1_piece}" if self.board.winning_move(self.ai_player_1_piece) else f"Player {self.ai_player_2_piece}"
                self.draw_winner(winner)
                self.reset_game()

            # Draw the board
            self.draw_board()

            # Update the display
            pygame.display.update()