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

def sum_lists_err(head1: Node, head2: Node) -> Node:
    '''adds two nums represented by linked lists and outputs linked list result'''
    n1 = head1
    n2 = head2
    curr_sum = n1.data + n2.data
    res = Node(curr_sum % 10)
    carry_over = curr_sum // 10
    while (n1.next and n2.next) or carry_over != 0: # while there are more nodes OR carry over bits
        current_sum = n1.next.data + n2.next.data + carry_over
        remainder = current_sum % 10 
        carry_over = current_sum // 10
        res.append_to_tail(remainder)
        # iterate to next
        n1 = n1.next
        n2 = n2.next
    # works, but not if we need to go one further digit OR what if we need to extend further? fix this later!
        # finish writing on paper - thinking about having 2 separate "end conditions" to check which one is None and then add the carryover bit!
    return res

def sum_lists(head1: Node, head2: Node) -> Node: # decided to rewrite 
    res = Node() # dummy head
    carry = 0
    n1, n2 = head1, head2
    while True:
        if not(n1 or n2):
            if carry == 1: res.append_to_tail(1)
            break
        Sum = carry
        if n1: 
            Sum += n1.data
            n1 = n1.next
        if n2: 
            Sum += n2.data
            n2 = n2.next
        remainder = Sum % 10
        carry = 1 if Sum > 9 else 0
        res.append_to_tail(remainder)
    return res.next # return the actual head, not the dummy one

# Driver Code
if __name__ == "__main__":
    ll = Node(1)
    ll.append_to_tail(5)
    ll.append_to_tail(3)
    print(ll)
    LL = Node(2)
    LL.append_to_tail(7)
    LL.append_to_tail(6)
    print(LL)
    print(sum_lists(ll, LL))