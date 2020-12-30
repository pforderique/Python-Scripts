# Stack Structure as outlined by CTCI

# STACK (LIFO)
    # methods:
        # pop(): remove top item from stack
        # push(item): add item to stack
        # peek(): return item on top
        # isEmpty(): return True if empty
    # PROS:
        # O(1) adds and removes
    # CONS: 
        # NOT O(1) access to ith item

class Stack:
    class StackNode():
        def __init__(self, data) -> None:
            self.data = data
            self.next = None

    class EmptyStackException(Exception):
        pass
    
    def __init__(self) -> None:
        self.top = self.StackNode()

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

# However, according to the Python Tutorial, we can use array for a stack??
# here is my take on this: 
class myStack():
    class EmptyStackException(Exception):
        pass
    def __init__(self) -> None:
        self.stack = []
    def pop(self):
        if not self.stack: raise self.EmptyStackException
        return self.stack.pop()
    def push(self, item):
        self.stack.append(item)
    def peek(self):
        if not self.stack: raise self.EmptyStackException
        return self.stack[-1]
    def isEmpty(self):
        return self.stack == []
    