##################################################
##  Problem 3.5 Constructing Tree Traversals
##################################################
import sys

# DO NOT REMOVE THIS LINE
sys.setrecursionlimit(10000)

# OUR HASH 
indices = dict()
# keep track of the last element in the post order index
post_idx = 0 


def construct_preorder_traversal(inorder, postorder):
    """
    Args:
        inorder (list): the inorder traversal of the tree
        postorder (list): the postorder traversal of the tree

    Output:
        list: the preorder traversal of the tree.
    """

    # we will call the recursive function "backwards" (first right side, then left, then root itself)
    preorder_list = []

    # initialize post_idx reference that all recursive calls will refer to
    global post_idx
    post_idx = len(inorder) - 1
    

    # place every element in inorder list into hash table indicies for O(1) lookup
    for i in range(len(inorder)):
        indices[inorder[i]] = i
 
    get_preorder(inorder, postorder, 0, len(postorder) - 1, preorder_list)
     
    # have to reverse it because we recursed in backwards pre order order
    preorder_list.reverse()

    return preorder_list
    

def get_preorder(inorder, postorder, start, end, curr_pre_list):
    # base case: return if there are no elements between
    if(start > end): return
 
    # use the same post_idx established globally so that "last index" works out well
    global post_idx
    root = postorder[post_idx]   # get our next "root" element
    idx = indices[root]     # get the index from hash
    post_idx -= 1           # update post_idx so we get the next "last" element from postOrder next time
     
    # recurse BACKWARDS -- first right side, then left, finally the "root"
    get_preorder(inorder, postorder, idx + 1, end, curr_pre_list)
    get_preorder(inorder, postorder, start, idx - 1, curr_pre_list)  
    # add in this root in last
    curr_pre_list.append(root)
    return

# if __name__ == "__main__":
#     ino = ["a", "b", "c", "d", "e", "f", "g"]
#     post = ["a", "c", "b", "e", "g", "f", "d"]

#     in1 =   ['h', 'd', 'i', 'b', 'j', 'e', 'k', 'a', 'f', 'g', 'c']
#     post1 = ['h', 'i', 'd', 'j', 'k', 'e', 'b', 'g', 'f', 'c', 'a']
#     print(construct_preorder_traversal(ino, post))
#     print(construct_preorder_traversal(in1, post1))
