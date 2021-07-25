class PriorityQueue:                      # Hash Table Implementation
    def __init__(self, size):                   # stores keys with unique labels
        self.A = [float('inf') for _ in range(size)]
        self.min = float('inf')

    def insert(self, label, key):         # insert labeled key
        self.A[label] = key
        
    def extract_min(self):                # return a label with minimum key
        self.min = float('inf')
        min_label = -1
        for label, dist in enumerate(self.A):
            if dist != None and dist <= self.min:
                min_label = label
                self.min = dist
        self.A[min_label] = None
        return min_label
        # min_label = None
        # for label in self.A:
        #     if (min_label is None) or (self.A[label] < self.A[min_label]):
        #         min_label = label
        #         del self.A[min_label]
        #         return min_label
                
    def decrease_key(self, label, key):   # decrease key of a given label
        if (label in self.A) and (key < self.A[label]):
            self.A[label] = key

def try_to_relax(adj, w, d, parent, u, v):
    if d[v] > d[u] + w[(u,v)]:
        print(f'relaxing node {v} from {d[v]} to {d[u]} + {w[(u,v)]}')
        d[v] = d[u] + w[(u,v)]
        parent[v] = u

def dijkstra(Adj, w, s):                            # Adj: adjacency list, w: weights, s: start
    d = [float('inf') for _ in Adj]                 # shortest path estimates d(s, v)
    parent = [None for _ in Adj]                    # initialize parent pointers
    d[s], parent[s] = 0, s                          # initialize source
    V = len(Adj)                                    # number of vertices
    Q = PriorityQueue(V)                             # initialize empty priority queue
    
    for v in range(V):                              # loop through vertices
        Q.insert(v, d[v])                           # insert vertex-estimate pair
    
    for _ in range(V):                              # main loop
        u = Q.extract_min()     
        print(f'min extracted: {u} with dist {d[u]}')                    # extract vertex with min estimate
        for v in Adj[u]:                            # loop through out-going edges
            try_to_relax(Adj, w, d, parent, u, v)
            Q.decrease_key(v, d[v])                 # update key of vertex

    return d, parent


adj = { 0: [],
        1: [2, 3],
        2: [4],
        3: [2, 4],
        4: [],           }

w = { (1, 2): 3,
      (2, 4): 3,
      (1, 3): 1,
      (3, 2): 1,
      (3, 4): 5, }

distances, parents = dijkstra(adj, w, 1)
print(distances)
print(parents)

'''
Code not working. extract min was not extracting min...
'''