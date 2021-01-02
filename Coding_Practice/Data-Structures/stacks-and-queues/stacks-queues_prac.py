# CTCI Practice Problems
# 31 December 2020

# Structures
class Stack:
    class StackNode():
        def __init__(self, data=None) -> None:
            self.data = data
            self.next = None

    class EmptyStackException(Exception):
        pass
    
    def __init__(self, data=None) -> None:
        self.top = self.StackNode(data=data)

    def pop(self):
        if self.top == None: raise self.EmptyStackException
        item = self.top.data
        self.top = self.top.next
        return item
    
    def push(self, item):
        t = self.StackNode(item)
        t.next = self.top
        self.top = t

    def peek(self):
        if self.top == None: raise self.EmptyStackException
        return self.top.data

    def isEmpty(self):
        return self.top == None

    def __str__(self) -> str:
        rep = '-'*5 + '\n'
        n = self.top
        while n:
            rep += str(n.data)+'\n'
            n = n.next
        rep += '-'*5
        return rep

class Queue:
    class QueueNode:
        def __init__(self, data=None) -> None:
            self.data = data
            self.next = None

    class NoSuchElementException(Exception):
        pass

    def __init__(self) -> None:
        self.first = self.QueueNode()
        self.last = self.QueueNode()

    def add(self, item):
        t = self.QueueNode(item)
        if self.last != None: 
            self.last.next = t

        self.last = t
        if self.first == None:
            self.first = self.last

    def remove(self):
        if self.first == None: raise self.NoSuchElementException
        data =  self.first.data
        self.first = self.first.next
        if self.first == None:
            self.last = None
        return data
    
    def peek(self):
        if self.first == None: raise self.NoSuchElementException
        return self.first.data
        
# Practice
def split_array(arr: list, divisions: int) -> list:
    '''splits arr into #divisions stacks. Returns list of stacks'''
    stacks = [Stack() for i in range(divisions)]
    for i in range(len(arr)):
        stacks[i%divisions].push(arr[i])
        print(stacks)
    return stacks

# min stack pseudocode:
    # gets min in O(1) time
    # solution:
        # keep min always on top
        # when pushing, check if new item is greater than top. Switch if it is
        # recursively apply this again? No wait, then pushing could be O(N) :/
    # solution attempt 2:
        # keep a sorted list (descending) of elements
        # pops from this list give you min in O(1)
        # pop from stack is O(1), but removal in list is O(logN) (binary search)
        # push from stack is O(1), but insertion into list is O(logN)
    # CTCI's Solution:
        # at each top node, record what it THINKS the min is.
        # this way, push and pop is O(1),
        # and getting min would require peekmin() which can be O(1)
        # nice!

class SetOfStacks:
    '''
    DATA STRUCTURE: Set of Stacks
    Composed of:
        several stacks and should create a new stack once the previous one exceeds capacity
        pop() and push() should behave identicall to that of a SINGLE stack
    '''
    def __init__(self, capacity) -> None:
        self.stacks = Stack() # stack of stacks and their current space availability
        self.stacks.top = None
        self.capacity = capacity

    def push(self, item):
        """push onto stack. if capacity is reached, create a new stack"""
        if self.stacks.top == None: # if there are no stacks, start "new" stack of stacks
            self.stacks = Stack([Stack(item), 1])
        elif self.stacks.peek()[1] == self.capacity: # add a new stack if last capacity reached
            self.stacks.push([Stack(item), 1]) 
        else: # else, there is enough space to add to current top stack
            self.stacks.top.data[0].push(item)
            self.stacks.top.data[1] += 1 

    def pop(self):
        """pops from latest stack. Removes stacks as the empty"""
        if self.stacks.top == None: # if there are no stacks, raise exception
            raise self.stacks.EmptyStackException("NO MO STACKS!")

        value = self.stacks.top.data[0].pop()
        self.stacks.top.data[1] -= 1

        if self.stacks.top.data[1] == 0: # if stack is empty get rid of this stack completey
            self.stacks.top = self.stacks.top.next

        return value

    def printStacks(self):
        print("*"*10)
        outter_node = self.stacks.top
        while outter_node:
            inner_stack = outter_node.data[0]
            inner_node = inner_stack.top
            while inner_node:
                print(inner_node.data)
                inner_node = inner_node.next
            print("*"*10)
            outter_node = outter_node.next
    
    def __str__(self) -> str:
        rep = '-'*5 + '\n'
        n = self.top
        while n:
            rep += str(n.data)+'\n'
            n = n.next
        rep += '-'*5
        return rep

if __name__ == "__main__":
    # stack = Stack(3)
    # stack.push(4)
    # print("INPUT STACK:\n" + str(stack))
    plates = SetOfStacks(capacity=3)
    plates.push("Plate 1")
    plates.push("Plate 2")
    plates.push("Plate 3")
    plates.push("Plate 4")
    plates.push("Plate 5")
    plates.push("Plate 6")
    plates.push("Plate 7")

    plates.printStacks()


