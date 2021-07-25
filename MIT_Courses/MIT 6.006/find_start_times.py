def find_start_times(constraints):
    """Find the start times that follows the provided constraints.

    Args:
        constraints(List[Tuple[str, str, int]]): A list of tuples
            `(a, b, t)` where `a` and `b` are strings that contain
            variable names such that `a - b <= t`.
    
    Returns:
        A python dictionary where keys are variables and values are
        their correct assignments.
        `None` if it is not possible.
    """
    print()
    # create adjacency and weights list:
    adj = dict()
    w = dict()
    vertices = set()

    for constraint in constraints:
        a, b, t = constraint
        vertices.add(a)
        vertices.add(b)

        w[(b,a)] = t

        if not b in adj: adj[b] = [a]
        else: adj[b].append(a)

    s1 = constraints[0][1]
    return bellman_ford(vertices, adj, w, s1)
    

def try_to_relax(adj, w, d, parent, u, v):
    if d[v] > d[u] + w[(u,v)]:
        # print(f'relaxing node {v} from {d[v]} to {d[u]} + {w[(u,v)]} = {d[u]+w[(u,v)]}')
        d[v] = d[u] + w[(u,v)]
        parent[v] = u

def bellman_ford(vertices, Adj, w, s):          # Adj: adjacency list, w: weights, s: start
    # initialization
    infinity = 1e9                              # number greater than sum of all + weights
    d = {node:infinity for node in vertices}    # shortest path estimates d(s, v)
    parent = {node:None for node in vertices}   # initialize parent pointers
    d[s], parent[s] = 0, s                      # initialize source

    # construct shortest paths in rounds
    V = len(Adj)                      # number of vertices
    for k in range(V - 1):            # relax all edges in (V - 1) rounds
        for u in vertices:            # loop over all edges (u, v)
            if u in Adj:
                for v in Adj[u]:          # relax edge from u to v
                    try_to_relax(Adj, w, d, parent, u, v)

    # check for negative weight cycles accessible from s
    for u in vertices:                # Loop over all edges (u, v)
        if u in Adj:
            for v in Adj[u]:
                if d[v] > d[u] + w[(u,v)]:  # If edge relax-able, report cycle
                    return None
    return d