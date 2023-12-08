"""Alpha-Beta Pruning"""

import numpy as np


class AlphaBeta:
    """Sets up the Alpha-Beta Pruning algo"""

    def __init__(self, board, max_depth=4):
        """
        initialize the AlphaBeta player

        Parameters:
        - board (Board): The game board
        - max_depth (int): The maximum depth for the AlphaBeta search tree
        """
        self.board = board
        self.max_depth = max_depth

    def is_terminal_node(self):
        """
        check if the current game state is a terminal node

        Returns:
        - bool: true if the game state is terminal, False otherwise.
        """
        return (
            self.board.winning_move(1)
            or self.board.winning_move(2)
            or len(self.get_valid_locations()) == 0
        )

    def get_valid_locations(self):
        """
        Get a list of valid column locations where a piece can be dropped

        Returns:
        - list: List of valid column locations
        """
        valid_locations = []
        for column in range(self.board.column_count):
            if self.board.valid_location(column):
                valid_locations.append(column)
        return valid_locations

    def evaluate_window(self, window, piece):
        """
        Evaluate a window of four consecutive positions for a given player

        Parameters:
        - window (list): List of four consecutive positions
        - piece (int): Player's piece (1 or 2)

        Returns:
        - int: Score for the given window and player's piece
        """
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
        """
        evaluate the current game board position

        Returns:
        - int: Score for the current game board position
        """
        score = 0

        # Evaluate center column
        center_array = [
            int(i) for i in list(self.board.board[:, self.board.column_count // 2])
        ]
        center_count = center_array.count(1)
        score += center_count * 3

        # Evaluate horizontal
        for row in range(self.board.row_count):
            row_array = [int(i) for i in list(self.board.board[row, :])]
            for column in range(self.board.column_count - 3):
                window = row_array[column : column + 4]
                score += self.evaluate_window(window, 1)

        # Evaluate vertical
        for column in range(self.board.column_count):
            col_array = [int(i) for i in list(self.board.board[:, column])]
            for row in range(self.board.row_count - 3):
                window = col_array[row : row + 4]
                score += self.evaluate_window(window, 1)

        # Evaluate positive slope diagonal
        for row in range(self.board.row_count - 3):
            for column in range(self.board.column_count - 3):
                window = [self.board.board[row + i][column + i] for i in range(4)]
                score += self.evaluate_window(window, 1)

        # Evaluate negative slope diagonal
        for row in range(self.board.row_count - 3):
            for column in range(self.board.column_count - 3):
                window = [self.board.board[row + 3 - i][column + i] for i in range(4)]
                score += self.evaluate_window(window, 1)

        return score

    def handle_terminal_node(self):
        """
        hanldes terminal nodes by providing scores based on game outcome

        Returns:
        - tuple: (None, score) for the terminal state
        """
        if self.is_terminal_node():
            return (
                (None, 100000000000000)
                if self.board.winning_move(2)
                else (None, -100000000000000)
                if self.board.winning_move(1)
                else (None, 0)
            )
        return (None, self.evaluate_position())

    def max_value(self, valid_locations, depth, alpha, beta):
        """
        perform the Max-Value step in the Minimax algorithm with Alpha-Beta Pruning.

        Parameters:
        - valid_locations (list): List of valid column locations.
        - depth (int): The current depth in the search tree.
        - alpha (float): The best value for the maximizing player.
        - beta (float): The best value for the minimizing player.

        Returns:
        - tuple: (Best column for the current player, corresponding value).
        """
        value = float("-inf")
        column = np.random.choice(valid_locations)
        for col in valid_locations:
            row = self.board.open_row(col)
            temp_board = self.board.board.copy()
            self.board.drop_piece(row, col, 2)
            board_score = self.minimax(depth - 1, alpha, beta, False)[1]
            self.board.board = temp_board
            if board_score > value:
                value = board_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    def min_value(self, valid_locations, depth, alpha, beta):
        """
        perform the Min-Value step in the Minimax algorithm with Alpha-Beta Pruning.

        Parameters:
        - valid_locations (list): List of valid column locations.
        - depth (int): The current depth in the search tree.
        - alpha (float): The best value for the maximizing player.
        - beta (float): The best value for the minimizing player.

        Returns:
        - tuple: (Best column for the current player, corresponding value).
        """
        value = float("inf")
        column = np.random.choice(valid_locations)
        for col in valid_locations:
            row = self.board.open_row(col)
            temp_board = self.board.board.copy()
            self.board.drop_piece(row, col, 1)
            board_score = self.minimax(depth - 1, alpha, beta, True)[1]
            self.board.board = temp_board
            if board_score < value:
                value = board_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

    def minimax(self, depth, alpha, beta, maximizing_player):
        """
        Perform the Minimax algorithm with Alpha-Beta Pruning

        Parameters:
        - depth (int): the current depth in the search tree
        - alpha (float): the best value for the maximizing player
        - beta (float): the best value for the minimizing player
        - maximizing_player (bool): true if the current player is maximizing

        Returns:
        - tuple: (Best column for the current player, corresponding value)
        """
        valid_locations = self.get_valid_locations()
        is_terminal = self.is_terminal_node()

        if depth == 0 or is_terminal:
            return self.handle_terminal_node()

        if maximizing_player:
            return self.max_value(valid_locations, depth, alpha, beta)
        else:
            return self.min_value(valid_locations, depth, alpha, beta)

    def get_best_move(self):
        """
        get the best move for the current player using the Alpha-Beta Pruning algorithm.

        Returns:
        - int: the best column to drop a piece in, determined by the minimax algorithm.
        """
        return self.minimax(self.max_depth, float("-inf"), float("inf"), True)[0]
