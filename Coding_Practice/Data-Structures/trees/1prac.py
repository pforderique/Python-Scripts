# CTCI Practice Questions Ch 4
# Piero Orderique
# Started 12 Jan 2021

# Structures 
class Node:
    def __init__(self, data, adjacent=[]) -> None:
        self.data = data
        self.adjacent = adjacent
        self.visited = False

    def __str__(self) -> str:
        return str(self.data)

class TreeNode():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.visited = False

    def print_tree(self):
        '''uses DFS to print'''
        if self == None: return
        self.visited = True
        print(self)
        # now do it for the children
        if self.left and not self.left.visited:
            self.left.visited = True
            self.left.print_tree()
        if self.right and not self.right.visited:
            self.right.visited = True
            self.right.print_tree()

    def __str__(self) -> str:
        return str(self.data)

# 4.1 Route Between Nodes : Design Algo that returns True iff there exists a path from S->E - CORRECT!
# I wil be using BFS for path finding
from collections import deque
def existsPath(S:Node, E:Node) -> bool:
    # init queue and append this root node
    queue = deque([])
    S.visited = True
    queue.append(S)
    # while there are still nodes to process, visit them and add their neighbors
    while len(queue) != 0:
        r = queue.popleft()
        # return True if node is E since that means there's a path!
        if r == E: return True
        # otherwise keep adding neighbors to queue
        for node in r.adjacent:
            if node.visited == False:
                node.visited = True
                queue.append(node)
    # if we are done BFSsing without encountering E, then there is no path S->E
    return False

# 4.2 Minimal Tree : given sorted increasing arr, create a Binary Search Tree with min height - CORRECT!
def treeify(arr:list) -> TreeNode:
    # Bases Cases
    if len(arr) == 0: return None
    if len(arr) == 1: return TreeNode(arr[0])
    # else get root create its subtrees
    mid = len(arr)//2 
    root = TreeNode(arr[mid])
    root.left = treeify(arr[:mid])
    root.right = treeify(arr[mid+1:])
    # now return the root node
    return root

# ____________________________________________________________________
# Test Data:

# Graph
    # S -> x -> y -> E
    # |-> andre
# E = Node("E")
# S = Node("S", [Node("x", [Node("y", [E])]), Node("andre")])

# BST:
    #      4
    #     / \
    #    2   9
    #   /   / \
    #  1   4   11
n1 = TreeNode(1)
n2 = TreeNode(4)
n3 = TreeNode(11)
n4 = TreeNode(2)
n4.left = n1
n5 = TreeNode(9)
n5.left = n2
n5.right = n3
root = TreeNode(4)
root.left = n4
root.right = n5
arr = [1,2,4,4,9,11]

if __name__ == "__main__":
    root = treeify(arr=arr)
    root.print_tree()
    