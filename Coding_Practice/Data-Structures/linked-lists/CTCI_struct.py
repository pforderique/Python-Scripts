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
        if self.next == None: rep = "Node data: {}\nNext Node: NONE".format(self.data)
        else: rep = "Node data: {}\nNext Node: {}".format(self.data, self.next)
        return rep

# outside user-defined functions
def delete_node(head: Node, data: int) -> Node:
    if head == None: return None
    n = head
    if n.data == data: return head.next # moved head
    while n.next != None:
        if n.next.data == data:
            n.next = n.next.next
            return head # head didn't change
        n = n.next
    return head # data not found

if __name__ == "__main__":
    ll = Node(1)
    ll.append_to_tail(2)
    ll.append_to_tail(3)
    print(ll)
    print('-'*10)
    delete_node(ll, 2)
    print(ll)
    