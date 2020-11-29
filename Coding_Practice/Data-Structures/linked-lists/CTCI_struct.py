# Structure as presented in CTCI
# 12 Oct 2020

# Linked-List Structure
class node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

    def appendToTail(self, data):
        self.end = node(data)
        
