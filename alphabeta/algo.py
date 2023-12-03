import numpy as np
from connect_4.board import Board
from random import shuffle

ROW = 6
COL = 7

PLAYER = 1
AI = 2
game_board = Board()

# def is_terminal(self):
#         """checks if either the player or AI or game is not done"""
#         return all([
#             not self.winning_move(1).any(),
#             not self.winning_move(2).any(),
#             len(self.get_valid_locations()) == 0
#         ])
        
def state_utility(self):
    if any(self.winning_move(PLAYER)) or self.winning_move(PLAYER) is None:
        return -1
    if any(self.winning_move(AI)) or self.winning_move(AI) is None:
        return 1
    return 0

def get_valid_locations(self):
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
    center_column = board[:, board.shape[1] // 2]
    score += np.count_nonzero(center_column == piece) * 3

    # Score Horizontal
    score += np.sum([evaluate(board[r, c:c+4], piece) for r in range(board.shape[0]) for c in range(board.shape[1] - 3)])

    # Score Vertical
    score += np.sum([evaluate(board[r:r+4, c], piece) for r in range(board.shape[0] - 3) for c in range(board.shape[1])])

    # Score positive sloped diagonal
    score += np.sum([evaluate(np.diag(board[r:r+4, c:c+4]), piece) for r in range(board.shape[0] - 3) for c in range(board.shape[1] - 3)])

    # Score negative sloped diagonal
    score += np.sum([evaluate(np.diag(np.fliplr(board[r:r+4, c:c+4])), piece) for r in range(board.shape[0] - 3) for c in range(board.shape[1] - 3)])

    return score

def get_successors(self, current_player):
    successors = []

    # Iterate over all columns to find valid moves
    for col in range(self.COLUMN_COUNT):
        if self.valid_location(col):
            # Create a copy of the current board to simulate the move
            successor_board = game_board.board
            successor_board.board = self.board.copy()

            # Find the open row in the selected column
            row = successor_board.open_row(col)

            # Make the move for the current player
            successor_board.drop_piece(row, col, current_player)

            successors.append(successor_board)

    return successors

class AlphaBetaAlgo:
    game_board = Board()
    def minimax_alpha_beta(self, board, depth, alpha=float('-inf'), beta=float('inf'), maximizing_player=True):
        if depth == 0 or board.is_terminal():
            return self.state_utility(board)

        if maximizing_player:
            v = float('-inf')
            for successor in board.get_successors(2):  # Assuming 2 represents the AI
                v = max(v, self.minimax_alpha_beta(successor, depth - 1, alpha, beta, False))
                alpha = max(alpha, v)
                if alpha >= beta:
                    break
            return v
        else:
            v = float('inf')
            for successor in board.get_successors(1):  
                v = min(v, self.minimax_alpha_beta(successor, depth - 1, alpha, beta, True))
                beta = min(beta, v)
                if alpha >= beta:
                    break
            return v

    def get_best_move(self, board, depth):
        best_move = None
        best_score = float('-inf')

        for col in range(board.COLUMN_COUNT):
            if board.valid_location(col):
                row = board.open_row(col)
                board.drop_piece(row, col, 2)  # Assuming 2 represents the AI
                score = self.minimax_alpha_beta(board, depth - 1, float('-inf'), float('inf'), False)
                board.board[row][col] = 0  # Undo the move

                if score > best_score:
                    best_score = score
                    best_move = col

        return best_move
