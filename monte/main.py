from tree_creation_try_1 import MonteCarloTreeNode
'''import random

node = MonteCarloTreeNode([[0] * 7 for _ in range(6)], 1)
for row in node.state:
    print(row, node.current_player)
print(node.is_vertical())
for lis in node.get_legal_actions():
    for row in lis:
        print(row)
    print('\n')
node2 = MonteCarloTreeNode(node.get_legal_actions()[0], node.opponent, node)
for lis in node2.get_legal_actions():
    for row in lis:
        print(row)
    print('\n')
random = random.choice(node2.get_legal_actions())
for row in random:
    print(row)'''
# Assume your game state is represented as a 2D list, for example, a Connect Four board.
node = MonteCarloTreeNode([[0] * 7 for _ in range(6)], 1)
actions = node.get_legal_actions()

for lis in node.untried_actions:
    for row in lis:
        print(row)
    print('untried \n')

for obj in node.children:
    for row in obj.state:
        print(row)
    print('children \n')

node.selection()
for obj in node.children:
    for row in obj.state:
        print(row)
    print('children \n')

print(node.is_fully_expanded())
print(node.random_choices_when_utc_unknown_called_rollout_simulation())

'''# Create an instance of MonteCarloTreeNode
root_node = MonteCarloTreeNode(initial_state_of_other_as_player_1, current_player=1)

# Run MCTS for 1000 iterations
best_move = MonteCarloTreeNode.monte_carlo_tree_search(initial_state_of_other_as_player_1, iterations=1000, current_player=1)

# Print or visualize the best move
print("Best Move:", best_move)

'''