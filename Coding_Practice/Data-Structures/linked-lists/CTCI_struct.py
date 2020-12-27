# Structure as presented in CTCI
# 12 Oct 2020
# Revisited 27 Dec 2020

# Linked-List Structure 
# - access to linked list via reference to the head node
class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

    def appendToTail(self, data):
        end = Node(data)
        n = self
        while(n.next != None):
            n = n.next
        n.next = end

