# Heap Practice Module 
# Dec 15 2020
# 11 Jan 2021

# TODO
def array_to_heap(arr):
    '''
    returns a heap data structure 
    '''
    pass

# MIN HEAP
    # COMPLETE binary tree where each node is SMALLER than its children
    # root is minimum element in tree

    # Key Operations:
        # insert O(logn)
            # start by inserting at bottom left to right in order to maintain complete property
            # now we fix min heap tree by swapping the new element with its parent until we find appropriate spot
        # extract_min O(1) (fixing is O(logn))
            # remove min element (root) and replace it with last element in tree (bottommost rightmost)
            # now, bubble down this element (swapping with its children) until min heap prop is restored


if __name__ == "__main__":
    h = [9,5,2,1,4,3,7,8,6]