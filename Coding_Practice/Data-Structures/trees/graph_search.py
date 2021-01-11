# Graph Searching Algorithms
# Piero Orderique
# 11 Jan 2021

# SIDE_NOTE:
    # fixed login authentication error with git by running: git config --global credential.helper winstore
    # from https://stackoverflow.com/questions/11693074/git-credential-cache-is-not-a-git-command

# Structures - adjacency list implementation
class Graph:
    def __init__(self, nodes=[]) -> None:
        self.nodes = nodes

class Node:
    def __init__(self, data, adjacent=[]) -> None:
        self.data = data 
        self.adjacent = adjacent
        self.visited = False # used for searching!

    def __str__(self) -> str:
        rep = 'Data: ' + str(self.data)
        return rep

def visit(node:Node):
    print(node)

# DFS
def DFS(root:Node):
    if root == None: return
    visit(root)
    root.visited = True
    for node in root.adjacent:
        if node.visited == False:
            DFS(node)

# Driver Code
if __name__ == "__main__":
    root = Node(1, [
        Node(2, [
            Node(4),
            Node(5)
        ]), 
        Node(3, [
            Node(6),
            Node(7)
        ])
        ])
    DFS(root)