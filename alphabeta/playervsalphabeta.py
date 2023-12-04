import pygame
import sys
import math 
import random
from threading import Timer

from connect_4.board import Board
from alphabeta.algo import *

PLAYER = 0
AI = 1

ROW = 6
COL = 7

# colors 
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# creating board instance
game_board = Board()

board = game_board.create_board()

def end_game():
    global game_over
    game_over = True
    print(game_over)
    
is_game_over = False

whos_turn = random.randint(PLAYER, AI)

# inititalizing init 
pygame.init()

width = COL * 100
height = (ROW + 1) * 100
draw_circle = int(100/2-5)
size = (width, height)
screen = pygame.display.set_mode(size)

# drawing
game_board.create_board(board)
pygame.display.update()

while not is_game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        

        if event.type == pygame.MOUSEMOTION and not_over:
            pygame.draw.rect(screen, BLACK, (0, 0, width, 100))
            xpos = pygame.mouse.get_pos()[0]
            if turn == PLAYER:
                pygame.draw.circle(screen, RED, (xpos, int(100/2)), draw_circle )

        # if player clicks the button, we drop their piece down
        if event.type == pygame.MOUSEBUTTONDOWN and not_over:
            pygame.draw.rect(screen, BLACK, (0,0, width, 100))

            # ask for player 1 inupt
            if turn == PLAYER:

                # we assume players will use correct input
                xpos = event.pos[0] 
                col = int(math.floor(xpos/100)) 

                if game_board.valid_location(board, col):
                    row = game_board.open_row(board, col)
                    game_board.drop_piece(board, row, col, PLAYER)
                    if game_board.winning_move(board, PLAYER):
                        print("PLAYER 1 WINS!")
                        label = pygame.render("PLAYER 1 WINS!", 1, RED)
                        screen.blit(label, (40, 10))
                        not_over = False
                        t = Timer(3.0, end_game)
                        t.start()
                
                game_board.draw_board(board) 

                # increment turn by 1
                turn += 1

                # this will alternate between 0 and 1 withe very turn
                turn = turn % 2 

        pygame.display.update()

                     
    # if its the AI's turn
    if turn == AI and not game_over and not_over:

        # the column to drop in is found using minimax
        col, minimax_score = AlphaBetaAlgo.minimax(board, 5, -math.inf, math.inf, True)

        if game_board.valid_location(board, col):
            pygame.time.wait(500)
            row = game_board.open_row(board, col)
            game_board.drop_piece(board, row, col, AI)
            if game_board.winning_move(board, AI):
                print("PLAYER 2 WINS!")
                label = pygame.render("PLAYER 2 WINS!", 1, YELLOW)
                screen.blit(label, (40, 10))
                not_over = False
                t = Timer(3.0, end_game)
                t.start()
        game_board.draw_board(board)    

        # increment turn by 1
        turn += 1
        # this will alternate between 0 and 1 withe very turn
        turn = turn % 2


