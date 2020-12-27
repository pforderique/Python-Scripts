# Practice problems in CTCI
class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

    def append_to_tail(self, data):
        end = Node(data)
        n = self
        while(n.next != None):
            n = n.next
        n.next = end
    
    def __str__(self):
        if self.next == None: rep = "Node data: {}\nNext Node: NONE".format(self.data)
        else: rep = "Node data: {}\nNext Node: {}".format(self.data, self.next)
        return rep

