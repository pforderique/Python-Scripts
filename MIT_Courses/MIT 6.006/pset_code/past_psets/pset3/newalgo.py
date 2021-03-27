
import sys

# DO NOT REMOVE THIS LINE
sys.setrecursionlimit(10000)

# OUR HASH 
indices = dict()

def construct_preorder_traversal(inorder, postorder):
    """
    Args:
        inorder (list): the inorder traversal of the tree
        postorder (list): the postorder traversal of the tree

    Output:
        list: the preorder traversal of the tree.
    """

    # place every element in inorder list into hash table
    for i in range(len(inorder)):
        indices[inorder[i]] = i

    # call our function now
    return get_preorder(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)


def get_preorder(inorder:list, postorder:list, Istart, Iend, Pstart, Pend) -> list:
    if Istart > Iend or Pstart > Pend: return []

    # get last element (our root) from postorder
    root = postorder[Pend]
    # find its index in inorder 
    idx = indices[root]

    result = [root]
    result += get_preorder(inorder, postorder, Istart, idx - 1, Pstart, Pend - idx)
    result += get_preorder(inorder, postorder, idx + 1, Iend, idx - Istart, Pend - 1)

    return result

if __name__ == "__main__":
    # ino = ["a", "b", "c", "d", "e", "f", "g"]
    # post = ["a", "c", "b", "e", "g", "f", "d"]
    ino = ['j', 'k', 'l', 'm']
    post = ['k', 'm', 'l', 'j']
    print(construct_preorder_traversal(ino, post))
    # print("heelo")