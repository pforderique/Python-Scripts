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
        self.first = None
        self.last = None

    def add(self, item):
        t = self.QueueNode(item)
        if self.last != None: 
            self.last.next = t

        self.last = t
        if self.first == None:
            self.first = self.last

    def remove(self):
        if self.first == None: raise self.NoSuchElementException
        data = self.first.data
        self.first = self.first.next
        if self.first == None:
            self.last = None
        return data
    
    def peek(self):
        if self.first == None: raise self.NoSuchElementException
        return self.first.data

    def isEmpty(self):
        return self.first == None

    def __str__(self) -> str:
        # rep =  'first in queue: {}\nlast in queue: {}'.format(self.first.data, self.last.data)
        # return rep
        rep = ''
        n = self.first
        while n:
            rep += str(n.data) +' -> '
            n = n.next
        rep += 'None'
        return rep

# Testing
if __name__ == "__main__":
    queue = Queue()
    queue.add(5)
    queue.add(9)
    queue.add(19)
    print(queue)
