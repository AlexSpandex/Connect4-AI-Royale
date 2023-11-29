import random
import math

class MonteCarloTreeNode:
    '''# Class variable to store all nodes
    all_nodes = {}'''
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
        
        # Add the current node to the dictionary hold refrence to self so if self changes so does the value of the dictionary at state
        MonteCarloTreeNode.all_nodes[tuple(map(tuple, self.state))] = self

    '''def find_node_if_in_tree(initial_state):
        return MonteCarloTreeNode.all_nodes.get(tuple(map(tuple, initial_state)), None)'''

    def get_legal_actions(self):
        legal_actions = []
        for column in range(len(self.state[0])):
            if self.state[0][column] == 0:
                new_state = [row.copy() for row in self.state]
                for row in reversed(range(len(new_state))):
                    if new_state[row][column] == 0:
                        new_state[row][column] = self.opponent #could be self.current_player state I'm unsure
                        legal_actions.append(new_state)
                        break  # Break once you've placed a piece in the column
        return legal_actions

    def is_terminal_and_win(self):
        return self.is_diagonal() or self.is_horizontal() or self.is_vertical() # or self.no_more_moves()
    
    def no_winner(self):
        lis = [player_in_row_0 for player_in_row_0 in range(len(self.state[0])) if player_in_row_0==0]
        return len(lis)==0

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
        for column in range(len(self.state[0])-3):
            for row in range(len(self.state)-3):
                if (
                    self.state[row][column] == self.current_player and
                    self.state[row+1][column+1] == self.current_player and
                    self.state[row+2][column+2] == self.current_player and
                    self.state[row+3][column+3] == self.current_player
                ):
                    return True
        return False

    def expand_current_node(self):
        action = self.untried_actions.pop(0)
        child_node = MonteCarloTreeNode(action,self.opponent, self)
        self.children.append(child_node)
        return child_node
    
    def is_fully_expanded(self):
        return len(self.untried_actions)==0

    def random_choice(self):
        random_state_or_action = random.choice(self.legal_actions)
        # Ensure that the chosen random action does not exceed the bounds of the game state
        return random_state_or_action
    
    def backpropogate_assign_wins_and_losses_after_simulation(self, result):
        current_node = self
        while current_node is not None:
            current_node.visits += 1
            if result == 1:
                current_node.wins += 1
            elif result == -1:
                current_node.losses += 1
            else:
                pass
            current_node = current_node.parent

    