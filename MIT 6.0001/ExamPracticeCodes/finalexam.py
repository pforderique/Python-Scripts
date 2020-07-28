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
            return trans[tens_digit] + ' shi '

# print(convert_to_mandarin('36')) #will return san shi liu)

