from connect_4.board import Board

COL = 6
ROW = 7

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
    # scoring: always prioritize winning move
    if window.count(piece) == 4:
        return 100
    
    elif window.count(piece) == 3 and window.count(0) == 1:
        return 5
    
    elif window.count(piece) == 2 and window.count(0) == 2:
        return 2
    
    elif window.count(opponent_piece) == 3 and window.count(0) == 1:
        return -4
    
    else:
        return 0

def score_directions(board, piece, directions):
    total_score = 0
    for start in directions:
        dir = [board[start[0] + i * start[2]][start[1] + i * start[3]] for i in range(4)]
    total_score += evaluate(dir, piece)
    return total_score

class AlphaBetaAlgo:
    def alpha_beta(self, board, depth, alpha, beta, maxPlayer):
        valid_loc = get_valid_locations(board)
        is_terminal_node = is_terminal(board)

        if depth == 0 or is_terminal_node:
            if is_terminal_node:
                if game_board.winning_move(board, AI):
                    return (None, 999999)
                elif game_board.winning_move(board, PLAYER):
                    return (None, -999999)
                else:
                    return (None, 0)
        else:
            return (None, score_directions(board, AI))

        best_score = float('-inf') if maxPlayer else float('inf')
        best_move = None

        for col in valid_loc:
            row = game_board.open_row(board, col)
            board_copy = board.copy()
            game_board.drop_piece(board_copy, row, col, AI if maxPlayer else PLAYER)

            new_score = self.minmax(board_copy, depth - 1, alpha, beta, not maxPlayer)[1]

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