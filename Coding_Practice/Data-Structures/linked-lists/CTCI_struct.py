# Structure as presented in CTCI
# 12 Oct 2020
# Revisited 27 Dec 2020

# Linked-List Structure 
# - access to linked list via reference to the head node
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
        if self.next == None: rep = "Node data: {}\nNext Node: NONE\n".format(self.data)
        else: rep = "Node data: {}\nNext Node: {}\n".format(self.data, self.next)
        return rep

# outside user-defined functions
def delete_node(self, head: Node, data) -> Node:
    if head == None: return None
    n = head


if __name__ == "__main__":
    ll = Node("Piero")
    ll.append_to_tail("Fabrizzio")
    n = ll
    n = n.next
    print(ll)
    print(n)