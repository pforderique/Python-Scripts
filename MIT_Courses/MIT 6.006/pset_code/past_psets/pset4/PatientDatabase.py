
#####################################
##### PLEASE DO NOT MODIFY THIS CODE
#####################################

class BST:
    def __init__(self, item = None, parent = None):
        "Initialize a BST node"
        self.item     = item
        self.parent   = parent
        self.left     = None
        self.right    = None

    def is_empty(self):       return self.item is None
    def is_right_child(self): return self.parent and (self.parent.right == self)
    
    def subtree_min(self):
        "Return node with minimum item key in subtree (assumes nonempty)"
        if self.left:
            return self.left.subtree_min()
        return self

    def subtree_find(self, k):
        "Return node from subtree having item with key k (assumes nonempty)"
        if k == self.item.key:
            return self
        if k < self.item.key and self.left:
            return self.left.subtree_find(k)
        if k > self.item.key and self.right:
            return self.right.subtree_find(k)
        return None

    def subtree_close(self, k): 
        '''
        Return node from (nonempty) subtree having either (assumes nonempty):
            - left-most item with smallest key >  query key k
            - right-most item with largest key <= query key k
        '''
        if k < self.item.key and self.left:
            return self.left.subtree_close(k)
        if k >= self.item.key and self.right:
            return self.right.subtree_close(k)
        return self

    def tree_successor(self):
        "Return next node in an in-order traversal of tree (assumes nonempty)"
        if self.right:
            return self.right.subtree_min()
        node = self
        while node.is_right_child():
            node = node.parent
        return node.parent

    def replace(self, node):
        "Replace self's attributes with node's attributes"
        self.item  = node.item
        self.left  = node.left
        self.right = node.right
        if self.left:   self.left.parent  = self
        if self.right:  self.right.parent = self
       
    def remove(self):
        "Remove self's item from subtree (assumes nonempty)"
        node = self
        if self.left and self.right:                    # has two children
            node = self.right.subtree_min()
            self.item = node.item
        if   node.right:    node.replace(node.right)    # has one child
        elif node.left:     node.replace(node.left)
        else:                                           # has no children
            if node.parent is None:         # root
                node.item = None
                return
            if node.is_right_child():       # right child
                node.parent.right = None
            else:                           # left child
                node.parent.left  = None
            node = node.parent
        node.maintain()

    def maintain(self):
        '''
        Perform maintenance after a dynamic operation
        Called by lowest node with subtree modified by insert or delete
        '''
        pass

    def find_min(self): 
        "Return an item with minimum key, else None"
        if self.is_empty(): return None
        node = self.subtree_min()
        return node.item if node else None

    def find(self, k):
        "Return an item with key k, else None"
        if self.is_empty(): return None
        node = self.subtree_find(k)
        return node.item if node else None

    def find_next(self, k): 
        "Return an item with smallest key greater than k, else None"
        if self.is_empty(): return None
        node = self.subtree_close(k) # guarenteed to have item
        if node.item.key <= k:
            node = node.tree_successor()
        return node.item if node else None

    def insert(self, x):
        "Insert item into self's subtree"
        if self.is_empty():
            self.item = x 
            self.maintain()
        elif x.key < self.item.key:
            if self.left is None:
                self.left  = self.__class__(None, self)
            self.left.insert(x)
        else:
            if self.right is None:
                self.right = self.__class__(None, self)
            self.right.insert(x)

    def delete(self, k):
        "Delete key k from self's subtree"
        if self.is_empty():
            raise IndexError('delete from empty data structure')  
        node = self.subtree_find(k)
        if node is None:
            raise IndexError('key not found in data structure')  
        item = node.item
        node.remove()
        return item

    def iter_recursive(self):
        if self.left:
            yield from self.left.iter_recursive()
        yield self.item
        if self.right:
            yield from self.right.iter_recursive()

    def iter_iterative(self):
        "Return iterator of subtree's nodes in order"
        node = self.subtree_min()
        while node:
            yield node.item
            node = node.tree_successor()

    def item_str(self):
        return str(self.item.key)

    def __str__(self):
        "Return ASCII drawing of the tree"
        if self.is_empty(): return '[Empty tree]'
        s = self.item_str()
        if self.left is None and self.right is None:
            return s
        sl, sr, sep = [''], [''], '_'
        if self.left:
            s = sep + s
            sl = str(self.left).split('\n')
        if self.right:
            s = s + sep
            sr = str(self.right).split('\n')
        wl, cl = len(sl[0]), len(sl[0].lstrip(' _'))
        wr, cr = len(sr[0]), len(sr[0].rstrip(' _'))
        a = [(' ' * (wl - cl)) + ('_' * cl) + s +
             ('_' * cr) + (' ' * (wr - cr))]
        for i in range(max(len(sl), len(sr))):
            ls = sl[i] if i < len(sl) else ' ' * wl
            rs = sr[i] if i < len(sr) else ' ' * wr
            a.append(ls + ' ' * len(s) + rs) 
        return '\n'.join(a)

