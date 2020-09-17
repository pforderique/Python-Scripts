# finds the reduced sum of a number 
# ex: DigitSum(4034) = 4+0+3+4 = 11 = 1+1 = 2
def DigitSum(num):
    if num < 10:
        return num
    else:
        sumOfDigits = sum(getDigits(num))
        return DigitSum(sumOfDigits)

# returns a list of of the digits of num
def getDigits(num):
    digits = []
    divisor = 10
    while num > 0:
        digit = num%10
        digits.append(digit)
        num = num//10
    return digits

#Driver Code
print(DigitSum(4034))