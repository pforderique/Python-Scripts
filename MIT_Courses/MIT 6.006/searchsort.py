# Common searching and sorting algorithms
# Written by Piero Orderique
# Date Started: 12/21/2020

def binarysearch(target: object, arr: str) -> bool:
    """input a list and return True if target in arr. Assumes arr is sorted ascending
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

if __name__ == "__main__":
    import doctest
    doctest.testmod()