class AVL(BST):
    def __init__(self, item = None, parent = None):
        "Augment BST with height and skew"
        super().__init__(item, parent)
        self.new_node = AVL
        self.height   = 0
        self.skew     = 0

    def update(self):
        "Update height and skew"
        left_height  = self.left.height  if self.left  else -1
        right_height = self.right.height if self.right else -1
        self.height  = max(left_height, right_height) + 1
        self.skew    = right_height - left_height

    def rotate_right(self):
        '''
        Rotate left to right, assuming left is not None
         __s__      __n__
        _n_  c  =>  a  _s_
        a b            b c
        Self and node swap contents so that subtree root does not change
        '''
        node, c = self.left, self.right
        a, b    = node.left, node.right 
        self.item, node.item = node.item, self.item
        if a:   a.parent = self
        if c:   c.parent = node
        self.left, self.right = a, node
        node.left, node.right = b, c
        node.update()
        self.update()

    def rotate_left(self):
        '''
        Rotate right to left, assuming right is not None
        __s__        __n__
        a  _n_  =>  _s_  c
           b c      a b   
        Self and node swap contents so that subtree root does not change
        '''
        a, node = self.left, self.right
        b, c    = node.left, node.right
        self.item, node.item = node.item, self.item
        if a:   a.parent = node
        if c:   c.parent = self
        self.left, self.right = node, c
        node.left, node.right = a, b
        node.update()
        self.update()

    def maintain(self):
        "Update height and skew and rebalance up the tree"
        self.update()
        if self.skew == 2:      # must have right child
            if self.right.skew == -1:
                self.right.rotate_right() 
            self.rotate_left()
        elif self.skew == -2:   # must have left child
            if self.left.skew == 1:
                self.left.rotate_left() 
            self.rotate_right()
        if self.parent:
            self.parent.maintain()

    def item_str(self):
        return str(self.item.key) + (
            '<' if 0 < self.skew else
            '>' if 0 > self.skew else '=')

##################
# Test your code #
##################
        

class Item:
    def __init__(self, key):
        self.key = key

def test_random(tree, population, num_inserts, num_deletes):
    from random import sample, choice
    print('Building new tree on %s random keys' % num_inserts)
    keys = sample(population, num_inserts)
    print('Keys: %s' % keys)
    print(str(tree)) 
    for key in keys:
        print('Inserting %s...' % key)
        tree.insert(Item(key))
        print(str(tree)) 
    print('Now deleting %s random keys' % num_deletes)
    for i in range(num_deletes):
        key = choice(population)
        print('Attemping to remove %s...' % key)
        try:
            item = tree.delete(key)
            print('%s removed!' % item.key)
            print(str(tree))
        except:
            print('%s not found... :(' % key)
    print('Iterate in-order (recursive)')
    print('%s' % [x.key for x in tree.iter_recursive()])
    print('Iterate in-order (iterative)')
    print('%s' % [x.key for x in tree.iter_iterative()])
    print('Repeatedly remove min')
    x = tree.find_min()
    while x:
        print('Removing %s...' % x.key)
        tree.delete(x.key)
        print(str(tree))
        x = tree.find_min()
    print('Inserting %s keys in order' % num_inserts)
    for i in range(num_inserts):
        tree.insert(Item(i))
    print(str(tree))

def test_BST(max_key, num_inserts, num_deletes):
    print('*' * 15)
    print('Testing BST')
    print('*' * 15)
    tree = BST()
    test_random(tree, range(max_key), num_inserts, num_deletes)

def test_AVL(max_key, num_inserts, num_deletes):
    print('*' * 15)
    print('Testing AVL')
    print('*' * 15)
    tree = AVL()
    test_random(tree, range(max_key), num_inserts, num_deletes)


