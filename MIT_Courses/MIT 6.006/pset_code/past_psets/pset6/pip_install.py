##################################################
##  pip-install
##################################################
import sys

# DO NOT REMOVE THIS LINE
sys.setrecursionlimit(100000)

def determine_install_order(dependencies):
    """
    Args: 
        dependencies (list): adjacency list showing which libraries each library is dependent on

    Output:
        int: The minimum number of sessions needed to install all libraries or None if there is no valid install order
    """

    # GET A TOPO SORT: IF THERES A CYCLE, RETURN NONE!!!
    topo_list = topo_sort(dependencies)
    if topo_list is True: return None

    # create DAA for set numbers    
    L = len(dependencies)
    set_number = [None]*L

    # place each node in correct set 
    for node in topo_list:
        if dependencies[node] == []: 
            set_number[node] = 0
            continue
        max_set = 0
        for neighbor in dependencies[node]:
            if set_number[neighbor] != None and set_number[neighbor] > max_set: 
                max_set = set_number[neighbor]
        set_number[node] = max_set + 1

    # create our total sets result
    total_sets = max(set_number) if set_number else 0

    res = [set() for i in range(total_sets+1)]

    for node in topo_list:
        res[set_number[node]].add(node)

    real_res = []
    for sett in res:
        if len(sett) != 0:
            real_res.append(sett)

    return len(real_res)

def topo_sort_helper(adjlist, i, seen, finsihed, topo_list):
    seen[i] = True
    finsihed[i] = True # finished within THIS recursion set

    # DFS essentially
    for node in adjlist[i]:
        if not seen[node]:
            if topo_sort_helper(adjlist, node, seen, finsihed, topo_list) is True: return True
        elif finsihed[node]: return True

    finsihed[i] = False # no longer in this recursion "set"
    topo_list.append(i)
    return False

def topo_sort(adjlist):
    '''TODO: How do we go back to make sure we visit all nodes?? --- answered: for loop bro '''
    topo_list = []
    L = len(adjlist)
    seen = [False]*L
    finished = [False]*L

    #! for loop to iterate through each node! want to make sure each node in topo list
    for i in range(L):
        if not seen[i]: 
            if topo_sort_helper(adjlist, i, seen, finished, topo_list) is True: return True

    return topo_list