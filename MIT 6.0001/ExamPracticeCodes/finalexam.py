trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    # FILL IN YOUR CODE HERE
    if int(us_num) < 11:
        return trans[us_num]
    elif int(us_num) < 20:
        return 'shi '+trans[us_num[1]]
    else:
        tens_digit = us_num[0]
        ones_digit = us_num[1]
        answer = ''
        if int(ones_digit) != 0:
            return trans[tens_digit] + ' shi '+trans[ones_digit]
        else:
            return trans[tens_digit] + ' shi'

# print(convert_to_mandarin('36')) #will return san shi liu)

def longest_run1(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    # Your code here

    #find longest increasing 
    list_of_inc = []
    longest_inc = []
    for i in range(1, len(L)):
        if L[i] >= L[i-1]:
            longest_inc.append(L[i-1])
            # if we are at the last one, go ahead and append the last term too if its bigger.
            if (L[i] >= L[i-1] and i < len(L)-1 and L[i+1] < L[i]):
                longest_inc.append(L[i])
        else:
            list_of_inc.append(longest_inc)
            longest_inc = []
    list_of_lens = [len(sublist) for sublist in list_of_inc]
    longest_inc = list_of_inc[list_of_lens.index(max(list_of_lens))]

    #find longest decreasing
    list_of_dec = []
    longest_dec = []
    for i in range(1, len(L)):
        if L[i] <= L[i-1]:
            longest_dec.append(L[i-1])
            # if we are at the last one, go ahead and append the last term too if its bigger.
            if (L[i] <= L[i-1] and i < len(L)-1 and L[i+1] > L[i]):
                longest_dec.append(L[i])
        else:
            list_of_dec.append(longest_dec)
            longest_dec = []
    list_of_lens = [len(sublist) for sublist in list_of_dec]
    longest_dec = list_of_dec[list_of_lens.index(max(list_of_lens))]

    if len(longest_inc) >= len(longest_dec):
        return sum(longest_inc)
    else:
        return sum(longest_dec)
    
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    # Your code here

    dec_count = 0
    inc_count = 0
    maxcount = 0
    result = 0

    for char in range(len(L) - 1):
        if (L[char] <= L[char + 1]):
            dec_count += 1
            if dec_count > maxcount:
                maxcount = dec_count
                result = char + 1
        else:
            dec_count = 0
        if (L[char] >= L[char + 1]):
            inc_count += 1            
            if inc_count > maxcount:
                maxcount = inc_count
                result = char + 1
        else:
            inc_count = 0
        
    startposition = result - maxcount
    return sum(L[startposition:result + 1])

# L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
# print(longest_run(L))

