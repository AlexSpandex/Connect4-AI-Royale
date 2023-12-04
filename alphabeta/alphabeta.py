"""Players vs alpha beta file"""
# Player 1 = red
# Player 2 = yellow

import numpy as np
from connect_4.board import Board


class AlphaBeta:
    """Sets up the player for the game"""

    def __init__(self, board, max_depth=4):
        self.board = board
        self.max_depth = max_depth

    def is_terminal_node(self):
        return (
            self.board.winning_move(1)
            or self.board.winning_move(2)
            or len(self.get_valid_locations()) == 0
        )

    def get_valid_locations(self):
        valid_locations = []
        for col in range(self.board.COLUMN_COUNT):
            if self.board.valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def evaluate_window(self, window, piece):
        score = 0
        opponent_piece = 1 if piece == 2 else 2

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 2

        if window.count(opponent_piece) == 3 and window.count(0) == 1:
            score -= 4

        return score

    def evaluate_position(self):
        score = 0

        # Evaluate center column
        center_array = [
            int(i) for i in list(self.board.board[:, self.board.COLUMN_COUNT // 2])
        ]
        center_count = center_array.count(1)
        score += center_count * 3

        # Evaluate horizontal
        for r in range(self.board.ROW_COUNT):
            row_array = [int(i) for i in list(self.board.board[r, :])]
            for c in range(self.board.COLUMN_COUNT - 3):
                window = row_array[c : c + 4]
                score += self.evaluate_window(window, 1)

        # Evaluate vertical
        for c in range(self.board.COLUMN_COUNT):
            col_array = [int(i) for i in list(self.board.board[:, c])]
            for r in range(self.board.ROW_COUNT - 3):
                window = col_array[r : r + 4]
                score += self.evaluate_window(window, 1)

        # Evaluate positive slope diagonal
        for r in range(self.board.ROW_COUNT - 3):
            for c in range(self.board.COLUMN_COUNT - 3):
                window = [self.board.board[r + i][c + i] for i in range(4)]
                score += self.evaluate_window(window, 1)

        # Evaluate negative slope diagonal
        for r in range(self.board.ROW_COUNT - 3):
            for c in range(self.board.COLUMN_COUNT - 3):
                window = [self.board.board[r + 3 - i][c + i] for i in range(4)]
                score += self.evaluate_window(window, 1)

        return score

    def minimax(self, depth, alpha, beta, maximizing_player):
        valid_locations = self.get_valid_locations()
        is_terminal = self.is_terminal_node()

        if depth == 0 or is_terminal:
            if is_terminal:
                if self.board.winning_move(2):
                    return (None, 100000000000000)
                elif self.board.winning_move(1):
                    return (None, -100000000000000)
                else:
                    return (None, 0)
            else:
                return (None, self.evaluate_position())

        if maximizing_player:
            value = float("-inf")
            column = np.random.choice(valid_locations)
            for col in valid_locations:
                row = self.board.open_row(col)
                temp_board = self.board.board.copy()
                self.board.drop_piece(row, col, 2)
                new_score = self.minimax(depth - 1, alpha, beta, False)[1]
                self.board.board = temp_board
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value
        else:
            value = float("inf")
            column = np.random.choice(valid_locations)
            for col in valid_locations:
                row = self.board.open_row(col)
                temp_board = self.board.board.copy()
                self.board.drop_piece(row, col, 1)
                new_score = self.minimax(depth - 1, alpha, beta, True)[1]
                self.board.board = temp_board
                if new_score < value:
                    value = new_score
                    column = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return column, value

    def get_best_move(self):
        return self.minimax(self.max_depth, float("-inf"), float("inf"), True)[0]
