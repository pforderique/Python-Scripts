# Common searching and sorting algorithms
# Written by Piero Orderique
# Date Started: 12/21/2020

####################################################
############          SEARCHES          ############
####################################################
def binarysearch(target: object, arr: list) -> bool:
    """input a list and return True if target in arr. Assumes arr is sorted ascending. 
    O(lgn) time, O(1) space?
    >>> binarysearch(10, [])
    False
    >>> binarysearch(3, [1,2,3])
    True
    >>> binarysearch(3, [2])
    False
    """
    # if empty, return false
    if arr == []: return False
    # else look in middle array
    mid = len(arr)//2
    if target == arr[mid]: return True
    # if target is less, look in left half
    elif target < arr[mid]: return binarysearch(target, arr[0:mid])
    # else, let's check in right half
    else: return binarysearch(target, arr[mid+1:]) # could produce out of bounds error

###################################################
############           SORTS           ############
###################################################
def insertionsort(arr: list) -> None:
    """returns original list but sorted. 
    O(n^2) time, O(1) space
    """
    # if empty, just go ahead and return empty list
    if arr == []: return None
    # else, we iterate through elems of the list - for every element, 
    for idx in range(0, len(arr)):
        # insert it in our sorted array by swapping until no more swaps needed, going backwards
        for idx2 in range(idx-1, -1, -1):
            if arr[idx] < arr[idx2]: 
                # swap if greater and continue
                arr[idx], arr[idx2] = arr[idx2], arr[idx]
                idx -= 1 # (no worries, this wont mess with actual counter)
                continue
            # if its greater or equal to previous, then leave it there
            else: break
        
def mergesort(arr: list) -> list:
    """mutates list by performing merge sort on it"""
    # check if empty or contains only one element first
    if len(arr) == 0 or len(arr) == 1: return arr
    # else mutate the list
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)
    

def merge(arr1: list, arr2: list) -> list:
    """merges 2 lists using two finger algorithm"""
    res = []
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] < arr2[0]:
            res.append(arr1[0])
            del arr1[0]
        else:
            res.append(arr2[0])
            del arr2[0]
    res.extend(arr1)
    res.extend(arr2)
    return res
 
if __name__ == "__main__":
    from doctest import testmod
    testmod()
    
    a1 = [66, 36, 2, 66, 34, 34, 82, 82, 38, 39, 97, 19, 99, 27, 59, 79, 42, 57, 96, 
    77, 26, 66, 59, 66, 50, 30, 86, 60, 4, 65, 23, 28, 39, 42, 55, 10, 43, 50, 66, 9]
    # a1 = [4,8,2,6,6]
    print("original:", a1)
    new = mergesort(a1)
    # new = merge([4,8], [2,6,6])
    print("sorted:", new)