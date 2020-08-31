### Code Signal Practice Questions
#####################################

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

#P1 - Correct
def removeKFromList(l, k):
    fakeHead = ListNode(None)
    fakeHead.next = l
    current = fakeHead
    while current:
        while current.next and current.next.value == k:
            current.next = current.next.next
        current = current.next
    return fakeHead.next

#P2 - Passed 20/22
def isListPalindrome(l):
    #traverse linked list once, record vals in stack
    stack = []
    curr = l
    while curr:
        stack.append(curr.value)
        curr = curr.next
        
    #traverse again, comparing stack.pop to curr.val
    curr = l
    while curr:
        if curr.value != stack.pop():
            return False
        curr = curr.next
    return True
    