from tree_creation_try_1 import MonteCarloTreeNode
import random

node = MonteCarloTreeNode([[0] * 7 for _ in range(6)], 1)
'''for row in node.state:
    print(row, node.current_player)
print(node.is_vertical())
for lis in node.get_legal_actions():
    for row in lis:
        print(row)
    print('\n')'''
node2 = MonteCarloTreeNode(node.get_legal_actions()[0], node.opponent, node)
for lis in node2.get_legal_actions():
    for row in lis:
        print(row)
    print('\n')
random = random.choice(node2.get_legal_actions())
for row in random:
    print(row)