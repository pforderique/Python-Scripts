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

def get_len(head: Node) -> int:
    '''returns the length of a linked list'''
    length = 1 
    n = head
    while n.next != None:
        length += 1 
        n = n.next
    return length

def kth_to_last(head: Node, k: int) -> Node:
    ''' returns the kth to last node in single linked list'''
    length = get_len(head)
    counter = 1
    curr = head
    while counter < length - k:
        curr = curr.next
        counter += 1
    return curr

def kth_to_last2(head: Node, k: int) -> Node: # what if we don't know the length?
    ''' returns the kth to last node in single linked list - using double pointer technique'''
    p1 = p2 = head
    # p2 will point to the node that is k nodes away from p2
    for i in range(k): 
        if p2 == None: raise ValueError("k value out of range")
        p2 = p2.next
    # iterate both until p2 hits the end of the list 
    while p2.next != None:
        p2 = p2.next
        p1 = p1.next
    return p1

# Driver Code
if __name__ == "__main__":
    ll = Node(1)
    ll.append_to_tail(2)
    ll.append_to_tail(3)
    ll.append_to_tail(5)
    ll.append_to_tail(8)
    print(ll)
    print("Length:", get_len(ll))
    print(kth_to_last2(ll, 1).data)