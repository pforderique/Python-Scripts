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

class TreeNode:
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

class LinkedListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def append_to_tail(self, data):
        end = LinkedListNode(data)
        n = self
        while(n.next != None):
            n = n.next
        n.next = end

    def __str__(self):
        n = self
        rep = "" + str(n.data)
        while n.next != None:
            rep += " -> " + str(n.next.data)
            n = n.next
        return rep + " -> NONE"

# 4.1 Route Between Nodes : Design Algo that returns True iff there exists a path from S->E - CORRECT!
# I wil be using BFS for path finding
from collections import deque
from random import choice, randint
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

# 4.3 List of Depths : Given BT, design algo that creates a linked list of all the nodes at each depth
# ex: if tree has depth d, output should be d linked lists
def ll_depths(root:TreeNode) -> list:
    '''takes in root from tree and returns list of linked lists'''
    # initialize our queue, result, and temporary level head
    queue = deque([])
    queue.append(root)
    result = [LinkedListNode(root)]
    head = LinkedListNode(None)
    # counter variables to help us know when we reached new level
    counter = 1
    exp = 2
    # BFS with queue - keep track of level and append new linked lists
    while len(queue) != 0:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
            head.append_to_tail(node.left)
        if node.right:
            queue.append(node.right)
            head.append_to_tail(node.right)
        # update our counter by 2 and check if we entered new level
        counter += 2
        if counter == 2**exp - 1:
            result.append(head.next)
            head = LinkedListNode(None)
            exp += 1
    return result

# 4.4 CheckBalanceed : Given BT, return True iff BT is not uneven by more than one level 
def isBalanced(root:TreeNode) -> bool:
    # check if root is a single leaf node
    if not root.left and not root.right: return True

    # else check subtrees
    flag = get_height(root=root)
    return bool(flag)

def get_height(root:TreeNode):
    if root is None: return 0 

    # else calculate subtree heights and return False if algo finds them to be unbalanced
    left_hieght = get_height(root.left)
    if left_hieght is False: return False

    right_height = get_height(root.right)
    if right_height is False: return False
    
    # get root's height by the max of of its subtree heights plus one
    height = max(left_hieght, right_height) + 1

    # check if root is at least 3 levels high and is "missing" a subtree - if so, it is unbalanced
    if height > 2 and not (root.right and root.left): return False
    else: return height

# 4.5 Validate BST : Given BT, return True iff it is a BST
def isBST(root:TreeNode):
    arr = []

    # in order traversal stores BST in ascending order
    def in_order_traversal(root:TreeNode):
        if root:
            in_order_traversal(root.left)
            arr.append(root.data)
            in_order_traversal(root.right)
    in_order_traversal(root)

    # return True if arr is in ascending order
    def isSorted(arr:list):
        prev = arr[0]
        for elem in arr:
            if elem < prev: 
                return False
            prev = elem
        return True

    return isSorted(arr)

# 4.7 Build Order : Given projects and dependencies list, find valid build order
def create_build_order(projects:list, dependencies:list) -> list:
    projects_left = projects[:]
    dependencies_left = dependencies[:]
    build_order = []
    # error class
    class LoopError(Exception):
        pass
    # helper function
    def create_build():
        if not dependencies_left: return # base case if no more dependencies left
        # else get the firsts and seconds
        firsts = set()
        seconds = set()
        for (first, second) in dependencies_left:
            firsts.add(first)
            seconds.add(second)
        # raise error if loop
        heads = firsts - seconds
        if not heads: raise LoopError('DAG not possible')
        # else add all heads to build order and remove them from lists
        for head in heads:
            build_order.append(head)
            projects_left.remove(head)
            for tup in dependencies_left:
                if tup[0] == head:
                    dependencies_left.remove(tup)
        # keep filling in build order until we have processed all
        create_build()
    # after call, extend whatever projects are left (they wont have dependencies!)
    create_build()
    if projects_left: build_order.extend(projects_left)
    return build_order

