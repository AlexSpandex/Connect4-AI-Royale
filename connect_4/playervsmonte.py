"""Players vs Monte file"""
# Player 1 = red
# Player 2 = yellow

import pygame
import sys
import math
from connect_4.board import Board
from connect_4.sounds import Sounds
from monte.tree_creation_try_1 import MonteCarloTreeNode
import connect_4.rgbcolors


class PlayerAIGame:
    """Sets up the player for the game"""

    def __init__(self, screen):
        pygame.init()

        self.board = Board()
        
        self.game_over = False
        self.turn = 0
        
        self.player = 0
        self.player_piece = 1
        
        self.ai_player = 1
        self.ai_piece = 2

        self.SQUARESIZE = 100
        self.width = self.board.column_count * self.SQUARESIZE
        self.height = (self.board.row_count + 1) * self.SQUARESIZE

        self.RADIUS = int(self.SQUARESIZE / 2 - 5)

        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def draw_board(self):
        """Calls the drawboard function from Board Class"""
        self.board.draw_board(self.screen, self.RADIUS)

    def draw_winner(self, winner):
        """Display the winning message with color coding"""
        if winner == f"Player {self.player_piece}":
            text_color = connect_4.rgbcolors.red
        elif winner == f"Player {self.ai_piece}":
            text_color = connect_4.rgbcolors.yellow
        else:
            text_color = connect_4.rgbcolors.black  # Default color

        text = self.font.render(f"{winner} wins!", True, text_color)
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
        Sounds.stop()
        Sounds.game_music()

        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # this moves the pieces when mouse moves
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(
                        self.screen,
                        connect_4.rgbcolors.light_blue,
                        (0, 0, self.width, self.SQUARESIZE),
                    )
                    posx = event.pos[0]
                    
                    # player 1
                    if self.turn == self.player:
                        pygame.draw.circle(
                            self.screen,
                            connect_4.rgbcolors.red,
                            (posx, int(self.SQUARESIZE / 2)),
                            self.RADIUS,
                        )
                    pygame.display.update()
                
                            
                # handles when the drop piece is dropped when clicked
                # player 1 and you click button 
                if event.type == pygame.MOUSEBUTTONDOWN: 
                    posx = event.pos[0]
                    col = int(math.floor(posx / self.SQUARESIZE))

                    if self.board.valid_location(col):
                        row = self.board.open_row(col)
                        self.board.drop_piece(row, col, self.player_piece)
                        
                        if self.board.winning_move(self.player_piece):
                            self.game_over = True

                        self.turn += 1
                        self.turn %= 2
                        
                    self.draw_board()
                    
            # ai functionn monte carlos
            if self.turn == self.ai_player:
                    state = self.board.board.tolist()[::-1]
                    action = MonteCarloTreeNode.monte_carlo_tree_search(state, 1000, 1)
                    row,col = MonteCarloTreeNode.get_coordinates(state, action.state)
                    
                    if self.board.valid_location(col):
                        row = self.board.open_row(col)
                        self.board.drop_piece(row, col, self.ai_piece)
                        
                        if self.board.winning_move(self.ai_piece):
                            self.game_over = True

                        self.draw_board()

                        self.turn += 1
                        self.turn %= 2

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
