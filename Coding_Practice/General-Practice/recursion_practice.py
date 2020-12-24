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

if __name__ == "__main__":
    # print(isPalindrome(2002), isPalindrome(1492), isPalindrome(29492), isPalindrome(30201))