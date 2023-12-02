import numpy as np
from connect_4.board import Board

ROW = 6
COL = 7

PLAYER = 1
AI = 2
game_board = Board()

def is_terminal(board):
    """checks if either the player or AI or game is not done"""
    return game_board.winning_move(PLAYER) or game_board.winning_move(AI) or len(get_valid_locations(board)) == 0

def get_valid_locations(board):
    return [column for column in range(COL) if game_board.valid_location(column)]

def evaluate(window, piece):
    # switches as player plays
    opponent_piece = PLAYER
    
    if piece == PLAYER:
        opponent_piece = AI
    
    # Check if the window has enough elements
    if len(window) >= 4:
        # scoring: always prioritize winning move
        if np.count_nonzero(window == piece) == 4:
            return 100
        
        elif np.count_nonzero(window == piece) == 3 and np.count_nonzero(window == 0) == 1:
            return 5
        
        elif np.count_nonzero(window == piece) == 2 and np.count_nonzero(window == 0) == 2:
            return 2
        
        elif np.count_nonzero(window == opponent_piece) == 3 and np.count_nonzero(window == 0) == 1:
            return -4
    
    return 0


def score_pos(board, piece):
    score = 0

    # Score center column
    center_column = board[:, COL // 2]
    score += np.count_nonzero(center_column == piece) * 3

    # Score Horizontal
    for r in range(ROW):
        row_array = board[r, :]
        score += sum(evaluate(row_array[c:c+4], piece) for c in range(COL - 3))

    # Score Vertical
    for c in range(COL):
        col_array = board[:, c]
        score += sum(evaluate(col_array[r:r+4], piece) for r in range(ROW - 3))

    # Score positive sloped diagonal
    for r in range(ROW - 3):
        for c in range(COL - 3):
            window = board[r:r+4, c:c+4].diagonal()
            score += evaluate(window, piece)

    # Score negative sloped diagonal
    for r in range(ROW - 3):
        for c in range(COL - 3):
            window = np.fliplr(board[r:r+4, c:c+4]).diagonal()
            score += evaluate(window, piece)

    return score

class AlphaBetaAlgo: 
    def alpha_beta(self, depth, alpha, beta, maxPlayer):
        valid_loc = get_valid_locations(game_board.board)
        is_terminal_node = is_terminal(game_board.board)

        if depth == 0:
            return (None, score_pos(game_board.board, AI))

        if is_terminal_node:
            if game_board.winning_move(AI):
                return (None, 999999)
            elif game_board.winning_move(PLAYER):
                return (None, -999999)
            else:
                return (None, 0)

        best_score = float('-inf') if maxPlayer else float('inf')
        best_move = None

        for col in valid_loc:
            row = game_board.open_row(col)
            game_board.drop_piece(row, col, AI if maxPlayer else PLAYER)

            new_score = self.alpha_beta(depth - 1, alpha, beta, not maxPlayer)[1]

            if maxPlayer and new_score > best_score:
                best_score = new_score
                best_move = col
                alpha = max(alpha, best_score)
            elif not maxPlayer and new_score < best_score:
                best_score = new_score
                best_move = col
                beta = min(beta, best_score)
                
            if alpha >= beta:
                break  # Prune the branch

        return best_move, best_score
