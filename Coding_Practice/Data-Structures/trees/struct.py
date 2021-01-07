# Tree Structure
# @author Piero Orderique
# @date 06 Jan 2021

# NOTE
# Binary Tree - all nodes have at most 2 children
# Leaf node - node has no children
# Binary Search Tree - a binary tree in which every node fits a specific ordering property:
    # all left descendants <= n < all right descendants, for each node n
    # BE SURE TO NOT JUST ASSUME BINARY TREE IS A BST!

class Node:
    # String name
    # Nodes list children
    def __init__(self, name=None, children=[]) -> None:
        self.name = name
        self.children = children