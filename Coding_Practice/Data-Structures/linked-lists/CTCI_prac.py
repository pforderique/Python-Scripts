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
        n = self
        rep = "" + str(n.data)
        while n.next != None:
            rep += " -> " + str(n.next.data)
            n = n.next
        return rep + " -> NONE"
        

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

# PRACTICE PROBLEMS
def remove_duplicates(head: Node) -> None:
    if not head: return None # return if head not initialized
    n = head
    seen = set({n.data})
    while(n.next != None):
        if n.next.data in seen:
            n.next = n.next.next
        else:
            seen.add(n.next.data)
        n = n.next

# Driver Code
if __name__ == "__main__":
    ll = Node(1)
    ll.append_to_tail(2)
    ll.append_to_tail(3)
    print(ll)