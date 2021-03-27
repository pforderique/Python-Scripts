# Python3 program to print Postorder traversal from given
# Inorder and Preorder traversals.
postIndex = 0
 
# Fills preorder traversal of tree with given
# inorder and postorder traversals in a stack
def fillPre(In, post, inStrt, inEnd, s, hm):
    global postIndex
    if(inStrt > inEnd):
        return
 
    # Find index of next item in postorder traversal in
    # inorder.
    val = post[postIndex]
    inIndex = hm[val]
    postIndex -= 1
     
    # traverse right tree
    fillPre(In, post, inIndex + 1, inEnd, s, hm)
 
    # traverse left tree
    fillPre(In, post, inStrt, inIndex - 1, s, hm)   
    s.append(val)
 
# This function basically initializes postIndex
# as last element index, then fills stack with
# reverse preorder traversal using printPre
def printPreMain(In, post):
    global postIndex
    Len = len(In)
    postIndex = Len - 1
    s = []
     
    # Insert values in a hash map and their indexes.
    hm = {}
    for i in range(len(In)):
        hm[In[i]] = i
 
    # Fill preorder traversal in a stack 
    fillPre(In, post, 0, Len - 1, s, hm)
     
    # Print contents of stack
    while(len(s) > 0):
        print(s.pop(), end = " ")
 
# Driver code
ino = ["a", "b", "c", "d", "e", "f", "g"]
post = ["a", "c", "b", "e", "g", "f", "d"]
printPreMain(ino, post)