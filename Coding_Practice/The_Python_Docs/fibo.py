# Fibonacci numbers module

# This script only exists as an example for thepythontutorial.py 's sec6() method. Ignore.

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# you can make the file usable as a script as well as an importable module by adding this code at the end of your module:
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))