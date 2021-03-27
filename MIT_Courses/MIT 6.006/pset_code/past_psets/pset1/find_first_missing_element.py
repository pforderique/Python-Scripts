##################################################
##  Problem 4.4. Find order
##################################################

# Given a list of positive integers and the starting integer d, return x such that x is the smallest value greater than
# or equal to d that's not present in the list
def find_first_missing_element(arr, d):
    '''
    Inputs: 
        arr        (list(int)) | List of sorted, unique positive integer order id's
        d          (int)       | Positive integer of smallest possible value in arr
    Output: 
        -          (int)       | The smallest integer greater than or equal to d that's not present in arr
    '''
    
    if len(arr) == 0: return d
    if len(arr) == 1:
        if d != arr[0]: return d
        return arr[0] + 1

    mid = (len(arr)) // 2

    if arr[mid] == d + mid:
        return find_first_missing_element(arr[mid:], d + mid)
    else:
        return find_first_missing_element(arr[:mid], d)
