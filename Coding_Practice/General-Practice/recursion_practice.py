# Beefing up recursion skills
# 24 December 2020

# recursive array sum
def sumarr(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sumarr(arr[1:])

# GEEKS FOR GEEKS RECURSION PRACTICE
def isPalindrome(num: int):
    str_num = str(num)
    if len(str_num) == 0 or len(str_num) == 1: return True
    if str_num[0] == str_num[-1]: return isPalindrome(str_num[1:len(str_num)-1])
    return False

# FIBONACCI DP Practice
def fib1(n):
    '''Worst fib function. Returns nth fib number. Exponential time.'''
    if n <= 0: return -1
    if n == 1 or n == 2: return 1
    else: return fib1(n-1)+fib1(n-2)



if __name__ == "__main__":
    # print(isPalindrome(2002), isPalindrome(1492), isPalindrome(29492), isPalindrome(30201))
    print(fib1(20))