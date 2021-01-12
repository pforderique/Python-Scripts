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

class Queue:
    class QueueNode:
        def __init__(self, data=None) -> None:
            self.data = data
            self.next = None

    class NoSuchElementException(Exception):
        pass

    def __init__(self) -> None:
        self.first = None
        self.last = None

    def add(self, item):
        t = self.QueueNode(item)
        if self.last != None: 
            self.last.next = t

        self.last = t
        if self.first == None:
            self.first = self.last

    def remove(self):
        if self.first == None: raise self.NoSuchElementException
        data = self.first.data
        self.first = self.first.next
        if self.first == None:
            self.last = None
        return data
    
    def peek(self):
        if self.first == None: raise self.NoSuchElementException
        return self.first.data

    def isEmpty(self):
        return self.first == None

    def __str__(self) -> str:
        # rep =  'first in queue: {}\nlast in queue: {}'.format(self.first.data, self.last.data)
        # return rep
        rep = ''
        n = self.first
        while n:
            rep += str(n.data) +' -> '
            n = n.next
        rep += 'None'
        return rep

def visit(node:Node):
    print(node)

# DFS - like pre order traversal! Root -> left -> right
def DFS(root:Node):
    if root == None: return
    visit(root)
    root.visited = True
    for node in root.adjacent:
        if node.visited == False:
            DFS(node)

# BFS - NOT RECURSIVE! Use a QUEUE!!! (iterative solution = best solution)
def BFS(root:Node):
    queue = Queue()
    root.visited = True
    queue.add(root) # add to the end of queue

    while not queue.isEmpty():
        r = queue.remove() # remove tree node from front of queue
        visit(r)
        for node in r.adjacent:
            if node.visited == False:
                node.visited = True
                queue.add(node)

# Driver Code:
# --------------------------------------------
# root node picture:
    #          1
    #       /  |  \
    #      2   0   3
    #     / \     / \
    #    4   5   6   7
root = Node(1, [
    Node(2, [
        Node(4),
        Node(5)
    ]), 
    Node(0),
    Node(3, [
        Node(6),
        Node(7)
    ])
    ])
# graph wrapper class (only if it contains disconnected components)
graph = Graph(nodes=[root])

if __name__ == "__main__":
    BFS(root)
