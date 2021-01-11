# Binary Tree Traversal
# Piero Orderique
# 11 Jan 2021

# Binary Tree Structure
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) -> str:
        rep = 'Data: ' + str(self.data)
        return rep

def visit(node:Node):
    print(node)

# In-Order Traversal: left branch -> current node -> right branch
def in_order_traversal(node:Node):
    if node != None:
        in_order_traversal(node.left)
        visit(node)
        in_order_traversal(node.right)

# Pre-Order Traversal: current node -> left branch -> right branch
def pre_order_traversal(node:Node):
    if node:
        visit(node)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

# Post-Order Traversal: left branch -> right branch -> current node 
def post_order_traversal(node:Node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        visit(node)

# Driver Code
if __name__ == "__main__":
    root = Node("Fabrizzio")
    root.left = Node("Piero")
    root.right = Node("Orderique")
    post_order_traversal(root)