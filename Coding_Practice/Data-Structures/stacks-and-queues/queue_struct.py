# QUEUE Structure as outlined by CTCI
# 12-30-2020

# QUEUE (FIFO)
    # methods:
        # add(item): add item to end of the queue
        # remove(): Remove the first item from queue 
        # peek(): return top of the queue
        # isEmpty(): return True if empty
    # implementation:
        # just like stack, it can be implemented as linked list
        # Essentially the same as a LL 
    # PROS:
        # O(1) adds and removes
    # CONS: 
        # NOT O(1) access to ith item

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

    def isEmpty(self):
        return self.first == None
