# Common searching and sorting algorithms
# Written by Piero Orderique
# Date Started: 12/21/2020

####################################################
############          SEARCHES          ############
####################################################
def binarysearch(target: object, arr: list) -> bool:
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

###################################################
############           SORTS           ############
###################################################
def insertionsort(arr: list) -> None:
    """returns original list but sorted
    >>> insertionsort([])
    []
    """
    # if empty, just go ahead and return empty list
    if arr == []: return arr
    # else, we start the sorted list with the first element
    # then we iterate through rest of the list - for every element left, 
        # insert it in our sorted array by swapping until no more swaps needed
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()