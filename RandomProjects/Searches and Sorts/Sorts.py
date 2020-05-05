# SORTS SCRIPT

# =============================
#   BUBBLE SORT: Ascending
# =============================

def bubbleSort(L):
    swapped = True
    while swapped:
        swapped = False
        for idx in range(1,len(L)):
            if L[idx-1] > L[idx]:
                swapped = True
                L[idx-1],L[idx] = L[idx],L[idx-1]
    return L

def bubbleSortTest(L):
    comparisons = 0
    swaps = 0
    swapped = True
    while swapped:
        swapped = False
        for idx in range(1,len(L)):
            comparisons+=1
            if L[idx-1] > L[idx]:
                swapped = True
                L[idx-1],L[idx] = L[idx],L[idx-1]
                swaps += 1
                print('After',swaps,'swaps: '+str(L))
    print('Total Number of Comparisons:',comparisons)
    return L

# =============================
#   SELECTION SORT: Ascending
# =============================

def selectionSort(L):
    suffix = []
    for j in range(len(L)):
        minIdx = 0
        minNum = L[0]
        for idx in range(len(L)):
            if L[idx] < minNum:
                minNum = L[idx]
                minIdx = idx
        suffix.append(L[minIdx])
        del L[minIdx]
    return suffix

def selectionSortTest(L):
    suffix = []
    comparisons = 0
    for j in range(len(L)):
        minIdx = 0
        minNum = L[0]
        for idx in range(len(L)):
            comparisons += 1
            if L[idx] < minNum:
                minNum = L[idx]
                minIdx = idx
        suffix.append(L[minIdx])
        del L[minIdx]
        print(suffix)
    print('Number of Comparisons:',comparisons)
    return suffix

# =============================
#   MERGE SORT: Ascending
# =============================
mergeComparisons = 0
def merge(L1,L2):
    global mergeComparisons
    # print('At',mergeComparisons,'comparisons:'+str(L1)+' '+str(L2))
    result = []
    while len(L1) > 0 and len(L2) > 0:
        mergeComparisons += 1
        if L1[0] < L2[0]:
            result.append(L1[0])
            del L1[0]
        else:
            result.append(L2[0])
            del L2[0]
    if len(L1) > 0:
        result.extend(L1)
        # print('     result:'+str(result))
        return result
    elif len(L2) > 0:
        result.extend(L2)
        # print('     result:'+str(result))
        return result
    else:
        # print('     result:'+str(result))
        return result

def mergeSort(L):
    if len(L) == 0 or len(L) == 1:
        return L
    else:
        mid = len(L)//2
        return merge(mergeSort(L[mid:]),mergeSort(L[:mid]))

def mergeSortTest(L):
    if len(L) == 0 or len(L) == 1:
        return L
    else:
        mid = len(L)//2
        print('merge comparisons',mergeComparisons)
        return merge(mergeSortTest(L[:mid]),mergeSortTest(L[mid:]))
           
