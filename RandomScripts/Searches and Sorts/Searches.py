#SEARCHES SCRIPT:
    #assumes sorted lists are in ascending order

# =============================
#   LINEAR SEARCHES
# =============================

def linearSearchBool(L, target):
    for e in L:
        if e == target:
            return True
    return False

def linearSearch(L, target):
    for idx, e in enumerate(L):
        if e == target:
            return idx
    return -1

def linearSearchBoolTest(L, target):
    comparisons = 0
    for e in L:
        comparisons+=1
        print("Comparison Number:",comparisons)
        if e == target:
            print('Element Found after',comparisons,'comparisons')
            return True
    return False

def linearSearchTest(L, target):
    comparisons = 0
    for idx, e in enumerate(L):
        comparisons+=1
        print("Comparison Number:",comparisons)
        if e == target:
            print('Element Found after',comparisons,'comparisons at index',idx)
            return idx
    return -1

# =============================
#   BINARY/BISECTION/LOGARITHMIC SEARCHES
# =============================
comparisons = 0

def binarySearchBool(L, target):
    middleIdx = len(L)//2
    if len(L) == 1 and L[middleIdx] != target:
        return False
    if L[middleIdx] == target:
        return True
    elif target < L[middleIdx]:
        return binarySearchBool(L[:middleIdx],target)
    else:
        return binarySearchBool(L[middleIdx:],target)

def binarySearchBoolTest(L,target,count=1):
    print('Comparison number:',count)
    middleIdx = len(L)//2
    if len(L) == 1 and L[middleIdx] != target:
        print('Element NOT in list. Total Comparisons:',count)
        return False
    if L[middleIdx] == target:
        print("Element found after",count,"comparisons.")
        return True
    elif target < L[middleIdx]:
        return binarySearchBoolTest(L[:middleIdx],target,count+1)
    else:
        return binarySearchBoolTest(L[middleIdx:],target,count+1)

def binarySearch(L, target):
    middleIdx = len(L)//2
    if len(L) == 1 and L[middleIdx] != target:
        return -1
    if L[middleIdx] == target:
        return middleIdx
    elif target < L[middleIdx]:
        return binarySearch(L[:middleIdx],target)
    else:
        return binarySearch(L[middleIdx:],target)

def binarySearchTest(L,target,count=1):
    print('Comparison number:',count)
    middleIdx = len(L)//2
    if len(L) == 1 and L[middleIdx] != target:
        print('Element NOT in list. Total Comparisons:',count)
        return -1
    if L[middleIdx] == target:
        print("Element found after",count,"comparisons.")
        return middleIdx
    elif target < L[middleIdx]:
        return binarySearchBoolTest(L[:middleIdx],target,count+1)
    else:
        return binarySearchBoolTest(L[middleIdx:],target,count+1)