# 4.8 First Common Ancestor : Return the node that is the first common ancestor of p and q
def get_first_common_ancestor(root:TreeNode, p:TreeNode, q:TreeNode) -> TreeNode:
    # returns true if p is a descendant of the root node
    def isDescendant(root:TreeNode, p:TreeNode) -> bool:
        if root:
            if p == root: return True
            return isDescendant(root.left, p) or isDescendant(root.right, p)
        return False
    # find nearest ancestor
    if isDescendant(root, p) and isDescendant(root, q):
        if root.left and isDescendant(root.left, p) and isDescendant(root.left, q):
            a = get_first_common_ancestor(root.left, p, q)
            if a: return a
        if root.right and isDescendant(root.right, p) and isDescendant(root.right, q):
            b = get_first_common_ancestor(root.right, p, q)
            if b: return b
        return root
    return None

# 4.10 Check Subtrees : Return True if T2 is a subtree of T1 where T1 >> T2
def isSubtree(T1:TreeNode, T2:TreeNode) -> bool:
    queue = deque()
    queue.append(T1)
    while len(queue) != 0:
        node = queue.popleft()
        if node == T2: return True
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    return False

# 4.11 Random Node : Implement BST class with insert, find, delete, and randomNode()
class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.all_descendants = [self]
        self.choices = [0]
    
    def insert(self, node):
        if node.data <= self.data:
            # insert it to the left if nothing is there 
            if self.left is None: self.left = node
            else: self.left.insert(node)
        else: 
            # else the data is larger so go on to the right
            if self.right is None: self.right = node
            else: self.right.insert(node)
        self.all_descendants.append(node)
        self.choices.append(0)
        
    def delete(self, node):
        queue = deque()
        queue.append(self)
        while queue:
            n = queue.popleft()
            if n == node:
                self.all_descendants.remove(n)
                n = None
                break
            if n.left: queue.append(n.left)
            if n.right: queue.append(n.right)

    def find(self, node):
        queue = deque()
        queue.append(self)
        while queue:
            n = queue.popleft()
            if n == node:
                return True
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return False

    # Slow Working. Better Solution is to keep track of sizes and use that to
    # calculate probability of moving right or left 
    def get_random_node(self):
        rand = randint(0, len(self.all_descendants) - 1)
        self.choices[rand]+=1
        return self.all_descendants[rand]

    def __str__(self) -> str:
        return str(self.data)

def printTree(root:BSTNode):
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        node = queue.popleft()
        print(node)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

# 4.12 Paths with Sum : Given BT containing ints, design algo to count number of paths 
# that sum to a given value. Path does NOT have to start or end at the root or leaf,
# you can only travel downwards

# ____________________________________________________________________
# Test Data:

# Graph
    # S -> x -> y -> E
    # |-> andre
# E = Node("E")
# S = Node("S", [Node("x", [Node("y", [E])]), Node("andre")])

# BST: - my function produced better BST - left to right!
    #      4
    #     / \
    #    2   9
    #   /   / \
    #  1   5   11
def init_test_tree() -> TreeNode:
    testNode = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(5)
    n3 = TreeNode(11)
    n4 = TreeNode(2)
    n4.left = n1
    # n4.right = testNode
    n5 = TreeNode(9)
    n5.left = n2
    n5.right = n3
    root = TreeNode(4)
    root.left = n4
    root.right = n5
    return root

def init_projects_and_dependencies():
    return ['a', 'b', 'c', 'd', 'e', 'f'], [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]

# arr = [1,2,4,4,9,11]

# Driver
if __name__ == "__main__":
    # root = init_test_tree()
    # print(get_first_common_ancestor(root, n2, n1))
    # projects_list, dependencies_list = init_projects_and_dependencies()
    # print(create_build_order(projects=projects_list, dependencies=dependencies_list))
    root = BSTNode(4)
    root.insert(BSTNode(2))
    root.insert(BSTNode(1))
    root.insert(BSTNode(9))
    root.insert(BSTNode(5))
    root.insert(BSTNode(11))
    printTree(root)
    print(f'Random Choice: {root.get_random_node()}')