#####################################
##### YOUR CODE IN THIS SECTION
#####################################

# do not modify this class
class Patient:
    def __init__(self, name, priority):
        self.key, self.name =  priority, name

# ITEM = Patient
class PatientDatabase(AVL):
    def __init__(self, item = None, parent = None):
        # do not change this line
        super().__init__(item, parent)

        if self.item: 
            self.num_nodes = 1
            self.min = self.max = self.item.key
        else: 
            self.num_nodes = 0
            self.min = None
            self.max = None # changed from 0 to None...? bc maybe min keeps at 0 all the way down
        
    def update(self):
        "updates the attributes of the current element"
        # do not change this line
        super().update()

        left_nodes  = self.left.num_nodes  if self.left   else 0
        right_nodes = self.right.num_nodes if self.right  else 0
        self.num_nodes = left_nodes + right_nodes + 1

        # if no children, your min and max are equal to your key
        if not self.left and not self.right: 
            self.min = self.max = self.item.key

        # elif only a left child, min = their min, keep your max
        elif self.left and not self.right: 
            self.min = self.left.min
            self.max = self.item.key

        # elif only a right child, max = thier max, keep your min
        elif self.right and not self.left: 
            self.min = self.item.key
            self.max = self.right.max

        # else, we have TWO CHILDREN. Adopt min of left and max of right
        else:
            self.min = self.left.min
            self.max = self.right.max
  
    # do not modify this function
    def update_patient(self, name,priority):
        "Change or update kid with name name and priority priority"
        try:
            patient = self.delete(priority)    # remove existing patient 
            patient.name = name             # update existing patient
        except:
            patient = Patient(name, priority)         # make new patient
        super().insert(patient)         # insert patient
    
    def num_patients(self,p1,p2):
        "return number of patients that have priority between p1 and p2"
        print(self.min, self.max)

        # return 0 if there isnt even an item (which means there isnt even a min or max for this node?)
        # if not self.item: return 0 
        # if self.min == self.max == None: return 0 # adding this line will take us from overshooting to always 0

        total = 0
        
        # if node range fully in [p1, p2], just return how many are in this subtree
        if p1 <= self.min and self.max <= p2:
            return self.num_nodes

        # elif node range is compltely outside of [p1, p2], return 0 -- no nodes here
        elif self.max < p1 or p2 < self.min:
            pass

        # else this node's range in only PARTIALLY in [p1, p2]
        else:

            #* check if this node's priority is in the range first
            if p1 <= self.item.key <= p2:
                total += 1

            #* check left
            if self.left:
                print("LEFT: ", self.left.item.key)
                print("LEFT NUM NODES: ", self.left.num_nodes)
                print("LEFT MIN: ", self.left.min)
                print("LEFT MAX: ", self.left.max)
                # node.left range fully in [p1, p2], just add how many are in this subtree
                if p1 <= self.left.min and self.left.max <= p2:
                    total += self.left.num_nodes
                    print("total incremented: ", total)
                
                # elif node.left range is compltely outside of [p1, p2], return 0 -- no nodes here
                elif self.left.max < p1 or p2 < self.left.min:
                    pass

                # else lets recurse on left
                else: total += self.left.num_patients(p1, p2)

            #* check right
            if self.right:
                # node.right range fully in [p1, p2], just add how many are in this subtree
                if p1 <= self.right.min and self.right.max <= p2:
                    total += self.right.num_nodes
                
                # elif node.right range is compltely outside of [p1, p2], return 0 -- no nodes here
                elif self.right.max < p1 or p2 < self.right.min:
                    pass

                # else lets recurse on right
                else: total += self.right.num_patients(p1, p2)

        return total


    def item_str(self):
        return str(self.item.key) + str(self.item.name) 


#####################################
##### PLEASE DO NOT MODIFY THIS CODE
#####################################

def testDB(ops):
    database = PatientDatabase() 
    i = 0
    ans = []
    for op in ops:
        if op[0] == 'q':
            _, t1, t2 = op
            sol = database.num_patients(t1, t2)
            ans.append(sol)
            i += 1
        else:
            name, priority = op
            database.update_patient(name, priority)
    return ans


#####################################
### MY TESTING
#####################################
if __name__ == "__main__":
    pass