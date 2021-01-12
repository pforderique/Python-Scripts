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

# 4.1 Design Algo that returns True iff there exists a path from S->E
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

# ____________________________________________________________________
# Testing

# Graph
    # S -> x -> y -> E
    # |-> redherring
E = Node("E")
S = Node("S", [Node("x", [Node("y", [E])]), Node("redherring")])

if __name__ == "__main__":
    print(existsPath(S, E))
