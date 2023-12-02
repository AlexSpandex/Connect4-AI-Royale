"""Players vs AlphaBeta file"""

import pygame
import sys
import math
from connect_4.board import Board
from connect_4.sounds import Sounds
from alphabeta.algo import *
import connect_4.rgbcolors

class PlayerAlphaBeta:

    def __init__(self, screen):
        pygame.init()

        self.board = Board()
        self.alpha = AlphaBetaAlgo()
        self.game_over = False
        self.turn = 0

        self.SQUARESIZE = 100
        self.width = self.board.COLUMN_COUNT * self.SQUARESIZE
        self.height = (self.board.ROW_COUNT + 1) * self.SQUARESIZE

        self.RADIUS = int(self.SQUARESIZE / 2 - 5)

        self.screen = screen
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
        # Wait for 1 second
        pygame.time.wait(1000)
    
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

                    # ai functionn alpha beta
                    # if self.turn == 1:
                    #         state = self.board.board.tolist()[::-1]
                    #         action = MonteCarloTreeNode.monte_carlo_tree_search(state, 1000, 1)
                    #         row,col = MonteCarloTreeNode.get_coordinates(state, action.state)
                    #         if self.board.valid_location(col):
                    #             row = self.board.open_row(col)
                    #             self.board.drop_piece(row, col, self.turn + 1)
                            
                                # self.turn += 1
                                # self.turn %= 2
                    if self.turn == 1 and not self.game_over:
                        col, _ = AlphaBetaAlgo().alpha_beta(5, -math.inf, math.inf, True)

                        # checking for validation space
                        if self.board.valid_location(col):
                            row = self.board.open_row(col)
                            self.board.drop_piece(row, col, self.turn + 1)

                            if self.board.winning_move(self.turn + 1):
                                label = pygame.render("Player 2 wins!!", 1, connect_4.rgbcolors.yellow)
                                self.screen.blit(label, (40, 10))
                                self.game_over = True

                            self.turn += 1
                            self.turn %= 2

                            
                # handles when the drop piece is dropped when clicked
                # player 1 and you click button 
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

                    pygame.display.update()

                # Draw the board and update the display continuously
                self.draw_board()