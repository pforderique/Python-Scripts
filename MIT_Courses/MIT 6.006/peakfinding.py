# Peak finding algorithm

def find_peak(arr):
    '''
    Finds a peak in the array and returns its index
    
    a[i] is a peak if a[i-1] < a[i] > a[i+1]
    if a[i] is edge, then just check if its greater than the one it's touching
    '''
    #check edge cases first:
    if len(arr) == 0 or len(arr) == 1:
        return -1
    elif arr[0] > arr[1]:
        return 0
    elif arr[len(arr)-1] > arr[len(arr)-2]:
        return len(arr)-1
    else:
        pass #implement here from idx 1 to len()-2
    

if __name__ == "__main__":
    s = [1,2,3,4,5,3]
    print(find_peak(s))