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
