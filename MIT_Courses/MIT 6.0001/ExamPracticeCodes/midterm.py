it = 1
def fancy_divide(numbers, index):
    global it
    print('iter:',it, ' index is ',index)
    it+=1
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print('iter:',it)
        print("0")

# fancy_divide([0, 2, 4], 4)

def closest_power(base, num):
    result = 0
    if base > num:
        result = 0
    elif base == num:
        result = 1
    else:
        for i in range(1, int(num)):
            if abs(base**i - num) <= abs(base**(i + 1) - num):
                result = i
                break
    return result
            
# print(closest_power(4,62))

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    # Your code here
    L.reverse()
    for i in range(len(L)):
        L[i].reverse()

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # Your code here
    inter = {}
    diff = {}
    for key in d1.keys():
        if key in d2.keys():
            inter[key] = f(d1[key], d2[key])
        else:
            diff[key] = d1[key]
    for key in d2.keys():
        if key not in d1.keys():
            diff[key] = d2[key]
    return (inter, diff)

def f(a,b):
    return a+b

# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
# print(dict_interdiff(d1, d2))

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    L_copy = L[:]
    L[:] = []
    for num in L_copy:
        if g(f(num)) == True:
            L.append(num)
    if len(L) == 0:
        return -1
    else:
        return max(L)

# def f(i):
#     return i + 2
# def g(i):
#     return i > 5
# L = [0, -10, 5, 6, -4]
# print(applyF_filterG(L, f, g))
# print(L)

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    L =[]
    print(type(aList))
    for element in aList:
        if type(element) != list:
            L.append(element)
        else:
            L.extend(flatten(element))
    return L
            
# print(flatten([ [1,'a',['cat'],2 ] ,[ [[3]],'dog' ], 4, 5 ])) # prints [1,'a','cat',2,3,'dog',4,5]

# print(flatten([1,[2]])) #
