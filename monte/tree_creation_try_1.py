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
        
        # Add the current node to the dictionary hold refrence to self so if self changes so does the value of the dictionary at state
        MonteCarloTreeNode.all_nodes[tuple(map(tuple, self.state))] = self

    def find_node_if_in_tree(initial_state):
        return MonteCarloTreeNode.all_nodes.get(tuple(map(tuple, initial_state)), None)

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
    
    def selection(self):
        selected_child = None
        if not self.is_fully_expanded():
            selected_child = self.expand_current_node()
            return selected_child
        else:
            #UCB = wins/visits + exploration_factor * sqrt(log(total_visits)/visits)
            exploration_factor = math.sqrt(2)
            choosen_ucb_is_max_ucb = float('-inf')
            for child in self.children:
                exploitation_factor=(child.wins/(child.visits+1))
                ucb=exploitation_factor+exploitation_factor*math.sqrt(math.log(self.visits)/(child.visits+1))
                if ucb > choosen_ucb_is_max_ucb:
                    choosen_ucb_is_max_ucb = ucb
                    selected_child = child
            return selected_child

    def expand_current_node(self):
        action = self.untried_actions.pop(0)
        child_node = MonteCarloTreeNode(action,self.opponent, self)
        self.children.append(child_node)
        return child_node
    
    def is_fully_expanded(self):
        return len(self.untried_actions)==0

    def random_choices_when_utc_unknown_called_rollout_simulation(self):
        current_random_state = self
        current_player = self.current_player
        while not current_random_state.is_terminal_and_win():
            legal_actions = current_random_state.get_legal_actions()
            if not legal_actions:
                # Handle the termination condition appropriately, for example, return 0
                return 0
            random_action = random.choice(legal_actions)
            # Ensure that the chosen random action does not exceed the bounds of the game state
            current_random_state = MonteCarloTreeNode(random_action, current_random_state.opponent, current_random_state)
            '''for lis in current_random_state.state:
                print(lis)
            print(current_random_state.current_player,self.current_player,'\n') 
        for lis in current_random_state.parent.state:
            print('parent',lis) '''                 
        # Check the result after the simulation
        if current_random_state.current_player == self.current_player:
            return 1
        else:
            return -1

    
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

    def monte_carlo_tree_search(initial_state, iterations=1000, current_player=1):
        # Check if the tree already has a node with the initial state
        root_node = MonteCarloTreeNode.find_node_if_in_tree(initial_state)
        # If not, create a new root node with the initial state
        if root_node is None:
            root_node = MonteCarloTreeNode(initial_state, current_player=current_player)
        else:
            root_node = MonteCarloTreeNode.all_nodes[tuple(map(tuple, initial_state))]
        for _ in range(iterations):
            selected_node = root_node.selection()
            if not selected_node.is_terminal_and_win():
                child_node = selected_node.expand_current_node()
                result = child_node.random_choices_when_utc_unknown_called_rollout_simulation()
                child_node.backpropogate_assign_wins_and_losses_after_simulation(result)
        # After the search is complete, choose the best move based on the statistics
        best_child = max(root_node.children, key=lambda x: x.visits)
        best_move = best_child.state
        return best_move