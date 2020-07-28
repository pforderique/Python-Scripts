def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    mid = int(len(aStr)/2)
    if (mid == 0 or mid == len(aStr)) and char != aStr[mid]:
        return False
    elif char == aStr[mid]:
        return True
    elif char > aStr[mid]:
        return isIn(char, aStr[mid+1:])
    elif char < aStr[mid]:
        return isIn(char, aStr[:mid])
    else:
        return False
    
# print(isIn('!','abcdeg'))

