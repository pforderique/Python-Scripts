# Graphs 
# Piero Orderique
# 11 Jan 2021

# Connected iff there is path between every pair of vertices
# cyclic or acyclic

# How to Represent??

# Method 1: Adjacency List (Most Common)
    # every node stores a list of adjacent vertices
    # WE NEED GRAPH CLASS because, unlike a tree, we can't expect to reach everything from one node (can have unconnected subgraphs!)

class Graph:
    nodes = []

class Node:
    name = ''
    children = []

# hell, you don't even need additional classes. You can just use an array (or hashtable) of lists!
    # its more compact, but not as clean. Use classes unless you have reason otherwise

# Method 2: Adjaceny Matrices
    # NxN (N = # nodes) matrix where a_ij is True iff theres an edge from i to j
    # Matrix will be symmetric for an undirected graph
    # mostly less efficent when using BFS, etc. but still viable 
