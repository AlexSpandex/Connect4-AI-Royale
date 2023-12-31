from logging import root
import random
import math


class MonteCarloTreeNode:
    # Class variable to store all nodes
    all_nodes = {}

    def __init__(self, state, current_player, parent=None):
        # The state of the game represented by the node
        self.state = state

        # The player whose turn it is in this node
        self.current_player = current_player
        # The opponent player
        self.opponent = 3 - current_player  # Assuming player values are 1 and 2
        # Reference to the parent node (None for the root node)
        self.parent = parent

        # List to store child nodes
        self.children = []

        # List to store untried actions from this state
        self.untried_actions = self.get_legal_actions()

        # Statistics for this node
        self.visits = 0
        self.wins = 0
        self.losses = 0
        self.game_over = False

        # Add the current node to the dictionary hold refrence to self 
        # so if self changes so does the value of the dictionary at state
        MonteCarloTreeNode.all_nodes[tuple(map(tuple, self.state))] = self

    def find_node_if_in_tree(initial_state):
        return MonteCarloTreeNode.all_nodes.get(tuple(map(tuple, initial_state)), None)

    def get_legal_actions(self):
        legal_actions = []
        for column in range(len(self.state[0])):
            if self.state[0][column] == 0:
                new_state = [row.copy() for row in self.state]  # Create a deep copy
                for row in reversed(range(len(new_state))):
                    if new_state[row][column] == 0:
                        new_state[row][column] = self.opponent
                        legal_actions.append(new_state)  # Append individual actions
                        break  # Break once you've placed a piece in the column
        return legal_actions

    def is_terminal_and_win(self):
        return (
            self.is_diagonal() or self.is_horizontal() or self.is_vertical()
        )  # or self.no_more_moves()

    def no_winner(self):
        lis = [
            player_in_row_0
            for player_in_row_0 in range(len(self.state[0]))
            if player_in_row_0 == 0
        ]
        return len(lis) == 0

    def is_horizontal(self):
        for column in range(
            len(self.state[0]) - 3
        ):  #'''-3 because to have 4 in a row you need to hae at least 3 other next https://youtu.be/zD-Xuu_Jpe4?si=YDoBGuXPa-a7hked'''
            for row in range(len(self.state)):
                if (
                    self.state[row][column] == self.current_player
                    and self.state[row][column + 1] == self.current_player
                    and self.state[row][column + 2] == self.current_player
                    and self.state[row][column + 3] == self.current_player
                ):
                    return True
        return False

    def is_vertical(self):
        for column in range(len(self.state[0])):
            for row in range(len(self.state) - 3):
                if (
                    self.state[row][column] == self.current_player
                    and self.state[row + 1][column] == self.current_player
                    and self.state[row + 2][column] == self.current_player
                    and self.state[row + 3][column] == self.current_player
                ):
                    return True
        return False

    def is_diagonal(self):
        for column in range(len(self.state[0]) - 3):
            for row in range(len(self.state) - 3):
                if (
                    self.state[row][column] == self.current_player
                    and self.state[row + 1][column + 1] == self.current_player
                    and self.state[row + 2][column + 2] == self.current_player
                    and self.state[row + 3][column + 3] == self.current_player
                ):
                    return True
                # checks for left diagnol
        for column in range(len(self.state[0]) - 3):
            for row in range(3, len(self.state)):
                if (
                    self.state[row][column] == self.current_player
                    and self.state[row - 1][column + 1] == self.current_player
                    and self.state[row - 2][column + 2] == self.current_player
                    and self.state[row - 3][column + 3] == self.current_player
                ):
                    return True
        return False

    def expand_current_node(self):
        action = self.untried_actions.pop(0)
        child_node = MonteCarloTreeNode(
            [row.copy() for row in action], self.opponent, self
        )
        self.children.append(child_node)
        return child_node

    def is_fully_expanded(self):
        return len(self.untried_actions) == 0

    def random_choice(self, possible_actions):
        # legal_actions = self.untried_actions
        random_state_or_action = random.choice(possible_actions)
        # Ensure that the chosen random action does not exceed the bounds of the game state
        return random_state_or_action

    def evaluate_window(self, window, player):
        """
        Evaluate a window of four consecutive positions for a given player

        Parameters:
        - window (list): List of four consecutive positions
        - piece (int): Player's piece (1 or 2)

        Returns:
        - int: Score for the given window and player's piece
        """
        # Customize this method based on your specific criteria for evaluating a window
        # For example, you can assign scores based on the number of player's pieces in the window
        player_pieces = window.count(player)
        opponent_pieces = window.count(3 - player)  # Assuming player values are 1 and 2
        if player_pieces == 4:
            return 100  # A win for the player
        elif opponent_pieces == 4:
            return -100  # A win for the opponent
        else:
            return player_pieces  # Adjust the scoring logic as needed

    def evaluate_position(self, state):
        """
        evaluate the current game board position

        Returns:
        - int: Score for the current game board position
        """
        score = 0

        # Evaluate center column
        center_array = [row[len(row) // 2] for row in self.state]
        center_count = center_array.count(1)
        score += center_count * 3

        # Evaluate horizontal
        for row in range(len(state)):
            row_array = [int(i) for i in state[row]]
            for column in range(len(state[0]) - 3):
                window = row_array[column : column + 4]
                score += self.evaluate_window(window, 1)

        # Evaluate vertical
        for column in range(len(state[0])):
            col_array = [int(state[row][column]) for row in range(len(state) - 3)]
            for row in range(len(state) - 3):
                window = col_array[row : row + 4]
                score += self.evaluate_window(window, 1)

        # Evaluate positive slope diagonal
        for row in range(len(state) - 3):
            for column in range(len(state[0]) - 3):
                window = [state[row + i][column + i] for i in range(4)]
                score += self.evaluate_window(window, 1)

        # Evaluate negative slope diagonal
        for row in range(len(state) - 3):
            for column in range(len(state[0]) - 3):
                window = [state[row + 3 - i][column + i] for i in range(4)]
                score += self.evaluate_window(window, 1)

        return score

    def simulate_fake_game_randomly_till_terminal(self):
        current_node = self
        while not current_node.is_terminal_and_win() and not current_node.no_winner():
            possible_actions = current_node.get_legal_actions()

            # Check if there are legal actions available
            if not possible_actions:
                break

            # action = current_node.random_choice(possible_actions)
            action_scores = [
                self.evaluate_position(state) for state in possible_actions
            ]

            best_action_index = action_scores.index(max(action_scores))
            action = possible_actions[best_action_index]

            if MonteCarloTreeNode.find_node_if_in_tree(action) is not None:
                current_node = MonteCarloTreeNode.all_nodes[tuple(map(tuple, action))]
            else:
                current_node = MonteCarloTreeNode(
                    action, current_node.opponent, current_node
                )

        if (
            current_node.is_terminal_and_win()
            and current_node.current_player == self.opponent
        ):
            return 1
        elif current_node.no_winner():
            return 0
        else:
            return -1

    # def best_uct_score_in_children_of_current_node(self):
    #     #UCB = wins/visits + exploration_factor * sqrt(log(total_visits)/visits)
    #     exploration_factor = math.sqrt(2)
    #     children_uct_values = [(c.wins / c.visits) + exploration_factor * math.sqrt((2 * math.log(self.visits) / c.visits)) for c in self.children]
    #     index_of_highest_ucb_of_children = children_uct_values.index(max(children_uct_values))
    #     return self.children[index_of_highest_ucb_of_children]
    def best_uct_score_in_children_of_current_node(self):
        if not self.children:
            return None  # Handle the case when there are no children

        exploration_factor = math.sqrt(2)
        children_uct_values = [
            (c.wins / c.visits)
            + exploration_factor * math.sqrt((2 * math.log(self.visits) / c.visits))
            for c in self.children
        ]

        # Check if children_uct_values is not empty before finding the maximum
        if children_uct_values:
            index_of_highest_ucb_of_children = children_uct_values.index(
                max(children_uct_values)
            )
            return self.children[index_of_highest_ucb_of_children]
        else:
            return self.children[0]  # Handle the case when there are no children

    def select_node_based_on_uct_unless_all_children_not_expanded_to_use_for_simulation(
        self,
    ):
        current_node = self
        while (
            current_node is not None
            and not current_node.is_terminal_and_win()
            and not current_node.no_winner()
        ):
            if not current_node.is_fully_expanded():
                return current_node.expand_current_node()
            else:
                # picks child with the best utc score until the node where we left off, then it starts expanding and picking randomly
                current_node = current_node.best_uct_score_in_children_of_current_node()

        # Return the current node if it is terminal
        return current_node

    def backpropogate_assign_wins_and_losses_after_simulation(self, result):
        current_node = self
        while current_node is not None:
            current_node.visits += 1

            if result == 1:
                current_node.wins += 1
            elif result == -1:
                current_node.losses += 1
            else:
                # Handle draws if applicable
                pass
            current_node = current_node.parent

    def monte_carlo_tree_search(initial_state, iterations=1000, current_player=1):
        if MonteCarloTreeNode.find_node_if_in_tree(initial_state) is not None:
            root_node = MonteCarloTreeNode.all_nodes[tuple(map(tuple, initial_state))]
        else:
            root_node = MonteCarloTreeNode(initial_state, current_player)

        if not root_node.no_winner() and not root_node.is_terminal_and_win():
            for i in range(iterations):
                choosen_action = (
                    root_node.select_node_based_on_uct_unless_all_children_not_expanded_to_use_for_simulation()
                )

                if choosen_action is None:
                    break

                reward_or_penalty = (
                    choosen_action.simulate_fake_game_randomly_till_terminal()
                )
                choosen_action.backpropogate_assign_wins_and_losses_after_simulation(
                    reward_or_penalty
                )

            if root_node.children:
                # avg_score = [c.wins / c.visits for c in root_node.children]
                avg_score = [
                    c.wins / (c.visits + (c.losses * 20)) for c in root_node.children
                ]
                best_avg_score_index = avg_score.index(max(avg_score))
                return root_node.children[best_avg_score_index]
        return None

    def get_coordinates(root_state, best_child_state):
        for column in range(len(root_state[0])):
            for row in range(len(root_state)):
                if root_state[row][column] != best_child_state[row][column]:
                    return row, column
