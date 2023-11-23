import random

class MonteCarloTreeNode:
    def __init__(self, state, current_player, parent=None, parent_action=None):
        # The state of the game represented by the node
        self.state = state

        # The player whose turn it is in this node
        self.current_player = current_player
        # The opponent player
        self.opponent = 3 - current_player  # Assuming player values are 1 and 2
        # Reference to the parent node (None for the root node)
        self.parent = parent

        # Action that led to this node from its parent (None for the root node)
        self.parent_action = parent_action

        # List to store child nodes
        self.children = []

        # List to store untried actions from this state
        self.untried_actions = self.get_legal_actions()

        # Statistics for this node
        self.visits = 0
        self.wins = 0
        self.losses = 0
        self.game_over = False

    def get_legal_actions(self):
        legal_actions = []
        for column in range(len(self.state[0])):
            if self.state[0][column] == 0:
                new_state = [row.copy() for row in self.state]
                for row in reversed(range(len(new_state))):
                    if new_state[row][column] == 0:
                        new_state[row][column] = self.current_player
                        legal_actions.append(new_state)
                        break  # Break once you've placed a piece in the column
        return legal_actions

    def is_terminal_and_win(self):
        return self.is_diagonal() or self.is_horizontal() or self.is_vertical() # or self.no_more_moves()

    def is_horizontal(self):
        for column in range(len(self.state[0]) - 3):#'''-3 because to have 4 in a row you need to hae at least 3 other next https://youtu.be/zD-Xuu_Jpe4?si=YDoBGuXPa-a7hked'''
            for row in range(len(self.state)):
                if (
                    self.state[row][column] == self.current_player and
                    self.state[row][column+1] == self.current_player and
                    self.state[row][column+2] == self.current_player and
                    self.state[row][column+3] == self.current_player
                ):
                    return True
        return False
    def is_vertical(self):
        for column in range(len(self.state[0])):
            for row in range(len(self.state)-3):
                if (
                    self.state[row][column] == self.current_player and
                    self.state[row+1][column] == self.current_player and
                    self.state[row+2][column] == self.current_player and
                    self.state[row+3][column] == self.current_player
                ):
                    return True
        return False
    def is_diagonal(self):
        for column in range(len(self.state[0])):
            for row in range(len(self.state)-3):
                if (
                    self.state[row][column] == self.current_player and
                    self.state[row+1][column+1] == self.current_player and
                    self.state[row+2][column+2] == self.current_player and
                    self.state[row+3][column+3] == self.current_player
                ):
                    return True
        return False
    

    def random_choices_when_utc_unknown_called_rollout_simulation(self):
        current_random_state = self.state
        current_player = self.current_player
        while not current_random_state.is_terminal_and_win() or current_random_state.get_legal_actions():#while not a win or lose and there are still more possible actions
            legal_actions = current_random_state.get_legal_actions()
            random_action = MonteCarloTreeNode(random.choice(legal_actions), 3-self.current_player, current_random_state)
            current_random_state = random_action.state

            if not legal_actions:
                return 0
            elif current_random_state.is_terminal_and_win():
                if current_player == self.current_player:
                    return 1
                else:
                    return -1