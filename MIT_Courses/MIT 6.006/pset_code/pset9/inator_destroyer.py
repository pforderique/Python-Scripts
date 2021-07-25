import sys
sys.setrecursionlimit(50000)

def nestible(a:tuple, b:tuple):
    '''
    TRUE dimensions of box b can be nested inside of box a
    a,b are tuples of h,w,l
    '''
    l_a,w_a,h_a = a
    l_b,w_b,h_b = b

    nestible = [
        l_a > l_b and w_a > w_b and h_a > h_b,
        l_a > l_b and w_a > h_b and h_a > w_b,
        l_a > w_b and w_a > h_b and h_a > l_b,
        l_a > w_b and w_a > l_b and h_a > h_b,
        l_a > h_b and w_a > w_b and h_a > l_b,
        l_a > h_b and w_a > l_b and h_a > w_b,
    ]
    return any(nestible)

def mergeSort(myList) -> list:
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if nestible(right[j][0],left[i][0]):
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

    return myList

def inator_destroyer(inators,incinerator_size):
    """
    inputs 
        inators: a list of tuples of the format ((height,width,length),evil_potential)
        incinerator_size: a tuple of (height,width,length) of the incinerator
    return value:
        a list of tuples of the format (height,width,lenth) [allowed to be returned in any order] such that this subset of the boxes 
        can nest inside each other in the incinerator and evil potential is maximized
    """

    inators = list(inators)

    '''    
    idx_incinerator = 0
        for idx, box in enumerate(inators):
        if box[1] is None: 
            idx_incinerator = idx
            # print(idx_incinerator)
            break'''
    
    #* filter out those that are NOT nestible within our incinerator
    feasible_inators = []
    for box in inators:
        if nestible(incinerator_size, box[0]): 
            feasible_inators.append(box)

    sorted_boxes = mergeSort(feasible_inators) # small to large
    sorted_boxes.append(((float('inf'), float('inf'), float('inf')), 0))
    sorted_boxes.reverse() # largest to smallest

    n = len(sorted_boxes)

    parent = dict()
    included = dict()
    best_inators = []

    memo = dict()

    def T(i:int,j:int) -> int:
        '''
        pass in i,j = ((h,l,w), e)
        '''

        if n > 1:
            box_i = sorted_boxes[i]
            box_j = sorted_boxes[j]

            i_size, e_i = box_i[0], box_i[1]
            j_size, e_j = box_j[0], box_j[1]

            # base case
            if i == n-1:
                if nestible(j_size, i_size): 
                    # best_inators.append(sorted_boxes[n-1][0])
                    parent[(i,j)] = None
                    included[(i,j)] = 1
                    return sorted_boxes[n-1][1]
                else:
                    parent[(i,j)] = None
                    included[(i,j)] = 0
                    return 0

            elif nestible(j_size, i_size):
                if (i+1,j) in memo: 
                    opt1 = memo[(i+1,j)] 
                else: 
                    opt1 = T(i+1,j)
                    memo[(i+1,j)] = opt1

                if (i+1, i) in memo: 
                    opt2 = memo[(i+1, i)]
                else: 
                    opt2 = e_i + T(i+1, i)
                    memo[(i+1, i)] = opt2
                
                max_ =  max( opt1, opt2 )

                if max_ == opt1: 
                    parent[(i,j)] = (i+1,j)
                    included[(i,j)] = 0
                elif max_ == opt2: 
                    # best_inators.append(sorted_boxes[i][0])
                    parent[(i,j)] = (i+1, i)
                    included[(i,j)] = 1

                return max_

            else:
                parent[(i,j)] = (i+1,j)
                included[(i,j)] = 0

                if (i+1,j) in memo: 
                    return memo[(i+1,j)]
                else: 
                    t = T(i+1,j)
                    memo[(i+1,j)] = t
                    return t
    
        else:
            return None

    ans = T(1,0)
    # print(f'\n{ans}')

    if ans is None: return []

    best_inators = []
    curr = (1,0) #* (i,j)
    while curr: 
        # print(f"curr = {curr}")

        parent_box_size = sorted_boxes[curr[0]][0]
        if included[curr]:
            best_inators.append(parent_box_size)

        curr = parent[curr]

    # print(set(best_inators))
    return list(set((best_inators)))