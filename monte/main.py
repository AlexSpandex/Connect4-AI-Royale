from tree_creation_try_1 import MonteCarloTreeNode
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

'''node.selection()
for obj in node.children:
    for row in obj.state:
        print(row)
    print('children \n')'''

print(node.is_fully_expanded())
print(node.simulate_fake_game_randomly_till_terminal())
'''print(MonteCarloTreeNode.find_node_if_in_tree(node.state))
root_node = MonteCarloTreeNode.all_nodes[tuple(map(tuple, node.state))]
print(root_node.current_player)

for _ in range(1000):
    selected_node = root_node.selection()
    if not selected_node.is_terminal_and_win():
        if not selected_node.is_fully_expanded():
            child_node = selected_node.expand_current_node()
        result = child_node.random_choices_when_utc_unknown_called_rollout_simulation()
        child_node.backpropogate_assign_wins_and_losses_after_simulation(result)
# After the search is complete, choose the best move based on the statistics
best_child = max(root_node.children, key=lambda x: x.visits)
best_move = best_child.state

print(best_child.visits, best_child.wins, best_child.losses)
for row in best_child.state:
    print(row, 'best child')

i=0
for child in root_node.children:
    i=i+1
    print(i, child.visits, child.visits, child.wins, child.losses)'''
'''# Create an instance of MonteCarloTreeNode
root_node = MonteCarloTreeNode(initial_state_of_other_as_player_1, current_player=1)

# Run MCTS for 1000 iterations
best_move = MonteCarloTreeNode.monte_carlo_tree_search(initial_state_of_other_as_player_1, iterations=1000, current_player=1)

# Print or visualize the best move
print("Best Move:", best_move)

'''